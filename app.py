from flask import Flask, jsonify

app = Flask(__name__)

# Ruta para el endpoint GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': 'Hola Chad este es tu ordinario y si aparece este mensaje es porque lo lograste'}), 200

# Ejecución de la app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
 
