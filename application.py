from flask import Flask, render_template_string, request
import requests

application = Flask(__name__)

# دالة محسنة لجلب الأسعار مع معالجة الأخطاء
def get_crypto_prices():
    try:
        # استخدام رابط مباشر وبسيط
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin,ripple&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Error fetching prices: {e}")
        return None

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>CryptoLive | منصة العملات الرقمية</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background: #0b0e11; color: white; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .container { background: #1e2329; padding: 2rem; border-radius: 20px; width: 380px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #333; }
        h2 { text-align: center; color: #f3ba2f; }
        .price-card { background: #2b3139; padding: 15px; border-radius: 12px; margin-bottom: 20px; text-align: center; border-left: 5px solid #f3ba2f; }
        input, select { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #444; background: #0b0e11; color: white; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #f3ba2f; border: none; border-radius: 8px; color: #000; font-weight: bold; cursor: pointer; transition: 0.2s; }
        button:hover { background: #ffca42; }
        .result { margin-top: 20px; padding: 15px; background: rgba(243, 186, 47, 0.1); border-radius: 10px; text-align: center; border: 1px solid #f3ba2f; }
        .error-msg { color: #ea3943; text-align: center; font-size: 0.9rem; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>CryptoLive ₿</h2>
        
        {% if not prices %}
            <div class="error-msg">⚠️ عذراً، تعذر جلب الأسعار اللحظية حالياً.</div>
        {% else %}
            <div class="price-card">
                سعر BTC الآن: <span style="color:#f3ba2f; font-weight:bold;">${{ prices['bitcoin']['usd'] }}</span>
            </div>
        {% endif %}

        <form method="POST">
            <input type="number" step="any" name="amount" placeholder="المبلغ بالدولار (USD)" required>
            <select name="crypto">
                <option value="bitcoin">Bitcoin (BTC)</option>
                <option value="ethereum">Ethereum (ETH)</option>
                <option value="binancecoin">BNB</option>
                <option value="ripple">Ripple (XRP)</option>
            </select>
            <button type="submit">تحويل العملة</button>
        </form>

        {% if result %}
        <div class="result">
            <div style="font-size: 0.9rem; color: #848e9c;">الكمية المقدرة:</div>
            <div style="font-size: 1.6rem; color: #f3ba2f; font-weight: bold;">{{ result }} {{ symbol }}</div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@application.route("/", methods=["GET", "POST"])
def index():
    prices = get_crypto_prices()
    result = None
    symbol = ""
    
    if request.method == "POST" and prices:
        try:
            amount = float(request.form.get("amount", 0))
            crypto = request.form.get("crypto")
            rate = prices[crypto]['usd']
            result = round(amount / rate, 6)
            symbol = crypto.upper()
        except:
            result = "خطأ"

    return render_template_string(HTML_CONTENT, prices=prices, result=result, symbol=symbol)

if __name__ == "__main__":
    application.run()

