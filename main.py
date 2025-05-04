from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'clave_segura'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ElementalEsplay.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_user = db.Column(db.String(16), unique=True, nullable=False)
    nombre = db.Column(db.String(16), nullable=False)
    apellido1 = db.Column(db.String(16), nullable=False)
    apellido2 = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    dni = db.Column(db.String(9), unique=True, nullable=False)
    contraseña=db.Column(db.String(200), nullable=False)
    monedero = db.Column(db.Numeric(8, 2), nullable=False)


error_login=False
error_register=0
EMAIL_ORIGEN = 'elementalesplay@gmail.com'
EMAIL_PASSWORD = 'ubhkuplxwcesryhw'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/agua')
def agua():
    return render_template('agua.html')


@app.route('/aire')
def aire():
    return render_template('aire.html')


@app.route('/fuego')
def fuego():
    return render_template('fuego.html')


@app.route('/tierra')
def tierra():
    return render_template('tierra.html')

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

# =======================================================================================================================================
@app.route('/calendario')
def calendario():
    return render_template("actividades.html", actividades=ACTIVIDADES)

@app.route('/minijuego')
def minijuego():
    return render_template("juego.html")

ACTIVIDADES = []
INSCRIPCIONES = {}

@app.route('/nueva_actividad', methods=['GET', 'POST'])
def crear_actividad():
    if request.method == 'POST':
        nueva = {
            "id": len(ACTIVIDADES) + 1,
            "nombre": request.form['nombre'],
            "fecha": request.form['fecha'],
            "lugar": request.form['lugar'],
            "cupo": int(request.form['cupo']),
            "inscritos": 0,
            "estado": request.form['estado']
        }
        ACTIVIDADES.append(nueva)
        INSCRIPCIONES[nueva['id']] = []
        return redirect(url_for('calendario'))
    return render_template('nueva_actividad.html')

@app.route('/inscribirse/<int:actividad_id>', methods=['GET', 'POST'])
def inscribir(actividad_id):
    actividad = next((a for a in ACTIVIDADES if a['id'] == actividad_id), None)
    if not actividad:
        return "Actividad no encontrada", 404
    if request.method == 'POST':
        usuario = request.form['usuario']
        if actividad['estado'] == 'Abierta' and actividad['inscritos'] < actividad['cupo']:
            INSCRIPCIONES[actividad_id].append(usuario)
            actividad['inscritos'] += 1
            actividad['cupo'] -= 1
            actividad['estado'] = 'Cerrada' if actividad['inscritos'] >= actividad['cupo'] else 'Abierta'
            return redirect(url_for('calendario'))
        else:
            return "No se puede inscribir", 400
    return render_template('inscribirse.html', actividad=actividad)

if __name__ == '__main__':
    app.run(debug=True)