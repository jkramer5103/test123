from flask import Flask, request, render_template_string

app = Flask(__name__)

# Funktion zur Berechnung
def wie_oft_passt(hauptzahl, teiler):
    if teiler == 0:
        return "Teilen durch Null ist nicht erlaubt!"
    
    vielfache = hauptzahl // teiler
    rest = hauptzahl % teiler      
    
    return vielfache, rest

# Funktion für Tausendertrennzeichen
def format_number(num):
    return f"{num:,}".replace(",", ".")

# HTML-Template
html_template = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wolkenkratzer Finanzrechner</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #e0f7fa, #80deea);
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #00796b;
        }
        form {
            margin-bottom: 20px;
        }
        label {
            font-weight: bold;
        }
        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #00796b;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #004d40;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background: #e0f2f1;
            border-left: 5px solid #00796b;
            border-radius: 4px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            margin: 5px 0;
        }
        footer {
            text-align: center;
            margin-top: 20px;
            font-size: 14px;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Wolkenkratzer Finanzrechner</h1>
        <form method="post">
            <label for="networth">Wie viel Geld hast du?</label>
            <input type="number" id="networth" name="networth" placeholder="Gib hier deinen Betrag ein" required>
            <button type="submit">Berechnen</button>
        </form>
        {% if result %}
        <div class="result">
            <h2>Ergebnis</h2>
            <p>Du könntest <strong>{{ result['wieviele'] }}</strong> Wolkenkratzer kaufen.</p>
            <p>Das wird <strong>{{ result['ausgegeben'] }}€</strong> kosten.</p>
            <p>Benötigte Ressourcen:</p>
            <ul>
                <li><strong>Bauherren:</strong> {{ result['bauherren'] }}</li>
                <li><strong>Metall:</strong> {{ result['metall'] }}</li>
                <li><strong>Holz:</strong> {{ result['holz'] }}</li>
                <li><strong>Beton:</strong> {{ result['beton'] }}</li>
            </ul>
            <p>Nach Fertigstellung bekommst du <strong>{{ result['endgeld'] }}€</strong>.</p>
            <p>Insgesamt machst du <strong>{{ result['profit'] }}€</strong> Gewinn.</p>
        </div>
        {% endif %}
        <footer>Wolkenkratzer Finanzrechner © 2024</footer>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            networth = int(request.form["networth"])
            skyscraper = 13655150
            bauherren = 800
            metall = 1450
            holz = 2800
            beton = 190000
            finalmoney = 20482000

            wieviele, rest = wie_oft_passt(networth, skyscraper)
            ausgegeben = wieviele * skyscraper
            endgeld = finalmoney * wieviele
            profit = endgeld - ausgegeben

            result = {
                "wieviele": wieviele,
                "ausgegeben": format_number(ausgegeben),
                "bauherren": format_number(bauherren * wieviele),
                "metall": format_number(metall * wieviele),
                "holz": format_number(holz * wieviele),
                "beton": format_number(beton * wieviele),
                "endgeld": format_number(endgeld),
                "profit": format_number(profit),
            }
        except ValueError:
            result = {"error": "Ungültige Eingabe!"}
    
    return render_template_string(html_template, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
