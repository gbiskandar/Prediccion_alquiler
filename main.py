from flask import Flask, render_template, request, redirect, url_for, jsonify
from predict import query, estimacion
from constants import *

app = Flask(__name__)

#ruta para la pagina principal
@app.route('/')
def index():
    return render_template('index.html')

#ruta para el formulario de valoración de viviendas
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        tipo = request.form['tipo']
        distrito = request.form['distrito']
        barrio = request.form['barrio']
        hab = int(request.form['hab'])
        banos = int(request.form['banos'])
        area = float(request.form['area'])
        furnished = request.form['muebles']

        # Se pasa la solicitud del usuario por la funcion de query para conseguir la solicitud encoded
        solicitud = query(tipo, distrito, barrio, hab, banos, area, furnished)
    
        # Proceder con la valoracion en base a la solicitud del usuario
        prediction = estimacion(solicitud)

        return render_template('prediction.html', prediction=prediction)
    return render_template('form.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    
    # Extraer detalles del JSON recibido
    tipo = data['tipo']
    distrito = data['distrito']
    barrio = data['barrio']
    hab = data['hab']
    banos = data['banos']
    area = data['area']
    furnished = data['furnished']

    # Se pasa la solicitud de full stack por la funcion de query para conseguir la solicitud encoded
    solicitud = query(tipo, distrito, barrio, hab, banos, area, furnished)
    
    # Obtener la valoracion
    prediction = estimacion(solicitud)

    # Return la valoracion del modelo en JSON
    return jsonify({'prediction': prediction})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, port=3500)