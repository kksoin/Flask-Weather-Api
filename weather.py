def weather_city(city, requests, BS):
    city = city.replace(' ', '+')
    r = requests.get(f'https://sinoptik.ua/погода-{city}')
    for el in BS(r.content, 'html.parser').select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        night = el.select('.temperature .p1')[0].text
        night_felt = el.select('.temperatureSens .p1')[0].text
        morning = el.select('.temperature .p3')[0].text
        morning_felt = el.select('.temperatureSens .p3')[0].text
        day = el.select('.temperature .p5')[0].text
        day_felt = el.select('.temperatureSens .p5')[0].text
        evening = el.select('.temperature .p7')[0].text
        evening_felt = el.select('.temperatureSens .p7')[0].text
        time_temp = el.select('.lSide .today-time')[0].text
        temp = el.select('.lSide .today-temp')[0].text
        description = el.select('.wDescription .description')[0].text
        if not description:
            description = 'Отсутствует информация'
        else:
            description = description
        sunrise_and_sunset = el.select('.lSide .infoDaylight')[0].text.split()

        weather = {
            "city": city.replace('+', ' '),
            "min": t_min,
            "max": t_max,
            "night": night,
            "night felt": night_felt,
            "morning": morning,
            "morning felt": morning_felt,
            "day": day,
            "day felt": day_felt,
            "evening": evening,
            "evening felt": evening_felt,
            "now": time_temp + ' ' + temp,
            "description": description,
            "sunrise": sunrise_and_sunset[0] + ' ' + sunrise_and_sunset[1],
            "sunset": sunrise_and_sunset[2] + ' ' + sunrise_and_sunset[3]
        }
        return weather
    else:
        return {"status": "fail", "cause": "город не найден"}