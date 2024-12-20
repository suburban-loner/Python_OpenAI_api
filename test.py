import os

folder = "characters"

def replace_cover_image():
    downloaded_path = f"downloaded_files/{folder}"

    if not os.path.exists(downloaded_path):
        print(f"The folder {downloaded_path} does not exist.")

    for file in os.listdir(downloaded_path):
        file_path = os.path.join(downloaded_path, file)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.readlines()

            updated_content = []
            cover_updated = False

            for line in content:
                if line.strip().startswith('cover:'):
                    line_raw = line.lstrip("cover: /").rstrip('.webp\n')
                    line_update = line.lstrip("cover: /").rstrip('.webp\n')
                    new_cover_image = f"{line_update}_cover.webp"
                    updated_content.append(new_cover_image)
                    
            file_name = file.lstrip('0123456789.').rstrip('.md')

        
        print(file)
        print(file_name)
        print(line_raw)
        print(updated_content)



if __name__ == "__main__":
    replace_cover_image()
