import requests
import urllib
from pprint import pprint

from common import execute_api

# 定数は上部で定義する
RAKUTEN_PRODUCT_URL = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
APP_ID = "1085281097134386336"

# タスク3
def item_info(keyword: str):
    '''
    指定したキーワードでAPIを実行して
    商品情報のうち、最高価格と最低価格を取得する
    '''
    # キーワード入力、リクエストパラメーター作成
    params = {
        "keyword": keyword,
        "format": "json",
        "applicationId": APP_ID
    }
    
    # APIを実行
    res = execute_api(url=RAKUTEN_PRODUCT_URL, params=params)
    
    #　結果を表示
    for obj in res["Products"]:
        print(f'product_name: {obj["Product"]["productName"]} / max_price: {obj["Product"]["maxPrice"]} / min_price: {obj["Product"]["minPrice"]}')
    
    return res

if __name__ == "__main__":
    keyword = input("検索キーワードを入力してください >>> ")
    item_info(keyword)