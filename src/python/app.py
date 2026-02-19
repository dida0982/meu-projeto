from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form["nome"]
    return f"Olá {nome}"

if __name__ == "__main__":
    app.run(debug=True)
