from flask import *
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user, login_required
import os
from hashlib import sha256
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "MINE"
login_manager = LoginManager(app)  

available_filename = []

class User(UserMixin):    
    pass  

@login_manager.user_loader  
def user_loader(id):  

    man = users.find_one({ "id" : id })

    if man == None:  
        return  
  
    user = User()  
    user.id = id  
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
            return redirect(url_for('bookshelf'))
        else:
            flash('Bad Login')
            
            return redirect(url_for('login'))


    return render_template('index_1.html')

client = MongoClient('localhost',username='user',password='pa',authSource='project')

db = client['project']
users = db['users']

def login_check(ac, pa):

    pa_hash = sha256(pa.encode('utf-8')).hexdigest()

    man = users.find_one({ "id": ac })

    if man == None:
        return 1

    if man["password"] == pa_hash: 
        return 0
    else:
        return 2

@app.route("/bookshelf")
@login_required
def bookshelf():

    user = users.find_one({"id" : current_user.id})

    books = db["books"]

    myBooks = user["books"]

    return render_template('myBookCase.html', account=current_user.id, books=myBooks)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        status = registering(request.form['account'], request.form['password'], request.form['check_password'])
        if status == 0:
            flash('register success')
            
            user = User()

            user.id = request.form['account']

            login_user(user)
            
            return redirect(url_for('bookshelf'))
        elif status == 1:
            flash('account already exist')

            return redirect(url_for('register'))
        elif status == 2:
            flash('check is not same as password')

            return redirect(url_for('register'))

    return render_template('index.html')

def registering(ac, pa, ch):

    man = users.find_one({ "id" : ac})

    if man is not None:
        return 1

    if pa != ch:
        return 2

    sha_pa = sha256(pa.encode('utf-8')).hexdigest()

    # users[ac] = sha_pa

    data = {
                "id" : ac,
                "password" : sha_pa,
                "books" : []
            }

    post_id = users.insert_one(data).inserted_id

    print("registed: ", post_id)

    return 0

@app.route("/logout")
@login_required
def logout():
    logout_user() 

    return redirect(url_for("index"))

from flask_login import LoginManager

@app.route("/book/<bookName>")
@login_required
def in_book(bookName):

    user = users.find_one({"id" : current_user.id})

    if bookName not in user["books"]:
        return redirect(url_for("bookshelf"))

    books = db["books"]
    pages = db["pages"]

    theBook = books.find_one({"name" : bookName})

    maxPage = theBook["maxPage"]

    thePages = pages.find({"bookName" : bookName})

    return render_template("in_book.html", bookName=bookName, maxPage=maxPage, thePages = thePages)

@app.route("/book/<bookName>/<number>")
# @app.route("/book/<bookName>/<pageName>")
@login_required
def in_page(bookName, number):

    user = users.find_one({"id" : current_user.id})

    if bookName not in user["books"]:
        return redirect(url_for("bookshelf"))

    books = db["books"]
    pages = db["pages"]

    theBook = books.find_one({"name" : bookName})

    maxPage = theBook["maxPage"]

    thePage = pages.find_one({"bookName" : bookName, "number" : float(number)})

    if thePage == None:
        return redirect(url_for("bookshelf"))

    return render_template("myPage.html", bookName=bookName, pageName=thePage["pageName"], content=thePage["text"])

basepath = os.path.dirname(__file__)
UPLOAD_FOLDER = basepath + "/tmp"
ALLOWED_EXTENSIONS = {'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            user = users.find_one({"id" : current_user.id})

            bookName = request.form['bookName']

            pages = db["pages"]
            books = db["books"]

            if bookName not in user["books"]:

                if books.find_one({ "name" : bookName }) != None:
                    flash("book already exist, but you dont own it!")

                    return redirect(request.url) 
                
                flash("add a new book")

                # "name" : "測試",
                # "maxPage" : 1

                books.insert_one({"name" : bookName, "maxPage" : 0 })

                users.update_one({"id" : current_user.id}, { "$push" : { "books" : bookName } })

            flash("success upload \"" + file.filename + "\"")

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            maxPage = books.find_one({ "name" : bookName })["maxPage"]

            books.update_one({ "name" : bookName}, { "$inc" : { "maxPage" : 1} })

            text = transformTxT(file.filename)

            pageName = file.filename

            pageName = pageName.split(".")[0]

            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            # "bookName" : "測試",
            # "pageName" : "第一頁",
            # "number" : 1,
            # "text" :  ["11月中，台泥集團

            pages.insert_one({ "bookName" : bookName, "pageName" : pageName, "number" : maxPage + 1, "text" : text })

            return redirect(url_for('upload'))

    return render_template("upLoadBook.html")

def transformTxT(filename):

    with open("finalProject/tmp/" + filename, "r") as fp:

        ori = fp.read()

    ori = ori.split("\n")

    return ori

if __name__ == '__main__':
    available_filename = list(range(100))
    app.debug = True
    app.run()
