import os
from flask import Flask, flash, request, redirect, url_for, jsonify, render_template, make_response
from werkzeug.utils import secure_filename
import datetime
import random

basepath = os.path.dirname(__file__)
UPLOAD_FOLDER = basepath + "/tmp"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'html'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Pic_str:
    def create_uuid(self): #生成唯一的图片的名称字符串，防止图片显示时的重名问题
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S");  # 生成当前时间
        randomNum = random.randint(0, 100);  # 生成的随机整数n，其中0<=n<=100
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        return uniqueNum

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def upload_test():
    return render_template('upload.html')

@app.route('/up_photo', methods=['POST'], strict_slashes=False)
def api_upload():
    print("HI")
    f = request.files['photo']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]
        new_filename = Pic_str().create_uuid() + '.' + ext
        print(new_filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
        img_url = 'show/'+new_filename
        img_url_new = 'show/'+new_filename  #处理后的图片，假数据

        print(img_url_new)
 
        return jsonify({"success": 200, "msg": "上传成功", "img_url": img_url, "img_url_new": img_url_new})
    else:
        return jsonify({"error": 505, "msg": "上传失败"})
    
# show photo
@app.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(app.config['UPLOAD_FOLDER'], '%s' % filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass
 
if __name__ == '__main__':
    app.run(debug=True)