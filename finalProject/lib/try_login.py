from flask import *
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user, login_required

app = Flask("__main__")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        status = login_check(request.form['account'], request.form['password'])

        if status:
            flash('login')
            # return redirect(url_for('myPage'), account=request.values['account'])
            return redirect(url_for('bookshelf', account=request.form.get('account')))
        else:
            flash('Bad Login')
            
            return redirect(url_for('login'))

    return render_template('index.html')



def login_check(ac, pa):

    try:
        if pa == users[ac]:
            #  實作User類別  
            user = User()  
            #  設置id就是email  
            user.id = ac 
            #  這邊，透過login_user來記錄user_id，如下了解程式碼的login_user說明。  
            login_user(user)  
            #  登入成功，轉址
            return True

    except:
        return False
    
    return False  
  
@app.route('/protected')  
@login_required  
def protected():  
    """  
 在login_user(user)之後，我們就可以透過current_user.id來取得用戶的相關資訊了  
 """   
    #  current_user確實的取得了登錄狀態
    if current_user.is_active:  
        return 'Logged in as: ' + current_user.id + ' Login is_active:True'

@app.route("/hello/<account>")
@login_required
def myPage(account):
    return render_template('myPage.html', account=account)

@app.route("/<account>")
@login_required
def bookshelf(account):
    return render_template('bookshelf.html', account=account) 
  
@app.route('/logout')
def logout():  
    """  
 logout\_user會將所有的相關session資訊給pop掉 
 """ 
    logout_user()  
    return 'Logged out'
