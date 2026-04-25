from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Hello from Team Navaneetha!</h1>
    <p>Flask App deployed on AWS EC2</p>
    <p>Built with Docker & GitHub Actions CI/CD</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)