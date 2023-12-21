# delisious-meal

社会実装演習という科目の共同開発用リポジトリです。

## ドキュメント

- [システム設計書](./docs/%E3%83%81%E3%83%BC%E3%83%A06_%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E8%A8%AD%E8%A8%88%E6%9B%B8.md)


### 1. venvの作成
'''
$ python -m venv venv
'''

### 2. venvのactivate
'''
$ source venv/bin/activate
'''

### 3. パッケージインストール
'''
$ pip install -r requirements.txt 
'''

### 4. yolo インストール
object_recognition/carにyolov5をクローンして下さい．
'''zsh
$ cd object_recognition/car
'''


'''
$ git clone https://github.com/ultralytics/yolov5
'''

### 5. detect.pyの置換
yolov5の中のdetect.pyをルートフォルダにあるdetect.pyに置き換えて下さい．

### 6. 実行ファイルはルートフォルダのremote.pyです．

### 7. ドローンの接続を確立しないと実行できません．(画像解析だけ行いたい場合は，yolov5を実行するだけでいいです)