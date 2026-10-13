from app import create_app, redact


def test_secrets_never_reach_the_llm():
    seen = {}

    def spy(text):
        seen["text"] = text
        return "ok"

    c = create_app(llm=spy).test_client()
    r = c.post("/explain", json={"error": "auth failed for vijay@example.com password=Hunter2 token: abc123"})
    assert r.status_code == 200
    assert "Hunter2" not in seen["text"] and "abc123" not in seen["text"]
    assert "vijay@example.com" not in seen["text"]
    assert r.get_json()["redactions"] == 3


def test_llm_failure_returns_502_not_a_crash():
    def broken(_):
        raise TimeoutError()

    r = create_app(llm=broken).test_client().post("/explain", json={"error": "x"})
    assert r.status_code == 502


def test_empty_request_is_rejected():
    assert create_app().test_client().post("/explain", json={}).status_code == 400


def test_redact_storage_connection_string():
    text, n = redact("DefaultEndpointsProtocol=https;AccountName=x;AccountKey=abc/def==;EndpointSuffix=core")
    assert "abc/def" not in text and n == 1
