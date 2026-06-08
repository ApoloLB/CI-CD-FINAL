from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"mensagem": "TaskFlow API ativa"}

def test_create_task():
    client = app.test_client()
    response = client.post("/tasks", json={"titulo": "Teste"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["titulo"] == "Teste"
    assert data["concluida"] is False

def test_list_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_error_404():
    client = app.test_client()
    # Tenta atualizar uma tarefa com ID 999 que não existe
    response = client.put("/tasks/999")
    assert response.status_code == 404
    assert response.get_json() == {"erro": "Tarefa não encontrada"}