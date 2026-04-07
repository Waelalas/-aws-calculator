from flask import Flask, render_template_string

application = Flask(__name__)

# واجهة الحاسبة العلمية (HTML + CSS + JS)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>حاسبة علمية متطورة - AWS</title>
    <style>
        body { background-color: #1a1a1a; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: sans-serif; }
        .calculator { background: #333; padding: 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); width: 320px; }
        #display { width: 100%; height: 60px; font-size: 30px; text-align: right; margin-bottom: 20px; padding: 10px; box-sizing: border-box; border: none; background: #222; color: #0f0; border-radius: 10px; }
        .buttons { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
        button { padding: 15px; font-size: 18px; border: none; border-radius: 8px; cursor: pointer; background: #444; color: white; transition: 0.2s; }
        button:hover { background: #555; }
        .operator { background: #ff9500; color: white; }
        .operator:hover { background: #e08400; }
        .special { background: #a5a5a5; color: black; }
        .equal { background: #28a745; grid-column: span 2; }
        .equal:hover { background: #218838; }
    </style>
</head>
<body>
    <div class="calculator">
        <input type="text" id="display" disabled>
        <div class="buttons">
            <button class="special" onclick="clearDisplay()">AC</button>
            <button class="special" onclick="deleteLast()">DEL</button>
            <button class="operator" onclick="appendToDisplay('**')">xʸ</button>
            <button class="operator" onclick="appendToDisplay('/')">÷</button>
            
            <button onclick="appendToDisplay('7')">7</button>
            <button onclick="appendToDisplay('8')">8</button>
            <button onclick="appendToDisplay('9')">9</button>
            <button class="operator" onclick="appendToDisplay('*')">×</button>
            
            <button onclick="appendToDisplay('4')">4</button>
            <button onclick="appendToDisplay('5')">5</button>
            <button onclick="appendToDisplay('6')">6</button>
            <button class="operator" onclick="appendToDisplay('-')">-</button>
            
            <button onclick="appendToDisplay('1')">1</button>
            <button onclick="appendToDisplay('2')">2</button>
            <button onclick="appendToDisplay('3')">3</button>
            <button class="operator" onclick="appendToDisplay('+')">+</button>
            
            <button onclick="appendToDisplay('0')">0</button>
            <button onclick="appendToDisplay('.')">.</button>
            <button class="operator" onclick="calculateRoot()">√</button>
            <button class="operator" onclick="appendToDisplay('%')">%</button>
            
            <button class="equal" onclick="calculateResult()">=</button>
            <button class="special" onclick="appendToDisplay('(')">(</button>
            <button class="special" onclick="appendToDisplay(')')">)</button>
        </div>
    </div>

    <script>
        const display = document.getElementById('display');
        function appendToDisplay(value) { display.value += value; }
        function clearDisplay() { display.value = ''; }
        function deleteLast() { display.value = display.value.slice(0, -1); }
        function calculateResult() {
            try { display.value = eval(display.value.replace('×', '*').replace('÷', '/')); }
            catch { display.value = 'خطأ'; }
        }
        function calculateRoot() {
            try { display.value = Math.sqrt(eval(display.value)); }
            catch { display.value = 'خطأ'; }
        }
    </script>
</body>
</html>
"""

@application.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8000)
