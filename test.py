import pandas as pd
import sys

def main():
    df = pd.read_table('input.txt', sep=':')  # input
    df.columns = ['i', 's']  # カラム名を変換
    df_is = df.iloc[:-1].copy()  # 判定に使用するi, sの行を格納
    df_is['i'] = df_is['i'].astype('int')  # str to int
    m = int(df.iloc[-1]['i'])  # m を取得

    judge = lambda i: 1 if int(m) % int(i) == 0 else 0  # mがiの倍数なら1 not倍数なら0
    df_is['mul'] = df['i'].map(judge)  # lambdaを適用

    sub_df = df_is.loc[df_is['mul'] == 1]  # mがiの倍数のものを取得
    sub_df = sub_df.sort_values('i')  # iでソート
    sub_df = sub_df.reset_index(drop=True)  # 出力しやすいようにインデックスを振り直し

    if len(sub_df) != 0:  # 出力するsがあるかを判定
            for s in sub_df['s']:
                print(s, end='')
    else:  # sがなかった場合、mを出力
        print(m)

if __name__ == '__main__':
    main()