from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Joel Hosting</title>
        <style>
            body {
                background-color: #0b1120;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 40px;
            }
            h1 {
                color: #00d4ff;
                font-size: 42px;
            }
            p {
                font-size: 18px;
                color: #cbd5e1;
            }
            .card {
                background: #1e293b;
                padding: 20px;
                margin: 20px auto;
                width: 320px;
                border-radius: 12px;
                box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
            }
            .price {
                font-size: 22px;
                color: #22c55e;
                font-weight: bold;
            }
            a {
                display: inline-block;
                margin-top: 25px;
                padding: 12px 25px;
                background: #22c55e;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Joel Hosting</h1>
        <p>
        Creamos páginas web profesionales, rápidas y modernas para negocios que quieren crecer en internet.
        Nos encargamos de todo: diseño, publicación y soporte.
        </p>

        <div class="card">
            <h2>🌐 Página Web Profesional</h2>
            <p>Diseño moderno + optimización móvil</p>
            <p class="price">$50 USD</p>
        </div>

        <div class="card">
            <h2>⚡ Mantenimiento & Hosting</h2>
            <p>Soporte, actualizaciones y seguridad</p>
            <p class="price">$5 USD mensual</p>
        </div>

        <a href="https://wa.me/18294257569">📲 Solicita tu página ahora</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
