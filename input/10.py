import requests

def grab_banner(user_id):
    url = f"https://discordapp.com/api/v9/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        banner_url = response.json()["banner"]
        print(f"L'URL de la bannière est : https://cdn.discordapp.com/banners/{user_id}/{banner_url}")
    else:
        print("[-] Erreur lors de la récupération de la bannière.")

user_id = input("Entrez l'ID de l'utilisateur : ")
grab_banner(user_id)