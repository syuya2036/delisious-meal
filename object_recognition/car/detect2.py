from yolov5 import detect
import requests

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = 'kK1396TPpSv4YIRaM1qGprbuCLztiZoY4q6524ym9VB'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)


labels = detect.run(source="./object_recognition/car/img/2023-12-01-09-38-1701391111")
print(labels)
if "person" in labels:
    send_line_notify("人いたわ")