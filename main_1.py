from pprint import pprint
import requests

token = 'y0_AgAAAABdhf5MAADLWwAAAADSazhui4raWx2sRumvw9rJ_r3JIhafcg4'

class YaUploader:

    host = 'https://cloud-api.yandex.net:443'
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        url = f'https://cloud-api.yandex.net:443/v1/disk/resources/files'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        response = requests.get(url, headers=headers)
        pprint(response.json())
        status_code = response.status_code
        return(status_code)

    def _get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": path, "overwrite": True}
        response = requests.get(url, headers=headers, params=params)
        status_code = response.status_code
        print(status_code)
        pprint(response.json())
        return response.json().get('href')

    def upload(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')
        status_code = response.status_code
        with open('test.txt', 'a', encoding='utf-8') as f:
            f.write(f'Статус код работы функции [upload]: {status_code} \n')
        return status_code



if __name__ == '__main__':
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(f'test.txt файл создан \n')
    token = 'y0_AgAAAABdhf5MAADLWwAAAADSazhui4raWx2sRumvw9rJ_r3JIhafcg4'
    uploader = YaUploader(token)
    uploader.upload('/test.txt', 'test.txt')


token = 'y0_AgAAAABdhf5MAADLWwAAAADSazhui4raWx2sRumvw9rJ_r3JIhafcg4'

