from flask import Flask, render_template, request, flash
from flask_login import current_user, login_user, login_manager, logout_user
import secrets
from postgres.accountsQ import AccountDBConnection

app = Flask(__name__)

secret = secrets.token_urlsafe(32)
app.secret_key = secret

login_manager = login_manager.LoginManager()
login_manager.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get/login")
def getLogin():
    return render_template("login.html", login=True)

@app.route("/get/signup")
def getSignup():
    return render_template("login.html", login=False)


@app.route('/login', methods=['POST'])
def login():
    email = request.form['userEmail']
    psswd = request.form['userPsswd']
    user = get_user_by_email(email)
    
    if user is not None:
        login_user(user, psswd)

        flash('Nice! You are now logged in', 'success')
        return home()
    else:  
        flash('Sorry, Your credentials are wrong !', 'error')
        return getLogin()
    

@app.route('/unlogin', methods=['POST', 'GET'])
def unLogin():
    logout_user()
    return home()


@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['userEmail']
    psswd = request.form['userPsswd']
    user = get_user_by_email(email)
    
    if user is not None:
        flash("Email déja utilisé !", 'error')
    else:
        postgres = AccountDBConnection()
        postgres.AddUser(email, psswd)
        user = get_user_by_email(email)
        login_user(user)
        flash("Compte créé !", 'success')
    return home()
   

@app.route('/update', methods=['POST'])
def update():
    oldEmail = request.form['oldUserEmail']
    newEmail = request.form['newUserEmail']
    postgres = AccountDBConnection()
    try:
        postgres.UpdateEmail(oldEmail, newEmail)
        return "Email mis à jour!"
    except BaseException as b:
        return str(b)

@login_manager.user_loader
def load_user(id):
    postgres = AccountDBConnection()
    user = postgres.LoadUser(id)
    return user
    
def get_user_by_email(email):
    postgres = AccountDBConnection()
    user = postgres.GetUserByPseudo(email)
    return user

if __name__ == "__main__":
    app.run(debug=True)