# 単独モジュールで実行可能なモジュールを追加
# from .hello import hello


# 単独モジュールで実行可能な関数を追加
# def main():
#     hello()


# pipenv run start でも起動
if __name__ == '__main__':
    from .cli import main
    main()

# slackモジュールを作成して、クラス化の練習
