from pathlib import Path
from flask import Flask, render_template, jsonify

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

def get_tarefas():
    return [
        {"id": 1, "titulo": "Estudar Flask", "descricao": "Rotas e templates", "concluida": True},
        {"id": 2, "titulo": "Criar API", "descricao": "Endpoints REST", "concluida": False},
        {"id": 3, "titulo": "Conectar DB", "descricao": "SQLAlchemy e migrações", "concluida": False},
    ]

# SSR (páginas)
@app.route("/")
def home():
    return render_template("index.html", tarefas=get_tarefas())

# API (JSON)
@app.route("/api/tarefas")
def api_tarefas():
    return jsonify(get_tarefas())

if __name__ == "__main__":
    app.run(debug=True)
