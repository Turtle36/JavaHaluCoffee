from flask import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/about/profile/")
def profile():
    return render_template("profile_processor.html")


@app.route("/products/")
def products():
    return render_template("produk_kopi.html")


if __name__ == "__main__":
    app.run()
