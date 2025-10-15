# from flask import Flask  
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
# db = SQLAlchemy(app)


# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     titulo = db.Column(db.String(100), nullable=False)
#     descricao = db.Column(db.String(200))
#     concluida = db.Column(db.Boolean, default=False)


#     def __repr__(self):
#         return f'<taks {self.titulo}>'
    
# with app.app_context():
#     db.create_all()
    


# with app.app_context():
#     nova_tarefa = Task(titulo= "estudar Flask", descricao = "aprender sobre modelagem de dados ")
#     db.session.add(nova_tarefa)
#     db.session.commit()

#     tarefas = Task.query.all()
#     print(tarefas)




# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     tarefas = [
#         {"titulo": "Estudas Flask", "concluida": True},
#         {"titulo": "Criar API", "concluida": False},
#     ]
#     return render_template ("index.html", tarefas=tarefas)

# if __name__ == '__main__':
#     app.run(debug=True)







from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    concluida = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return f'<taks {self.titulo}>'
    
with app.app_context():
    db.create_all()
    


with app.app_context():
    nova_tarefa = Task(titulo= "estudar Flask", descricao = "aprender sobre modelagem de dados ", concluida = True)
    db.session.add(nova_tarefa)
    db.session.commit()

    tarefas = Task.query.all()
    print(tarefas)



# app = Flask(__name__)

@app.route('/')
def index():  
    tarefas == Task.query.all()
    return render_template('index.html',  tarefas=tarefas)

if __name__ =='__main__':
    app.run(debug=True)