from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# 画像ファイルの拡張子
IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def is_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMAGE_EXTENSIONS

@app.route('/')
@app.route('/<path:req_path>')
def dir_listing(req_path=''):
    base_dir = '/Users/koyo/git/delicious_meal/object_recognition/car/yolov5/runs/detect'  # 閲覧するディレクトリのベースパス

    # 完全なファイルパスを取得
    abs_path = os.path.join(base_dir, req_path)

    if os.path.exists(abs_path):
        files = []
        directories = []
        with os.scandir(abs_path) as it:
            for entry in it:
                if entry.is_file() and is_image(entry.name):
                    files.append(entry.name)
                elif entry.is_dir():
                    directories.append(entry.name)
    else:
        files = []
        directories = []

    return render_template('directory_listing.html', files=files, directories=directories, req_path=req_path)

@app.route('/file/<path:filename>')
def file(filename):
    base_dir = '/Users/koyo/git/delicious_meal/object_recognition/car/yolov5/runs/detect'  # 閲覧するディレクトリのベースパス
    return send_from_directory(base_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
