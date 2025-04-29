from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_user = db.Column(db.String(100), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido1 = db.Column(db.String(100), nullable=False)
    apellido2 = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    dni = db.Column(db.String(9), unique=True, nullable=False)
    contraseña=db.Column(db.String(200), nullable=False)
    monedero = db.Column(db.Numeric(20, 2), nullable=False)

error_login=False
error_register=0


@app.route('/')
def index():
    global error_login
    global error_register
    error_login = False
    error_register=0
    return render_template('index.html', users=User.query.all())

@app.route('/add_user', methods=['POST'])
def crear_user():
    global error_register
    if User.query.filter_by(name_user=request.form.get('name_user')).first():
        error_register = 1
        return redirect('/register')
    if User.query.filter_by(dni=request.form.get('dni')).first() or User.query.filter_by(email=request.form.get('email')).first():
        error_register = 2
        return redirect('/register')
    db.session.add(User(name_user=request.form.get('name_user'), nombre=request.form.get('nombre'), apellido1=request.form.get('apellido1'), apellido2=request.form.get('apellido2'), email=request.form.get('email'), contraseña=generate_password_hash(request.form.get('contraseña')), monedero=0, dni=request.form.get('dni')))
    db.session.commit()
    return redirect('/')

@app.route('/register')
def register():
    return render_template('register.html',error_register=error_register)

@app.route('/login')
def login():
    global error_login
    return render_template('login.html',error_login=error_login)

@app.route('/comprobar_user', methods=['POST'])
def comprobador_user():
    global error_login
    if not User.query.filter_by(name_user=request.form.get('name_user')).first():
        error_login = True
        return redirect('/login')
    elif check_password_hash(User.query.filter_by(name_user=request.form.get('name_user')).first().contraseña, request.form.get('contraseña')):
        return redirect('/')
    error_login = True
    return redirect('/login')



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
