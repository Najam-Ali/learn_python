import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        user_country = user_data["location"]["coordinates"]["latitude"]
        return user_name, user_country
    else:
        raise Exception("Failed to fetch user data.") # Raise Error massage if error exist.
def main():
    try:
        for i in range(5):
            user_name, user_country = fetch_random_user_freeapi()
            print(type(f'User_name = {user_name}, country = {user_country}'))
        # print(f"user_name = {user_name} the user_country = {user_country}")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()
