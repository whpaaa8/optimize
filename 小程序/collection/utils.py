import os
import datetime

from django.conf import settings


# 将文件下载到本地, 下载到不同文件夹并命名
def handle_uploaded_file(files, file_type, data):
    # 没有上传文件就跳过
    if len(files) == 0:
        return
    # 设置目录
    directory = os.path.join(settings.MEDIA_ROOT, data['jobNumber'], file_type)
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("目录：{}已存在".format(directory))
    index = 1
    all_names = ""
    # 获取当前时间
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H.%M.%S")
    directory = os.path.normpath(directory)
    for f in files:
        ext = f.name.split('.')[-1]
        filename = data['submitter'] + '_' + now_str + '_' + str(index) + '.' + ext
        index += 1
        path = directory + '/' + filename
        # print(path)
        with open(path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        all_names += filename + ';'
    return all_names


# 下载不同类型文件
def upload_filelist(files_list, data):
    paths = {}
    for file_type, files in files_list.items():
        path = handle_uploaded_file(files, file_type, data)
        paths[file_type] = path
    return paths