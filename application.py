from flask import Flask, render_template_string, request

application = Flask(__name__)
history = []

# تصميم عصري بألوان متناسقة وتأثيرات زجاجية احترافية
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>حاسبة السحاب الاحترافية</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Cairo', sans-serif;
            background: #0f172a;
            background: radial-gradient(circle at top right, #1e1b4b, #0f172a);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            color: white;
        }
        .calculator-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 2.5rem;
            border-radius: 30px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            width: 380px;
            transition: all 0.3s ease;
        }
        h2 { text-align: center; margin-bottom: 2rem; color: #818cf8; font-weight: 700; }
        
        .input-group { position: relative; margin-bottom: 1.5rem; }
        
        input[type="text"] {
            width: 100%;
            padding: 1.2rem;
            background: rgba(15, 23, 42, 0.6);
            border: 2px solid #334155;
            border-radius: 15px;
            color: #f8fafc;
            font-size: 1.8rem;
            text-align: center;
            outline: none;
            transition: border-color 0.3s;
            box-sizing: border-box;
        }
        input[type="text"]:focus { border-color: #818cf8; box-shadow: 0 0 15px rgba(129, 140, 248, 0.3); }

        button {
            width: 100%;
            padding: 1rem;
            background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
            border: none;
            border-radius: 15px;
            color: white;
            font-size: 1.2rem;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.4);
            transition: transform 0.2s, hover 0.3s;
        }
        button:hover { background: linear-gradient(135deg, #818cf8 0%, #6366f1 100%); transform: translateY(-2px); }
        button:active { transform: translateY(0); }

        .result-display {
            margin-top: 2rem;
            padding: 1.5rem;
            background: rgba(16, 185, 129, 0.1);
            border: 1px dashed #10b981;
            border-radius: 20px;
            text-align: center;
            animation: fadeIn 0.5s ease-out;
        }
        .result-value { font-size: 2.5rem; color: #34d399; font-weight: 700; }
        
        .history-section {
            margin-top: 2.5rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            padding-top: 1rem;
        }
        .history-title { color: #94a3b8; font-size: 0.9rem; margin-bottom: 10px; display: block; }
        .history-item {
            background: rgba(255, 255, 255, 0.03);
            margin-bottom: 8px;
            padding: 8px 15px;
            border-radius: 10px;
            font-size: 0.85rem;
            color: #cbd5e1;
            display: flex;
            justify-content: space-between;
        }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div class="calculator-card">
        <h2>حاسبة السحاب 💎</h2>
        <form method="POST">
            <div class="input-group">
                <input type="text" name="expression" placeholder="0" autocomplete="off" required>
            </div>
            <button type="submit">احسب النتيجة</button>
        </form>

        {% if result is not none %}
        <div class="result-display">
            <span style="color: #94a3b8; font-size: 0.9rem;">النتيجة النهائية</span>
            <div class="result-value">{{ result }}</div>
        </div>
        {% endif %}

        {% if history %}
        <div class="history-section">
            <span class="history-title">آخر العمليات:</span>
            {% for item in history %}
            <div class="history-item">
                <span>{{ item.split('=')[0] }}</span>
                <span style="color: #818cf8;">= {{ item.split('=')[1] }}</span>
            </div>
            {% endfor %}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@application.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            expr = request.form.get("expression")
            # حماية بسيطة وتنفيذ العملية
            result = eval(expr, {"__builtins__": None}, {})
            history.insert(0, f"{expr} = {result}")
            if len(history) > 4: history.pop()
        except:
            result = "خطأ!"
    return render_template_string(HTML_CONTENT, result=result, history=history)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)
