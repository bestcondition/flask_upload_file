from collections import deque
from pathlib import Path
from argparse import ArgumentParser

from flask import Flask, request, render_template

app = Flask(__name__)
# 上传路径
upload_folder = Path.home() / 'Downloads'


@app.route('/', methods=['GET'])
def show():
    """首页"""
    return render_template('index.html', file_list=[])


@app.route('/upload_file', methods=['POST'])
def upload_file():
    """接收文件"""
    # 文件名列表
    file_list = deque()
    for file in request.files.getlist('file'):
        # 获取文件名
        filename = file.filename
        target_path = upload_folder / filename
        # 保存文件
        file.save(target_path)
        # 添加绝对路径，用于前端显示
        file_list.append(filename)
    return render_template('index.html', file_list=file_list)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=3502)
    parser.add_argument('--folder', type=str, default=str(upload_folder))

    args = parser.parse_args()
    print(args)
    upload_folder = Path(args.folder)
    # 确保上传路径存在
    upload_folder.mkdir(parents=True, exist_ok=True)

    app.run(host=args.host, port=args.port)
