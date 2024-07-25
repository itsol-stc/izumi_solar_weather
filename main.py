# -----------------------------------------------------------------------------
# 会社名: 湘南技術センター株式会社
# 名前: 加藤　悠乃
# 作成日: 2024/7/18
# # -----------------------------------------------------------------------------

import requests
from datetime import datetime, timedelta
import mysql_ops as mysql

# URL設定
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/140000.json"
# 天気情報の取得
data = requests.get(url).json()

def date_serialize(date_string):
    """
    date_serialize 関数

    概要:
        
    引数:
        date_string：変更したいISO 8601形式の日時文字列

    戻り値:
        formatted_date：変更後の日付文字列

    例外処理:
        なし

    """
    # ISO 8601形式の日時文字列をdatetimeオブジェクトに変換する
    dt = datetime.fromisoformat(date_string)
    
    # 1日後の同じ時刻を計算
    dt_new = dt + timedelta(hours=9)
    
    # 新しい日時を指定のフォーマットに整形する
    formatted_date = dt_new.strftime("%Y/%m/%d %H:%M:%S")
    
    return formatted_date

# 変数
prefArea_code = 140000
prefArea_officeName = data[0]["publishingOffice"]
area_code = data[0]["timeSeries"][0]["areas"][0]["area"]["code"]
area_name = data[0]["timeSeries"][0]["areas"][0]["area"]["name"]
weather_forecast_time = data[0]["timeSeries"][0]["timeDefines"]
weather_code = data[0]["timeSeries"][0]["areas"][0]["weatherCodes"]
weather_explanation = data[0]["timeSeries"][0]["areas"][0]["weathers"]
temp_forecast_time = data[0]["timeSeries"][2]["timeDefines"]
temp_forecast_time_today = date_serialize(temp_forecast_time[0])
temp_forecast_time_tommorow = date_serialize(temp_forecast_time[2])
temp= data[0]["timeSeries"][2]["areas"][0]["temps"]

print("-----------------------------------------------------")

report_time = datetime.now()

# 天気情報の表示
prefArea_officeName = data[0]["publishingOffice"]
print("観測場所："+prefArea_officeName)

print(area_name)
print(area_code)


for i, date in enumerate(weather_forecast_time):
    new_date = date_serialize(date)
    mysql.db_weather(prefArea_code,area_code,new_date,weather_code[i],report_time)
    # print(new_date + "："+ "天気コード" + weather_code[i]  +" : "+ weather_explanation[i] )


# 1日目の気温をセット
mysql.db_temp(prefArea_code,area_code,temp_forecast_time_today,temp[0],temp[1],report_time)

# print(temp_forecast_time_today)
# print("最低気温" + temp[0])
# print("最高気温" + temp[1])


# 2日目の気温をセット
mysql.db_temp(prefArea_code,area_code,temp_forecast_time_tommorow,temp[2],temp[3],report_time)

# print(temp_forecast_time_tommorow)
# print("最低気温" + temp[2])
# print("最高気温" + temp[3])
