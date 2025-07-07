from flask import Flask, request
import main  # importa seu script renomeado

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run_pipeline():
    main.main()  # chama a função principal do seu script
    return "Pipeline executado com sucesso!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
