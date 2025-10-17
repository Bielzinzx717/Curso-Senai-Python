from pathlib import Path
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

# pp = Flask(__name__)
# pp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
# pp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(pp)

@app.route("/")
def home():
    tarefas = [
        {"titulo": "Estudar Flask", "descricao": "Configurar projeto e entender rotas.", "concluida": True},
        {"titulo": "Criar API", "descricao": "Definir endpoints REST para tarefas.", "concluida": False},
        {"titulo": "Conectar DB", "descricao": "Integrar SQLAlchemy e migrar modelos.", "concluida": False},
    ]
    return render_template("index.html", tarefas=tarefas)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    concluida = db.Column(db.Boolean, default=False)


    from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    concluida = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    tarefas = Task.query.all()
    return render_template('index.html', tarefas=tarefas)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
