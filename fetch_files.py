import os
import requests

folder = "continents"

URL = f"https://api.github.com/repos/suburban-loner/DnD_campaign_site/contents/content/{folder}"
GitHub_Token = os.getenv('GITHUB_TOKEN')


def fetch_files(url, token):
    headers = {
        'Authorization': f'token {token}'
    }

    response = requests.get(url)
    if response.status_code == 200:
        files = response.json()

        loacl_directory = os.path.join('downloaded_files', folder)
        if not os.path.exists(loacl_directory):
            os.makedirs(loacl_directory)
        
        

        for file in files:
            file_name = file['name']
            file_url = file['download_url']
            print(f"File name: {file_name}\n Download url: {file_url}")

            file_content = requests.get(file_url).content
            file_path = os.path.join(loacl_directory, file_name)

            with open(file_path, 'wb') as file:
                file.write(file_content)

if __name__ == "__main__":
    fetch_files(url=URL, token=GitHub_Token)