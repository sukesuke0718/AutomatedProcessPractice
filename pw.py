#! python3
# pw.py -パスワード管理プログラム（脆弱性あり）

PASSWORDS = {'email':'password',
             'blog':'P@ssw0rd',
             'luggage':"wordpass"}

import sys
import pyperclip

# コマンドライン引数の
# 2番目の要素の桁数が2以下なら使い方を表示
if len(sys.argv) < 2:
    print('使い方： python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1]           # 最初のコマンドライン引数がアカウント名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウント名はありません')
