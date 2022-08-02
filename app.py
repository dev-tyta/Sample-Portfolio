from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
port_db = SQLAlchemy(app)


class UserContact(port_db.Model):
    id = port_db.Column(port_db.Integer, primary_key=True)
    name = port_db.Column(port_db.String(100), nullable=False)
    email = port_db.Column(port_db.String(100), nullable=False)
    message = port_db.Column(port_db.Text, nullable=False)

    def __repr__(self):
        return "Contact " + str(self.id)


# class UserLogin(port_db.Model):
#     id = port_db.Column(port_db.Integer, primary_key=True)
#     email = port_db.Column(port_db.String(100), nullable=False)
#     password = port_db.Column(port_db.String(20), nullable=False)
#
#     def __repr__(self):
#         return "User Login " + str(self.id)
#
#
# class UserRegistration(port_db.Model):
#     id = port_db.Column(port_db.Integer, primary_key=True)
#     first_name = port_db.Column(port_db.String(100))
#     last_name = port_db.Column(port_db.String(100))
#     phone = port_db.Column(port_db.Integer)
#     # gender = db_port.Column(db_port.)
#     email = port_db.Column(port_db.String(100), nullable=False)
#     message = port_db.Column(port_db.Text, nullable=False)
#
#     def __repr__(self):
#         return "Contact " + str(self.id)
#

@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/home/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        user_name = request.form.get("name")
        user_mail = request.form.get("email")
        user_message = request.form.get("message")
        new_user = UserContact(name=user_name, email=user_mail, message=user_message)
        port_db.session.add(new_user)
        port_db.session.commit()
        return redirect('/home')
    return render_template("contact.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    return render_template("registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
