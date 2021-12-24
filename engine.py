import requests as r
import json


def fetch_horoscope(sign, day='tomorrow'):  # <- функция
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    querystring = {"sign": sign, "day": day}
    headers = {
        'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
        'x-rapidapi-key': "e2eb357b7amsh926cfc62b8ec75cp17a448jsn5b614312d78a"
    }
    response = r.post(url, headers=headers, params=querystring)
    jr = response.json()  # превращаю ответ сервера в JSON-объект
    return jr['description']  # возвращаю сам гороскоп


def translate_horoscope(text, lang='ru'):  # <- функция
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {"to": lang, "api-version": "3.0", "profanityAction": "NoAction", "textType": "plain"}
    payload = [
        {'Text': text}
    ]
    pld = json.dumps(payload)  # перевожу Python код в JSON
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com",
        'x-rapidapi-key': "e2eb357b7amsh926cfc62b8ec75cp17a448jsn5b614312d78a"
    }
    response = r.post(url, data=pld, headers=headers, params=querystring)
    jr = response.json()
    return jr[0]['translations'][0]['text']
