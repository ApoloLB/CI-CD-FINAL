from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    return jsonify({"mensagem": "TaskFlow API ativa"})

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "titulo" not in data:
        return jsonify({"erro": "O campo 'titulo' é obrigatório"}), 400
        
    task = {
        "id": len(tasks) + 1,
        "titulo": data["titulo"],
        "concluida": False
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks)

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    for task in tasks:
        if task["id"] == id:
            task["concluida"] = True
            return jsonify(task)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)