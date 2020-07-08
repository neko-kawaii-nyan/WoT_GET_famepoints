import os
import requests
api_url = 'https://api.worldoftanks.asia/wot/globalmap/eventaccountratings/'
app_id = os.environ['APP_ID'] # ここにWG-APIのIDを入力してもよい
event_id = 'metal_wars' # CWシーズンごとに代わる
front_id = 'metal_wars_bg' # 同上
fields = f'rank%2C+fame_points%2C'

def get_fame_point(rank):
    page = int((rank - 1) / 10) + 1
    index = rank % 10 - 1
    url = f'{api_url}?application_id={app_id}&event_id={event_id}&front_id={front_id}&in_rating=1&fields={fields}&page_no={page}&limit=10'
    res = requests.get(url).json()['data'][index]
    rank = res['rank']
    fame = res['fame_points']
    return rank, fame


for i in [0, 1, 1000, 1179, 1500]: # []内にコンマ区切りで調べたい順位を入れる。
    if i <= 0:
        continue
    try:
        rank, fame = get_fame_point(i)
    except Exception as e:
        print(f'入力:{i}について、Error:{e}')
        continue
    print(f'入力:{i}, 順位:{rank} 名声:{fame}')
    # ↑念のためiとrankを表示。この2つの値が異なっていたら後者を信じてください。
