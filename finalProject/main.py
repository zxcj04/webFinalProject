from flask import *
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user, login_required

app = Flask(__name__)  
app.secret_key = 'Your Key'  
login_manager = LoginManager(app)  

class User(UserMixin):  
    """  
 設置一： 只是假裝一下，所以單純的繼承一下而以 如果我們希望可以做更多判斷，
 如is_administrator也可以從這邊來加入 
 """
    
    pass  

@login_manager.user_loader  
def user_loader(email):  
    """  
 設置二： 透過這邊的設置讓flask_login可以隨時取到目前的使用者id   
 :param email:官網此例將email當id使用，賦值給予user.id    
 """   
    if email not in users:  
        return  
  
    user = User()  
    user.id = email  
    return user  

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('bookshelf'))

    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('bookshelf'))
    
    if request.method == 'POST':
        status = login_check(request.form['account'], request.form['password'])

        if status == 0:

            user = User()

            user.id = request.form['account']

            login_user(user)

            # flash('login')
            # return redirect(url_for('myPage'), account=request.values['account'])
            return redirect(url_for('bookshelf'))
        else:
            flash('Bad Login')
            
            return redirect(url_for('login'))


    return render_template('index.html')

from hashlib import sha256

users = {'admin': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'}

def login_check(ac, pa):

    pa_hash = sha256(pa.encode('utf-8')).hexdigest()

    try:
        users[ac]
    except:
        return 1

    if users[ac] == pa_hash: 
        return 0
    else:
        return 2

@app.route("/bookshelf")
@login_required
def bookshelf():
    return render_template('bookshelf.html', account=current_user.id)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        status = registering(request.form['account'], request.form['password'], request.form['check_password'])
        if status == 0:
            flash('register success')
            
            user = User()

            user.id = request.form['account']

            login_user(user)
            # return redirect(url_for('myPage'), account=request.values['account'])
            return redirect(url_for('bookshelf'))
        elif status == 1:
            flash('account already exist')

            return redirect(url_for('register'))
        elif status == 2:
            flash('check is not same as password')

            return redirect(url_for('register'))

    return render_template('register.html')

def registering(ac, pa, ch):
    if ac in users:
        return 1

    if pa != ch:
        return 2

    sha_pa = sha256(pa.encode('utf-8')).hexdigest()

    users[ac] = sha_pa

    return 0

@app.route("/logout")
@login_required
def logout():
    logout_user() 

    return redirect(url_for("index"))

from flask_login import LoginManager

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "MINE"
    app.run()