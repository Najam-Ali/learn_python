import requests

def jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        jokes_data = data["data"]
        joke = jokes_data["content"]
        return joke
    else:
        raise Exception("User fail in fetch data.")

def main():
    try:
        joke_content = 'store_joke.text'
        joke = jokes()
        with open(joke_content, 'a') as file:
            file.write(joke)    
        print(f"The joke is = {joke}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()