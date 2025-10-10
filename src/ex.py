from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calcular_imc():
    resultado = ""
    if request.method == "POST":
        try:
            peso = float(request.form["peso"])
            altura = float(request.form["altura"])
            imc = peso / (altura ** 2)

            
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc < 25:
                classificacao = "Peso normal"
            elif imc < 30:
                classificacao = "Sobrepeso"
            else:
                classificacao = "Obesidade"

            resultado = f"<p>Seu IMC é {imc:.2f} - {classificacao}</p>"
        except (ValueError, ZeroDivisionError):
            resultado = "<p>Por favor, insira valores válidos!</p>"

    
    html = f"""
    <h1>Calculadora de IMC</h1>
    <form method="post">
        <label>Peso (kg):</label><br>
        <input type="text" name="peso" required><br><br>
        <label>Altura (m):</label><br>
        <input type="text" name="altura" required><br><br>
        <input type="submit" value="Calcular IMC">
    </form>
    {resultado}
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)
