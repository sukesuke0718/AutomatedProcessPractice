######################################
# フォルダ内を表示
######################################
import os

print('指定したフォルダ内を表示します')
path = input('フォルダパスを入れてください ：')

for foldername, subfolders, filenames in os.walk(path):
    print('The current folder is ' + foldername)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + foldername + " : " + subfolder)

    for filename in filenames:
        print('FILE INSIDE' + foldername + ' : ' + filename)

print('')