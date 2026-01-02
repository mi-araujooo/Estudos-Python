from flask import Flask, render_template,  request, jsonify #importa o flask
from game import fazer_jogada,  verificar_vitoria, resetar
app = Flask(__name__) #Cria a aplicação

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/jogada', methods=['POST'])
def jogada():
    dados = request.json
    index = dados.get("index")
    resultado = fazer_jogada(index)
    if resultado["valida"]:
        fim = verificar_vitoria()
        resultado["resultado"] = fim
    else:
        resultado["resultado"] = None
    return jsonify(resultado)
    print(resultado)

@app.route('/reset', methods=['POST'])
def reset():
    resetar()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
