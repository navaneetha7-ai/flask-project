from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask DevOps App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: white;
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            h1 { color: #667eea; font-size: 2.5em; }
            .badge {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                margin: 5px;
                font-size: 0.9em;
            }
            .status {
                background: #00c853;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
                margin-top: 20px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Flask DevOps App</h1>
            <h3>👩‍💻 Team Navaneetha</h3>
            <br>
            <span class="badge">🐍 Python Flask</span>
            <span class="badge">🐳 Docker</span>
            <span class="badge">☁️ AWS EC2</span>
            <span class="badge">🔄 CI/CD</span>
            <span class="badge">📦 GitHub Actions</span>
            <div class="status">✅ Live & Running on AWS!</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)