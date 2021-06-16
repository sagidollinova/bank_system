import requests


def getCurrency():
    response = requests.get(
        'https://free.currconv.com/api/v7/convert?q=USD_KZT&compact=ultra&apiKey=ae1da62bd4cb7ca4ddf8')
    usd_kzt = response.json()['USD_KZT']
    response = requests.get(
        'https://free.currconv.com/api/v7/convert?q=RUB_KZT&compact=ultra&apiKey=ae1da62bd4cb7ca4ddf8')
    rub_kzt = response.json()['RUB_KZT']
    response = requests.get(
        'https://free.currconv.com/api/v7/convert?q=KZT_USD&compact=ultra&apiKey=ae1da62bd4cb7ca4ddf8')
    kzt_usd = response.json()['KZT_USD']
    response = requests.get(
        'https://free.currconv.com/api/v7/convert?q=RUB_USD&compact=ultra&apiKey=ae1da62bd4cb7ca4ddf8')
    rub_usd = response.json()['RUB_USD']
    response = requests.get(
        'https://free.currconv.com/api/v7/convert?q=KZT_RUB&compact=ultra&apiKey=ae1da62bd4cb7ca4ddf8')
    kzt_rub = response.json()['KZT_RUB']
    response = requests.get(
        'https://free.currconv.com/api/v7/convert?q=USD_RUB&compact=ultra&apiKey=ae1da62bd4cb7ca4ddf8')
    usd_rub = response.json()['USD_RUB']
    return usd_kzt, rub_kzt, kzt_usd, kzt_rub, usd_rub, rub_usd
