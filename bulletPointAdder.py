#! python3
# bulletPointAdder.py -クリップボードのテキスト各行に点を打って、Wikipediaの箇条書きにする
# 引数として文字を指定する

import sys
import pyperclip

if len(sys.argv) < 2:
    print('引数を入れてください')
    sys.exit()

dotStyle = sys.argv[1]
text = pyperclip.paste()

# 行を分割して、”*”を追加する
lines = text.split('\n')
for i in range(len(lines)):         # 要素の数だけループ
    lines[i] = str(dotStyle) + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
