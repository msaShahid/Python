from pip._vendor import requests


def getUserdata():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        userData = data['data']
        username = userData["login"]["username"]
        country = userData["location"]["country"]
        return username,country
    else:
        raise Exception("Fail to fetch user data!")
    
def main():
    try:
        username,country = getUserdata()
        print(f"username : {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()