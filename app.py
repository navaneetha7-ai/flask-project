from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask DevOps App | Team Navaneetha</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                background: rgba(255,255,255,0.05);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 24px;
                padding: 50px;
                text-align: center;
                max-width: 600px;
                box-shadow: 0 30px 80px rgba(0,0,0,0.5);
            }
            .logo { font-size: 3em; margin-bottom: 10px; }
            h1 {
                color: white;
                font-size: 2.2em;
                font-weight: 700;
                margin-bottom: 5px;
            }
            .subtitle {
                color: #a78bfa;
                font-size: 1em;
                margin-bottom: 30px;
                letter-spacing: 2px;
                text-transform: uppercase;
            }
            .divider {
                border: none;
                border-top: 1px solid rgba(255,255,255,0.1);
                margin: 25px 0;
            }
            .tech-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 12px;
                margin: 20px 0;
            }
            .tech-card {
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 12px;
                padding: 15px 10px;
                color: white;
                font-siz