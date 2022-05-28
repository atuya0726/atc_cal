import datetime,re
import googleapiclient.discovery
import google.auth

def api(time):
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    calendar_id = 'atuya07261008@gmail.com'
    # Googleの認証情報をファイルから読み込む
    gapi_creds = google.auth.load_credentials_from_file('atccal-789fa58ba112.json', SCOPES)[0]
    # APIと対話するためのResourceオブジェクトを構築する
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=gapi_creds)


    # ②予定を書き込む
    # 書き込む予定情報を用意する
    body = {
        # 予定のタイトル
        'summary': 'ABC',
        # 予定の開始時刻
        'start': {
            'dateTime': datetime.datetime(time[0], time[1], time[2], time[3], time[4]).isoformat(),
            'timeZone': 'Japan'
        },
        # 予定の終了時刻
        'end': {
            'dateTime': datetime.datetime(time[0], time[1], time[2], time[3] + 1, time[4] + 30).isoformat(),
            'timeZone': 'Japan'
        },
    }
    # 用意した予定を登録する
    event = service.events().insert(calendarId=calendar_id, body=body).execute()