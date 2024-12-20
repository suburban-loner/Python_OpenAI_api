from openai import OpenAI
client = OpenAI()

downloaded_descriptions = [
    {'file name': '1.elves.md', 'description': '"Elves are strikingly beautiful, ethereal beings who wield spirit magic with elegant mastery. With eyes full of ancient wisdom, they handle swords and bows with fluid grace, exuding a powerful mystical aura."'},
    {'file name': '2.dark elves.md', 'description': '"Dark elves are as beautiful as elves, the only difference being that they have dark skin and malevolent eyes. They usually dwell in deserts and wield dark and blood magic, favoring daggers as weapons to strike with precision and deadly intent."'},
    {'file name': '3.orcs.md', 'description': '"Orcs are tall and are muscular with green skin and violent eyes, they thrive in forests and perilous terrains, wielding heavy weapons to dominate foes with brute strength."'},
    {'file name': '4.dragons.md', 'description': '"Dragons are shapeshifters of unmatched power, they are a reptilian race with massive muscular bodies covered in thick scales. They bare wings, razor sharp claws, and large fangs like swords. They wield potent magic beyond any other being’s capability."'},
    {'file name': '5.dwarves.md', 'description': '"Dwarves are short and muscular with tan skin and hazel eyes, they are skilled miners, blacksmiths, and warriors, wielding earth magic alongside war hammers and axes."'},
    {'file name': '6.humans.md', 'description': '"Huamns are versatile beings with low mana tolerance, they wield diverse weapons and magic, often thriving through a strong pack mentality and adaptability."'}
]

image_prompt = []

def prompt_generation():
    for entry in downloaded_descriptions:
        description = entry['description']
        file_name = entry['file name']

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You summarize the given description and make it into an image prompt, make it 30 words or less. Make it mostly physical descriptions."},
                {
                    "role": "user",
                    "content": f"make the given description an image prompt of 30 words or less: {description}. Make it more physical descriptions and appearances."
                }
            ]
        )

        image_prompt.append({
            'file name': file_name,
            'image prompt': completion.choices[0].message.content
        })

    print(image_prompt)

if __name__ == '__main__':
    prompt_generation()

