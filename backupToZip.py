#! python3
# backupToZip.py - フォルダ全体を連番付きZIPファイルにコピーする
import zipfile, os

def backup_to_zip(folder):
    # フォルダ全体をZIPファイルにバックアップする

    folder = os.path.abspath(folder)        # folderを絶対パスにする

    # 既存のファイル名からファイル名の連番を決める
    number = 1
    while True:
        # 新しくつけるファイルの名前
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        # ファイルが見つからなかったらループを抜ける
        if not os.path.exists(zip_filename):
            break
        number = number + 1

    # ZIPファイルを作成する
    print('Creating {} ...'.format(zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, 'w')         # 書き込みモード

    # フォルダーのツリーを渡り歩いてその中のファイルを圧縮する
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in {} ...'.format(foldername))
        # 現在のフォルダをZIPファイルに追加する
        backup_zip.write(foldername)
        # 現在のフォルダの中の全ファイルをZIPファイルに追加する
        for filename in filenames:
            new_base = os.path.basename(foldername) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue    # バックアップ用ZIPファイルはバックアップしない
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()

    print('Done.')

# バックアップ処理を実行
backup_to_zip(r'')