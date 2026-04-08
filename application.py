from flask import Flask, render_template_string, request
import requests

application = Flask(__name__)

# دالة لجلب الأسعار الحقيقية من CoinGecko
def get_crypto_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin,ripple,cardano&vs_currencies=usd"
        response = requests.get(url, timeout=5)
        return response.json()
    except:
        return None

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CryptoLive | محول العملات الرقمية</title>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'IBM Plex Sans Arabic', sans-serif; background: #050505; color: white; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .card { background: linear-gradient(145deg, #111, #1a1a1a); padding: 2.5rem; border-radius: 30px; border: 1px solid #333; width: 400px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); }
        h2 { text-align: center; color: #f3ba2f; margin-bottom: 2rem; }
        .price-badge { background: #222; padding: 10px; border-radius: 12px; margin-bottom: 20px; text-align: center; border: 1px solid #444; }
        .btc-price { color: #f3ba2f; font-weight: bold; font-size: 1.2rem; }
        input, select { width: 100%; padding: 12px; margin: 10px 0; border-radius: 10px; border: 1px solid #444; background: #000; color: white; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #f3ba2f; border: none; border-radius: 10px; color: black; font-weight: bold; cursor: pointer; margin-top: 10px; transition: 0.3s; }
        button:hover { background: #ffca42; transform: translateY(-2px); }
        .result { margin-top: 20px; padding: 15px; background: rgba(243, 186, 47, 0.1); border-radius: 10px; text-align: center; border: 1px solid #f3ba2f; }
    </style>
</head>
<body>
    <div class="card">
        <h2>CryptoLive ₿</h2>
        
        <div class="price-badge">
            سعر البيتكوين الآن: <span class="btc-price">${{ btc_usd }}</span>
        </div>

        <form method="POST">
            <label>المبلغ (USD):</label>
            <input type="number" step="any" name="amount" placeholder="أدخل المبلغ بالدولار" required>
            
            <label>حول إلى:</label>
            <select name="crypto">
                <option value="bitcoin">Bitcoin (BTC)</option>
                <option value="ethereum">Ethereum (ETH)</option>
                <option value="binancecoin">BNB</option>
                <option value="ripple">Ripple (XRP)</option>
            </select>
            
            <button type="submit">تحويل الآن</button>
        </form>

        {% if result %}
        <div class="result">
            <div>تحصل على تقريباً:</div>
            <div style="font-size: 1.8rem; color: #f3ba2f; font-weight: bold;">{{ result }} {{ symbol }}</div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@application.route("/", methods=["GET", "POST"])
def index():
    prices = get_crypto_prices()
    btc_usd = prices['bitcoin']['usd'] if prices else "جاري التحميل..."
    
    result = None
    symbol = ""
    
    if request.method == "POST" and prices:
        amount = float(request.form.get("amount", 0))
        crypto = request.form.get("crypto")
        crypto_price = prices[crypto]['usd']
        
        result = round(amount / crypto_price, 6)
        symbol = crypto.upper()

    return render_template_string(HTML_CONTENT, btc_usd=btc_usd, result=result, symbol=symbol)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)
