#! python3
# phoneAndEmail.py   - クリップボードから電話番号とメアドを検索する

import pyperclip, re

phone_regex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?                         # 市外局番
                        (\s|-|\.)?                                 # 区切り
                        (\d{3})                                    # 3桁の番号
                        (\s|-|\.)                                 # 区切り
                         (\d{4})                                  # 4桁の番号
                         (\s*(ext|x|ext.)\s*(\d{2, 5}))         # 内線番号
                        
                )''', re.VERBOSE)

# TODO: 電子メールの正規表現を作る

# TODO: クリップボードのテキストを検索する。

# TODO: 検索結果を苦リプボードに張り付ける。
