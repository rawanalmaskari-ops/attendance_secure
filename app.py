from flask import Flask, render_template, request
import database_safe

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("register.html")  # يفتح صفحة التسجيل مباشرة

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        ok = database_safe.add_user(username, password)

        if not ok:
            return "❌ Invalid username – security vulnerability"
        return "✔ User registered securely!"

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if database_safe.verify_user(username, password):
            return f"✔ Welcome {username} — Login successful!"
        else:
            return "❌ Invalid username or password"

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
