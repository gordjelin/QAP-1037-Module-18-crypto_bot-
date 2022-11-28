import requests
import json
from config import coins


class Coin:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_mark = coins[base]
        except KeyError:
            raise APIException(f'Валюта/монета <{base}> не поддерживается ботом.\n\n\
💹 Список доступных валют можно посмотреть с помощью команды: /values')
        try:
            quote_mark = coins[quote]
        except KeyError:
            raise APIException(f'Валюта <{quote}> не поддерживается.\n\n\
💹 Список доступных валют/монет можно посмотреть с помощью команды: /values')
        try:
            int_amount = int(amount)
            if int_amount <= 0:
                raise APIException('Необходимое количество не может быть меньше или равно нулю.')
        except ValueError:
            raise APIException('Необходимое количество должно быть целым числом')
        url = 'https://min-api.cryptocompare.com/data/price'
        params = {'fsym': base_mark, 'tsyms': quote_mark}
        data = json.loads(requests.get(url, params=params).content)
        return f'Cтоимость {int_amount} {base_mark} по текущему курсу составляет \
{round(int_amount * float(data[quote_mark]), 2)} {quote_mark}'


class APIException(Exception):
    pass
