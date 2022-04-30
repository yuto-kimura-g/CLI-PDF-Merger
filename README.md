# CLI PDF Merger repo

## Overview
以前にWebブラウザで動作するPDF結合ツールをJavaScriptで書いたが，なんかバグってるので，慣れ親しんだPythonで作り直した．今度は正常に動作しているが，代わりに，Pythonが実行できる環境が無いと使えない．

## Usage
1. ```./input/```以下に結合したいPDFファイルを置く
2. PyPDF2モジュールをインストールして，結合処理を実行
```shell
# 以下はWindowsでvenv環境を使う場合
$ python -m venv venv
$ venv/Script/activate
$ pip install -r requirements.txt
$ python main.py -i ./input/ -o ./output/main.pdf
```
3. デフォルトでは```./output/```以下に結合されたファイルが生成されている

## References
- [PyPDF2 repo](https://github.com/py-pdf/PyPDF2)
