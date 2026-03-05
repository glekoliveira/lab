from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "CI/CD funcionando e validado! Agora vai, não sou tao burro 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)