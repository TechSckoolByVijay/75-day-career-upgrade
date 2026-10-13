from app import MemoryStore, create_app


def client():
    return create_app(MemoryStore()).test_client()


def test_health_is_always_ok():
    assert client().get("/healthz").status_code == 200


def test_ready_with_memory_store():
    assert client().get("/readyz").get_json()["status"] == "ready"


def test_add_and_list_notes():
    c = client()
    assert c.post("/notes", json={"text": "learn kubectl"}).status_code == 201
    assert c.get("/api/notes").get_json()["notes"] == ["learn kubectl"]


def test_empty_note_is_rejected():
    assert client().post("/notes", json={"text": "  "}).status_code == 400
