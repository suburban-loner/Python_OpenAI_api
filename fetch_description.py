import os

downloaded_description = []
folder = "characters"

def fetch_description():
    downloaded_path = f"downloaded_files/{folder}"

    if not os.path.exists(downloaded_path):
        print(f"The folder {downloaded_path} does not exist.")
        return

    for file in os.listdir(downloaded_path):
        file_path = os.path.join(downloaded_path, file)
        if os.path.isfile(file_path):
            with open(os.path.join(downloaded_path, file), 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith('description'):
                        description = line.strip('description: ').strip('" "').strip('\n')
                        break
        
        downloaded_description.append({
            'file name': file,
            'description': description if description else "No description found."
        })

    for item in downloaded_description:
        print(item)


if __name__ == '__main__':
    fetch_description()
