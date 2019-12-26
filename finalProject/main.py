from flask import *
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user, login_required
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)  
app.secret_key = 'Your Key'  
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


    return render_template('index.html')

from hashlib import sha256

# users = {'admin': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'}

from pymongo import MongoClient
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

    return render_template('bookshelf.html', account=current_user.id, books=myBooks)

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

    return render_template('register.html')

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

    return render_template("in_page.html", bookName=bookName, pageName=thePage["pageName"], content=thePage["text"])

basepath = os.path.dirname(__file__)
UPLOAD_FOLDER = basepath + "/tmp"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'html'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
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
            flash("success upload \"" + file.filename + "\"")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            

            return redirect(url_for('upload_file'))

    return render_template("upload.html")

def transformTxT(filename):

    with open("tmp/" + filename, "r") as fp:

        ori = fp.readlines()

    print(ori)

    first = "\""
    replacement = "\", \""
    last = "\""

    ori = replacement.join(ori)

    ori = first + ori.replace("\n", "") + last

    ori = ori.replace("\"\", ", "")

    return ori

if __name__ == '__main__':
    available_filename = list(range(100))
    app.debug = True
    app.secret_key = "MINE"
    app.run()
