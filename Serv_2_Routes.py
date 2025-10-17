from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "nombre_app": "Mi Aplicacion Flask",
        "Version" : "1.0",
        "descripcion": "Ejemplo basico de arquitectura Cliente Servidor"
})

# Ruta Post
@app.route("/mensaje", methods = ["POST"])
def mensaje():
    data = request . get_json()
    usuario = data.get("usuario", "Invitado")
    mensaje = data.get("mensaje","Sin mensaje")
    return jsonify({
        "respuesta": f"Hola {usuario} , recibi tu mensaje: '{mensaje}'"
})

if __name__ == "__main__":
    app.run(debug=True)