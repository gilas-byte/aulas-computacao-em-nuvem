from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "projeto": "Radar ENEM",
        "disciplina": "Computacao em Nuvem",
        "status": "online"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/aluno/<nome>")
def aluno(nome):
    ambiente = os.getenv("AMBIENTE", "desenvolvimento")
    return jsonify({
        "aluno": nome,
        "ambiente": ambiente,
        "mensagem": "Bem-vindo ao Mini Radar ENEM"
    })

@app.route("/nota/<int:nota>")
def consultar_nota(nota):
    if nota >= 600:
        classificacao = "acima de 600"
    else:
        classificacao = "abaixo de 600"
    
    return jsonify({
        "nota": nota,
        "classificacao": classificacao
    })

@app.route("/professor/<nome>")
def professor(nome):
    escola = os.getenv("ESCOLA", "Unisenai")
    return jsonify ({
        "professor": nome,
        "escola": escola,
        "mensagem": "Bem vindo ao painel do professor"
    })

@app.route("/nota/aluno/<nome>/media")
def media(nome):
    notas = [600, 750, 500, 450] # pode ser substituido depois pelas notas no banco de dados
    media = sum(notas) / len(notas)

    return jsonify ({
        "aluno": nome,
        "media": media
    })

if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)