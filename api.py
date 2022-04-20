import requests
import urllib


def get_api(url, params: dict):
    result = requests.get(url, params=params)
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706" #エンドポイント
    
    # パラメータを記述
    params = {
        "format": "json",
        "keyword": keyword,
        "applicationId": "1085281097134386336",
        "minPrice": 111
    }
    
    print(get_api(url, params=params))


main()