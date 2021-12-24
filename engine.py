import requests as r


def fetch_horoscope():  # <- функция
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    querystring = {"sign": "aquarius", "day": "today"}
    headers = {
        'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
        'x-rapidapi-key': "e2eb357b7amsh926cfc62b8ec75cp17a448jsn5b614312d78a"
    }
    response = r.post(url, headers=headers, params=querystring)
    return 'horoscope'


def translate_horoscope():  # <- функция
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {"to": "<REQUIRED>", "api-version": "3.0", "profanityAction": "NoAction", "textType": "plain"}
    payload = []
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com",
        'x-rapidapi-key': "e2eb357b7amsh926cfc62b8ec75cp17a448jsn5b614312d78a"
    }
    #response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    response = r.post(url, data=payload, headers=headers, params=querystring)
    return 'гороскоп'
