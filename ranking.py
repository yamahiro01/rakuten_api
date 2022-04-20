import requests
import urllib
from pprint import pprint
from common import execute_api
import pandas as pd
import os

# 定数は上部で定義する
RAKUTEN_RANKING_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
APP_ID = "1085281097134386336"


# タスク4
def ranking(genre_id: str):
    '''
    指定したジャンルのランキングを取得
    '''
    # キーワード入力、リクエストパラメーター作成
    params = {
        "genreId": genre_id,
        "format": "json",
        "applicationId": APP_ID
    }
    
    # APIを実行
    res = execute_api(url=RAKUTEN_RANKING_URL, params=params)
    
    
    #　結果を表示
    for obj in res["Items"]:
        print(f'rank: {obj["Item"]["rank"]} / {obj["Item"]["itemName"]}')
    
    return res

if __name__ == "__main__":
    genre_id = input("ジャンルIDを入力してください >>> ")
    ranking(genre_id)