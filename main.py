import requests

def superhero_request(superheroes):
    heroes_list = []
    heroes_int = []
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    for heroes in response.json():
        if heroes["name"] in superheroes:
            heroes_list.append(heroes)
    for element in heroes_list:
        heroes_int.append(element['powerstats']['intelligence'])
    return max(heroes_int)


if __name__ == '__main__':
    print(superhero_request(["Hulk", "Captain America", "Thanos"]))
