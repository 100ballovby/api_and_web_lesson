from engine import fetch_horoscope, translate_horoscope

h = fetch_horoscope('virgo')  # сохраняю гороскоп
tr = translate_horoscope(h)  # перевожу полученный гороскоп

print(tr)
