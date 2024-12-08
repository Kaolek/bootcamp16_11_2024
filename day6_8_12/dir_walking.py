import os

print(os.path.abspath("../main.py"))
# /Users/karolkontek/PycharmProjects/bootcamp16_11_2024/main.py

for root, dirs, files in os.walk("../.."):
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)

    if files:
        print('Files')
        for filname in files:
            print(filname)