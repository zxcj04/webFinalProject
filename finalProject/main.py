from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['account'], request.form['password']):
            flash('login')
            # return redirect(url_for('myPage'), account=request.values['account'])
            return redirect(url_for('myPage', account=request.form.get('account')))

    return render_template('index.html')

from hashlib import sha256

accounts = {'admin': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'}

def login_check(ac, pa):

    pa_hash = sha256(pa.encode('utf-8')).hexdigest()

    try:
        accounts[ac]
    except:
        return False

    if accounts[ac] == pa_hash: 
        return True
    else:
        return False

@app.route("/hello/<account>")
def myPage(account):
    return render_template('myPage.html', account=account)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        status = registering(request.form['account'], request.form['password'], request.form['check_password'])
        if status == 0:
            flash('register success')
            # return redirect(url_for('myPage'), account=request.values['account'])
            return redirect(url_for('myPage', account=request.form.get('account')))
        elif status == 1:
            flash('account already exist')

            return redirect(url_for('register'))
        elif status == 2:
            flash('check is not same as password')

            return redirect(url_for('register'))

    return render_template('register.html')

def registering(ac, pa, ch):
    if ac in accounts:
        return 1

    if pa != ch:
        return 2

    sha_pa = sha256(pa.encode('utf-8')).hexdigest()

    accounts[ac] = sha_pa

    return 0

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "MINE"
    app.run()