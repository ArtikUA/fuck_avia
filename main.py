import requests

url_pattern = 'https://api.skypicker.com/flights?v=2&sort=quality&asc=1&locale=ru&daysInDestinationFrom=&daysInDestinationTo=&children=0&infants=0&flyFrom={fr}&to={to}&dateFrom=20/06/2016&dateTo=20/06/2016&typeFlight=oneway&returnFrom=&returnTo=&one_per_date=0&oneforcity=0&wait_for_refresh=1&adults=1&limit=45'

with open("codes.txt") as f:
    for line in f:

        mass = line.strip().split(' — ')
        code = mass[0]
        name = ""
        for i in range(1, len(mass)):
            part = mass[i]
            name += part

        url = url_pattern.format(fr='KBP', to=code)
        json = requests.get(url).json()

        if json['data']:
            minimum = 0
            for data in json['data']:
                price = data['conversion']['EUR']
                if minimum == 0 or price < minimum:
                    minimum = price
            print("{} ({})\t{}".format(name, code, minimum))
