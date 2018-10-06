###############################################
# 5章 辞書とデータ構造
# 5.6 演習プロジェクトのプログラム
###############################################

# 引数として与えられた辞書の中身を
# 一覧として表示するプログラム
def display_inventory(inventry):
    print('持ち物リスト：')
    item_total = 0
    count = {}
    for k, v in inventry.items():
        item_total += v
        print(str(v) + ' ' + k)
    print("アイテム総数：" + str(item_total))

#stuff = {'ロープ':1, 'たいまつ':6, '金貨':42, '手裏剣':1, '矢':12}
#display_inventory(stuff)

# 持ち物に取得したアイテムを追加するプログラム
def add_toinventory(inventry, added_items):
    for item in added_items:
        inventry.setdefault(item, 0)
        inventry[item] += 1

    return inventry

inv = {'金貨':42, 'ロープ':1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']

inv = add_toinventory(inv, dragon_loot)
display_inventory(inv)