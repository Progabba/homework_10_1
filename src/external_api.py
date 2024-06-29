import os
import requests
from dotenv import load_dotenv


def get_convert(code_, amount_):
    """Функция возвращает стоимость в рублях"""
    load_dotenv()
    apikey = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": amount_, "from": code_, "to": "RUB"}
    headers = {"apikey": apikey}

    responce = requests.get(url, headers=headers, params=payload)

    return responce.json()["result"]


if __name__ == "__main__":
    print(get_convert("USD", "100"))
