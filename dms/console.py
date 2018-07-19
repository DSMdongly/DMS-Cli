from dms import client
from dms import EXTENSION_TIMES, EXTENSTION_CLASSES, STAY_VALUES


def mypage(access_token):
    info = client.mypage(access_token)

    print(f'이름: {info["name"]}')
    print(f'학번: {info["number"]}')
    print(f'상점: {info["goodPoint"]}')
    print(f'벌점: {info["badPoint"]}')


def meal(menus):
    return ", ".join(menus) or "급식이 없습니다."


def meals(year, month, day):
    today_meals = client.meal(year, month, day)

    print(f'[조식] {meal(today_meals ["breakfast"])}')
    print(f'[중식] {meal(today_meals ["lunch"])}')
    print(f'[석식] {meal(today_meals ["dinner"])}')


def applies(access_token):
    my_applies = client.applies(access_token)
    extension_11 = my_applies["extension11"]
    extension_12 = my_applies["extension12"]
    stay = my_applies["stay"]

    print(f'11시 연장신청: {EXTENSTION_CLASSES[extension_11["classNum"]] if extension_11 else "미신청"}')
    print(f'12시 연장신청: {EXTENSTION_CLASSES[extension_12["classNum"]] if extension_12 else "미신청"}')
    print(f'주말 잔류신청: {STAY_VALUES[stay if stay else "미신청"]}')


def stay_values():
    for val, desc in STAY_VALUES.items():
        print(f'{val}. {desc}')


def stay_apply(access_token):
    stay_values()
    stay_value = int(input('값을 입력하세요\t'))

    result = client.stay_apply(stay_value, access_token)
    print(f'잔류신청 {"성공" if result else "실패"}')


def extension_times():
    for time, desc in EXTENSION_TIMES.items():
        print(f'{time}. {desc}')


def extension_classes():
    for num, desc in EXTENSTION_CLASSES.items():
        print(f'{num}. {desc}')


def extension_map(map_data):
    for row in map_data:
        print(" ".join([f'{e: >4}' for e in row]))


def extension_apply(access_token):
    extension_times()
    extension_time = int(input('신청 시간을 선택해주세요:\t'))

    extension_classes()
    class_num = int(input('신청 교실을 선택해주세요:\t'))

    extension_map(client.extension_map(extension_time, class_num, access_token))
    seat_num = int(input('좌석을 선택해주세요:\t'))

    result = client.extension_apply(extension_time, class_num, seat_num, access_token)
    print(f'연장신청 {"성공" if result else "실패"}')
