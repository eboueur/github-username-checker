import requests
from requests.structures import CaseInsensitiveDict


base_url = "https://github.com/"


with open("input.txt", "r") as file:
    usernames = file.read().splitlines()


headers = CaseInsensitiveDict()
headers["authority"] = "github.com"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"

for username in usernames:
    user_url = base_url + username
    resp = requests.get(user_url, headers=headers)

    if resp.status_code == 404:
        print(f"L'utilisateur '{username}' est disponible.")
    elif resp.status_code == 200:
        print(f"L'utilisateur '{username}' existe déjà.")
    else:
        print(f"Erreur {resp.status_code} lors de la vérification pour '{username}'.")


        with open("output.txt", "a") as output_file:
            output_file.write(username + "\n")