import os

import requests


def lambda_handler(event, context):
    # LINE Notifyで取得したアクセストークン
    # 環境変数LINE_NOTIFY_ACCESS_TOKENから取得
    access_token = os.environ.get('LINE_NOTIFY_ACCESS_TOKEN')
    # 送信するメッセージ
    message = 'hello, world'
    # LINE Notifyの通知系APIのエンドポイント
    url = 'https://notify-api.line.me/api/notify'
    # リクエストヘッダー
    headers = {'Authorization':	f'Bearer {access_token}'}
    # リクエストパラメータ
    data = {'message': message}
    # POSTリクエストをエンドポイントに送信
    response = requests.post(url=url, headers=headers, data=data)
    # HTTPレスポンス
    return response.json()
