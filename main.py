from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)
