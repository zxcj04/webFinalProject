from flask import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if login_check(request.form['account'], request.form['password']):
            flash('login')
            # return redirect(url_for('myPage'), account=request.values['account'])
            return redirect(url_for('myPage', account=request.form.get('account')))

    return render_template('index.html')

from hashlib import sha256

def login_check(ac, pa):

    pa_hash = sha256(pa.encode('utf-8')).hexdigest()

    accounts = {'admin': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'}

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

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "MINE"
    app.run()