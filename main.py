import requests
from pprint import pprint
# 1 задание
# def superhero_request(superheroes):
#     heroes_list = []
#     heroes_int = []
#     url = "https://akabab.github.io/superhero-api/api/all.json"
#     response = requests.get(url)
#     for heroes in response.json():
#         if heroes["name"] in superheroes:
#             heroes_list.append(heroes)
#     for element in heroes_list:
#         heroes_int.append(element['powerstats']['intelligence'])
#     return max(heroes_int)


# if __name__ == '__main__':
#     print(superhero_request(["Hulk", "Captain America", "Thanos"]))

# 2 задание
# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token

#     def upload(self, file_path: str, filename):
#         upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
#         headers = {
#             'Authorization': f'OAuth {token}'
#         }
#         params = {"path": file_path, "overwrite": "true"}
#         response = requests.get(upload_url, headers = headers, params = params)
#         data = response.json()['href']
#         upload_file = requests.put(data, data = open(filename, 'rb'))
#         upload_file.raise_for_status()
#         if upload_file.raise_for_status == 201:
#             print('success')


# if __name__ == '__main__':
#     path_to_file = "IT/test_file.txt"
#     filename = "file.txt"
#     token = ''
#     uploader = YaUploader(token)
#     result = uploader.upload(path_to_file, filename)

# 3 задание
# даты от 03.07.2023 до 05.07.2023  
if __name__ == '__main__':
    url = "https://api.stackexchange.com//2.3/answers?fromdate=1688342400&todate=1688515200&order=desc&sort=activity&tags='Python'&site=stackoverflow"
    response = requests.get(url)
    pprint(response.json())
