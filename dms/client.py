import requests
from dms import BASE_PATH


def request(target_method, url_endpoint, json_body=None, token=None, *args, **kwargs):
    authorization = f'JWT {token}' if token else None

    return target_method(
        BASE_PATH + url_endpoint,
        json=json_body,
        headers={
            'Authorization': authorization
        },

        *args, **kwargs
    )


def auth(id, password):
    resp = request(requests.post, '/student/auth', {'id': id, 'password': password})
    return resp.json() if resp.status_code == 201 else None


def mypage(access_token):
    resp = request(requests.get, '/student/info/mypage', token=access_token)
    return resp.json() if resp.status_code == 200 else None


def meal(year, month, day):
    resp = request(requests.get, f'/meal/{year}-{month:0>2}-{day:0>2}')
    return resp.json() if resp.status_code == 200 else None


def applies(access_token):
    resp = request(requests.get, '/student/info/apply', token=access_token)
    return resp.json() if resp.status_code == 200 else None


def stay_apply(stay_value, access_token):
    resp = request(requests.post,
                   '/student/apply/stay', {
                       'value': stay_value
                   }, token=access_token)

    return resp.status_code == 201


def extension_map(extension_time, class_num, access_token):
    resp = request(requests.get, f'/student/apply/extension/{extension_time}/map',
                   params={'classNum': class_num}, token=access_token)

    return resp.json() if resp.status_code == 200 else None


def extension_apply(extension_time, class_num, seat_num, access_token):
    resp = request(requests.post, f'/student/apply/extension/{extension_time}',
                   {'classNum': class_num, 'seatNum': seat_num},
                   token=access_token)

    return resp.status_code == 201
