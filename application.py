from flask import Flask, render_template_string, request

application = Flask(__name__)
history = []

# الكود الجديد الجميل مدمج هنا لضمان عدم حدوث خطأ 500
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>حاسبة السحاب المتقدمة</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root { --primary: #6366f1; --bg: #0f172a; }
        body { font-family: 'Tajawal', sans-serif; background: var(--bg); color: white; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); }
        .container { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); padding: 2rem; border-radius: 24px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); border: 1px solid rgba(255, 255, 255, 0.1); width: 350px; }
        h2 { text-align: center; color: var(--primary); }
        input[type="text"] { width: 100%; padding: 1rem; background: rgba(0, 0, 0, 0.2); border: 2px solid rgba(255, 255, 255, 0.1); border-radius: 12px; color: white; font-size: 1.5rem; text-align: left; box-sizing: border-box; margin-bottom: 10px; }
        button { width: 100%; padding: 1rem; background: var(--primary); border: none; border-radius: 12px; color: white; font-weight: bold; cursor: pointer; }
        .result-box { margin-top: 1.5rem; padding: 1rem; background: rgba(16, 185, 129, 0.1); border-radius: 12px; text-align: center; border: 1px solid #10b981; }
        .history { margin-top: 2rem; font-size: 0.8rem; color: #94a3b8; }
    </style>
</head>
<body>
    <div class="container">
        <h2>حاسبة السحاب 🚀</h2>
        <form method="POST">
            <input type="text" name="expression" placeholder="مثال: 10 * 5" required>
            <button type="submit">احسب</button>
        </form>
        {% if result is not none %}<div class="result-box"><small>النتيجة:</small><div style="font-size: 2rem;">{{ result }}</div></div>{% endif %}
        <div class="history">
            <strong>السجل:</strong>
            {% for item in history %}<div style="border-bottom: 1px solid #334155; padding: 5px 0;">{{ item }}</div>{% endfor %}
        </div>
    </div>
</body>
</html>
"""

@application.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            expression = request.form.get("expression")
            result = eval(expression, {"__builtins__": None}, {})
            history.insert(0, f"{expression} = {result}")
            if len(history) > 3: history.pop()
        except: result = "خطأ"
    return render_template_string(HTML_CONTENT, result=result, history=history)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)
