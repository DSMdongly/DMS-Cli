import os
import sys

from datetime import datetime
from dms import client, console

if __name__ == '__main__':
    dms_id = os.getenv('DMS_ID')
    dms_pw = os.getenv('DMS_PW')

    dms_access_token = os.getenv('DMS_ACCESS_TOKEN')
    dms_refresh_token = os.getenv('DMS_REFRESH_TOKEN')

    if not (dms_access_token and dms_refresh_token):
        tokens = client.auth(dms_id, dms_pw)

        dms_access_token = tokens['accessToken']
        dms_refresh_token = tokens['refreshToken']

    action = sys.argv[1]

    def mypage():
        console.mypage(dms_access_token)

    def meals():
        now = datetime.now()
        console.meals(now.year, now.month, now.day)

    def applies():
        console.applies(dms_access_token)

    def stay_apply():
        console.stay_apply(dms_access_token)

    def extension_apply():
        console.extension_apply(dms_access_token)

    actions = {
        'mypage': mypage,
        'meals': meals,
        'applies': applies,
        'stay-apply': stay_apply,
        'extension-apply': extension_apply,
    }

    action = actions[action]
    action()
