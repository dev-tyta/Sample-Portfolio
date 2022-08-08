from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
port_db = SQLAlchemy(app)


class UserContact(port_db.Model):
    id = port_db.Column(port_db.Integer, primary_key=True)
    name = port_db.Column(port_db.String(100), nullable=False, unique=True)
    email = port_db.Column(port_db.String(100), nullable=False)
    message = port_db.Column(port_db.Text, nullable=False)

    def __repr__(self):
        return "Contact " + str(self.id)


class UserLogin(port_db.Model):
    id = port_db.Column(port_db.Integer, primary_key=True)
    email = port_db.Column(port_db.String(100), nullable=False)
    password = port_db.Column(port_db.String(20), nullable=False)

    def __repr__(self):
        return "User Login " + str(self.id)


class UserRegistration(port_db.Model):
    id = port_db.Column(port_db.Integer, primary_key=True)
    first_name = port_db.Column(port_db.String(100), unique=True, nullable=True)
    last_name = port_db.Column(port_db.String(100), unique=True, nullable=True)
    phone = port_db.Column(port_db.Integer)
    gender = port_db.Column(port_db.String(20), unique=True, nullable=True)
    country = port_db.Column(port_db.String(50), unique=True, nullable=True)
    state = port_db.Column(port_db.String(20), unique=True, nullable=True)
    email = port_db.Column(port_db.String(100), nullable=False)
    password = port_db.Column(port_db.String(30), nullable=False, unique=True)
    con_password = port_db.Column(port_db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return "Contact " + str(self.id)


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/home/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_name = request.form.get("name", type=str)
        user_mail = request.form.get("email")
        user_message = request.form.get("message")
        new_user = UserContact(name=user_name, email=user_mail, message=user_message)
        port_db.session.add(new_user)
        port_db.session.commit()
        return redirect('/home')
    return render_template("contact.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        reg_f_name = request.form.get("f_name")
        reg_l_name = request.form.get("l_name")
        reg_no = request.form.get("phone")
        gender = request.form.get("gender")
        country = request.form.get("country")
        state = request.form.get("state")
        password = request.form.get("password")
        con_password = request.form.get("confirm-password")
        reg_mail = request.form.get("email")
        new_registration = UserRegistration(f_name=reg_f_name, l_name=reg_l_name, phone=reg_no, gender=gender,
                                            country=country, state=state, password=password, con_password=con_password,
                                            email=reg_mail)
        port_db.session.add(new_registration)
        port_db.session.commit()
        return redirect('/login')
    return render_template("registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_mail = request.form.get("email")
        login_pass = request.form.get("password")
        user_login = UserLogin(email=login_mail, password=login_pass)
        port_db.session.add(user_login)
        port_db.session.commit()
        return redirect('/home')
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
