from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>مرحبا بك في مشروعي الأول!</h1><p>Flask يعمل بنجاح 🚀</p>"

if __name__ == "__main__":
    app.run(debug=True)
