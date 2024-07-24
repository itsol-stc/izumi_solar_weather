# -----------------------------------------------------------------------------
# 会社名: 湘南技術センター株式会社
# 名前: 加藤　悠乃
# 作成日: 2024/7/18
# # -----------------------------------------------------------------------------

# 標準ライブラリ
import datetime as dt

# 外部ライブラリ
import mysql.connector

# DB接続情報
DB_HOST = "133.18.228.30"
DB_USER = "admin"
DB_PASSWORD = "admin"
DB_DATABASE = "mysql"

# テーブル名

def db_init():
    
    """
    db_init 関数

    概要:
        MySQLデータベースに接続し、コネクションとカーソルを取得する。

    引数:
        なし

    戻り値:
        conn (mysql.connector.connection.MySQLConnection): MySQLデータベース接続オブジェクト。
        cursor (mysql.connector.cursor.MySQLCursor): MySQLデータベースカーソルオブジェクト。

    例外処理:
        MySQLデータベースへの接続に失敗した場合は例外が発生する可能性がある。
    """

    # MySQLに接続
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )

    # カーソルを取得
    cursor = conn.cursor()

    # コネクタとカーソルを返す
    return conn,cursor

def db_close(conn,cursor):

    """
    db_close 関数

    概要:
        MySQLデータベースのコネクションとカーソルを閉じる。

    引数:
        conn (mysql.connector.connection.MySQLConnection): MySQLデータベース接続オブジェクト。
        cursor (mysql.connector.cursor.MySQLCursor): MySQLデータベースカーソルオブジェクト。

    戻り値:
        なし

    例外処理:
        なし

    """

    # カーソルを閉じる
    cursor.close()

    # コネクタを閉じる
    conn.close()

def db_weather(prefArea_code,area_code,date_of_forecast,weather_code,report_datetime):
    
    # DBに接続
    my_conn,my_cursor = db_init()

    # 時間別テーブルに対して該当日時の件数を取得
    sql = ''
    sql = f"""
    INSERT
    INTO weather_forecast(
    prefArea_code,
    area_code,
    date_of_forecast,
    weather_code,
    report_datetime
    )
    VALUES ({prefArea_code},{area_code},'{date_of_forecast}',{weather_code},'{report_datetime}');
    """

    # SQLクエリを実行し、結果を取得
    my_cursor.execute(sql)
    # results = my_cursor.fetchall()
    my_conn.commit()

    # # 結果をコンソールに出力
    # print(results)

    # DBの接続を閉じる
    db_close(my_cursor,my_conn)


def db_temp(prefArea_code,area_code,date_of_forecast,temp_min,temp_max,report_datetime):
    
    # DBに接続
    my_conn,my_cursor = db_init()

    # 時間別テーブルに対して該当日時の件数を取得
    sql = ''
    sql = f"""
    INSERT
    INTO temp_forecast(
    prefArea_code,
    area_code,
    date_of_forecast,
    temp_min,
    temp_max,
    report_datetime
    )
    VALUES ({prefArea_code},{area_code},'{date_of_forecast}',{temp_min},{temp_max},'{report_datetime}');
    """

    # SQLクエリを実行し、結果を取得
    my_cursor.execute(sql)
    # results = my_cursor.fetchall()
    my_conn.commit()

    # # 結果をコンソールに出力
    # print(results)

    # DBの接続を閉じる
    db_close(my_cursor,my_conn)