import requests

def translate_text(source_language, target_language, text):
    url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
    token = ""  # Place the access token here

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "source_language": source_language,
        "target_language": target_language,
        "text": text
    }

    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

    if response.status_code == 200:
        translated_text = response.json()["text"]
        print("Translated text:", translated_text)
    else:
        print("Error:", response.status_code, response.text)


def main():
    print("Please choose the source language:")
    source_language = input("(English, Luganda, Runyankole, Ateso, Lugbara or Acholi): ")

    if source_language.lower() == "english":
        target_language = input("Please choose the target language (Luganda, Runyankole, Ateso, Lugbara, or Acholi): ")
    else:
        target_language = "English"

    text = input("Enter the text to translate: ")

    translate_text(source_language, target_language, text)


if __name__ == '__main__':
    main()
