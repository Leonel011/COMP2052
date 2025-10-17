from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.get("/info")
def info():
    return jsonify({
        "sistema" : "Demo Flask",
        "endpoints" : ["/info (GET)" , "/crear_usuario (POST)" , "/usuarios(GET)"]
    })

@app.post("/crear_usuario")
def crear_usuario():
    data = request.get_json(silent=True) or {}
    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or correo:
        return jsonify({"error": "nombre y correo son requeridos"}), 400
    
    usuario = {"nombre" : nombre, "correo": correo}
    usuarios.append(usuario)
    return jsonify({"mensaje" : "Usuario creado" , "usuario": usuario}), 201

@app.get("/usuarios")
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)