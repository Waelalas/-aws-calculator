from flask import Flask, render_template, request

application = Flask(__name__)
history = []

@application.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            expression = request.form.get("expression")
            result = eval(expression, {"__builtins__": None}, {})
            history.insert(0, f"{expression} = {result}")
            if len(history) > 5: history.pop()
        except:
            error = "خطأ في العملية"
    return render_template("index.html", result=result, error=error, history=history)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)
