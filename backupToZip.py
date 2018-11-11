#! python3
# backupToZip.py - フォルダ全体を連番付きZIPファイルにコピーする
import zipfile, os

def backup_to_zip(folder):
    # フォルダ全体をZIPファイルにバックアップする

    folder = os.path.abspath(folder)        # folderを絶対パスにする

    # 既存のファイル名からファイル名の連番を決める
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1

    # TODO: ZIPファイルを作成する

    # TODO; フォルダーのツリーを渡り歩いてその中のファイルを圧縮する
    print('Done.')


backup_to_zip(r'')