import shutil
import os

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIRS = []
FILTER_FILE_NAME = ['.git', '.vscode', '.gitignore', 'Sync.py']


def _run(source, des_dir, filter_file_name=FILTER_FILE_NAME):
    # 源文件夹，目标文件夹，过滤文件名
    if(os.path.exists(des_dir)):
        shutil.rmtree(des_dir)
        os.mkdir(des_dir)
        
    for dirpath, dirnames, filenames in os.walk(SOURCE_DIR):
        for each_file in filenames:
            for each_filter in filter_file_name:
                if (each_filter in each_file):
                    continue
            path = os.path.join(dirpath, each_file)
            relative_path = path[path.index(
                SOURCE_DIR)+len(SOURCE_DIR)+1:path.rindex('\\')]
            dirs = relative_path.split('\\')
            for i in range(0, len(dirs)):
                now_dir = "/"
                for j in range(0, i+1):
                    now_dir = now_dir+dirs[j]+'/'
                if(not os.path.exists(des_dir+now_dir)):
                    os.mkdir(des_dir+now_dir)
            shutil.copyfile(path, des_dir+'/'+relative_path+'/'+each_file)


if __name__ == "__main__":
    TARGET_DIRS.append("F:\\Sync\\cpp_quiz_note")
    
    for each_dir in TARGET_DIRS:
        _run(SOURCE_DIR, each_dir)
    