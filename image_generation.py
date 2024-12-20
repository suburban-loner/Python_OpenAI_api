import openai
import os
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")

image_prompts = [
                {'file name': '2.dark elves.md', 'image prompt': 'Brown-skinned elves in a desert, they wear more assassin and ninja clothing, wielding daggers and practicing dark and blood magic, exuding beauty and deadly intent.'},  
                {'file name': '4.dragons.md', 'image prompt': 'Majestic reptilian dragon shapeshifting, with scale-armored body, powerful wings, sword-like fangs, sharp claws, and potent glowing magical aura, soaring over a mystical landscape.'}, 
                {'file name': '5.dwarves.md', 'image prompt': 'Short, muscular dwarves with tan skin and hazel eyes, skilled in mining and blacksmithing. They wield war hammers and axes, channeling earth magic as fierce warriors.'}, 
                {'file name': '6.humans.md', 'image prompt': 'Humans wield diverse weapons and magic.Thriving through strong pack mentality and adaptability, they form dynamic groups.'}
            ]


def generate_image():
    for entry in image_prompts:
        image_prompt = entry['image prompt']
        file_name = entry['file name']

        file_name = file_name.lstrip('0123456789.')
        file_name = file_name.rstrip('.md')

        response = openai.images.generate(
        model="dall-e-3",
        prompt= f"{image_prompt}",
        size="1024x1024",
        quality="standard",
        n=1,
        )

        image_url = response.data[0].url
        image_data = requests.get(image_url).content

        image_new_name = f"{file_name}_cover.webp"
        with open(image_new_name, 'wb') as image:
            image.write(image_data)

        print(f"Image saved as {image_new_name}")

if __name__ == '__main__':
    generate_image()
