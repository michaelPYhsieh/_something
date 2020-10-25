import os
import random
import string
from pprint import pprint

folder = '_wa'
old_pre = '舊的'
doc_names = 'docnamelist.txt'


# 建立工作資料夾
if not os.path.isdir(folder):
    os.mkdir(folder)


def get_random_string(length):
    # https://pynative.com/python-generate-random-string/
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# 生隨機檔案F
for i in range(1, 5):
    with open(os.path.join(folder, f'{old_pre}{str(i)}{get_random_string(5)}.docx'), mode='a', encoding='utf-8', errors='ignore') as f:
        f.write('')


# 抓取舊的黨名
old_filenames = os.listdir(folder)
# pprint(old_filenames)


# 產生相同數量的新黨名
new_filenames = [f'測試{str(i)}.docx' for i in range(1, len(old_filenames)+1)]
# pprint(new_filenames)


# 清空檔名檔案
with open(doc_names, mode='w', encoding='utf-8', errors='ignore') as f:
    f.write('')


# 生出的新檔名寫入檔案
for fn in new_filenames:
    with open(doc_names, mode='a', encoding='utf-8', errors='ignore') as f:
        f.write(fn+'\n')


# 讀取 doc_names
with open(doc_names, mode='r', encoding='utf-8', errors='ignore') as f:
    tmp = f.read()
new_filenames = tmp[:-1].split('\n')
# pprint(new_filenames)


# 檢查既有檔名 及 要改的 doc_names
exist, err = set(old_filenames), False
for fn in new_filenames:
    if fn in exist:
        err = True
        print(f'！ 要改的檔名 \"{fn}\" 已經存在了啦')


# 改名
if not err:
    for old, new in zip(old_filenames, new_filenames):
        # 顯示對應
        print(f'{old} -> {new}')
        if old and new:
            os.rename(os.path.join(folder, old),
                      os.path.join(folder, new))
