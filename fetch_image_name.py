import os

downloaded_image_names = []
folder = "characters"

def fetch_image_and_name():
    downloaded_path = f"downloaded_files/{folder}"

    if not os.path.exists(downloaded_path):
        print(f"The folder {downloaded_path} does not exist.")
        return

    for file in os.listdir(downloaded_path):
        file_path = os.path.join(downloaded_path, file)
        if os.path.isfile(file_path):
            with open(os.path.join(downloaded_path, file), 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith('cover'):
                        image_name = line.strip('cover: ').strip('\n')
                        break
        
        downloaded_image_names.append({
            'file name': file,
            'image name': image_name
        })

    for item in downloaded_image_names:
        print(item)


if __name__ == '__main__':
    fetch_image_and_name()

