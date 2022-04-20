import requests
import urllib
from pprint import pprint
from common import execute_api

# 定数は上部で定義する
RAKUTEN_ITEM_SEARCH_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
APP_ID = "1085281097134386336"

# タスク１、２
def search_items(keyword: str):
    '''
    指定したキーワードでAPIを実行して
    結果を表示する
    '''
    # キーワード入力、リクエストパラメーター作成
    params = {
        "keyword": keyword,
        "format": "json",
        "applicationId": APP_ID 
    }
    
    # APIを実行
    res = execute_api(url=RAKUTEN_ITEM_SEARCH_URL, params=params)
    
    #　結果を表示
    for obj in res["Items"]:
        print(f'item_name: {obj["Item"]["itemName"]} / price: {obj["Item"]["itemPrice"]}')
        
    return res

if __name__ == "__main__":
    keyword = input("検索キーワードを入力してください >>> ")
    search_items(keyword)
    