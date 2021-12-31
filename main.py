import requests;
import time;

#global variables

api_key = '<your api key>'
bot_key = '<your bot key>'
chat_id = '<your chat id>'
limit = 59000
time_interval = 5 * 60


def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    paramters = {
        'start': '1',
        'limit': '10'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=paramters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price


def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


def main():
    while True:
        price = get_price()
        print(price)
        if price < limit:
            send_update(chat_id, f"عم اتش البيتكوين عامل :  {price}")
        time.sleep(time_interval)
main()
