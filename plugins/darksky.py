# coding: utf-8

# モジュールのインポート
import requests
import json
from datetime import datetime
from slackbot.bot import respond_to


# Dark Sky APIを呼び出し天気データのjsonを返す関数
def get_data(API_KEY, LATITUDE, LONGITUDE):
    # Dark Sky API
    api = "https://api.darksky.net/forecast/{key}/{latitude},{longitude}?lang=ja"
    # APIのURLを生成
    url = api.format(key=API_KEY, latitude=LATITUDE, longitude=LONGITUDE)
    # 天気予報のjsonデータを取得し, dataに保存
    response = requests.get(url)
    data = json.loads(response.text)
    return data


# 天気データを取得し, 現在の天気情報を返す関数
def get_current_forecast():
    API_KEY = "YOUR KEY"    # Dark SkyのAPIキー
    LATITUDE = "ATTITUDE"   # 天気情報を取得したい位置の緯度経度
    LONGITUDE = "LONGITUDE"

    # 天気予報データの取得
    data = get_data(API_KEY, LATITUDE, LONGITUDE)

    # 取得したデータをそれぞれ変形
    date = datetime.fromtimestamp(data["currently"]["time"])
    summary = data["currently"]["summary"]
    temperature = (data["currently"]["temperature"]-32) * 5/9   # 華氏から摂氏への変換
    humidity = data["currently"]["humidity"]
    windSpeed = data["currently"]["windSpeed"]*1609.344/3600    # mphからm/sへの変換
    precipProbability = data["currently"]["precipProbability"]
    # 天気情報の文字列を作成
    forecast_str = ("{0}時{1}分時点での天気情報です。\n".format(date.hour, date.minute))
    forecast_str += ("現在の天気:{}\n".format(summary))
    forecast_str += ("気温:{:.1f}℃ 湿度:{:.1%} 風速:{:.1f}m/s 降水確率:{:.1%}\n".format(temperature, humidity, windSpeed, precipProbability))
    return forecast_str


# "天気"を含むメッセージが送られた時, 天気情報を返す
@respond_to("天気")
def tenki(message):
    str = get_current_forecast()
    message.send(str)
