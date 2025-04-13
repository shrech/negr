import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/TON_WEBHOOK_ICI"

def send_to_webhook(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message})
    except Exception as e:
        print(f"[Erreur Webhook] {e}")

def main():
    print("[09] > Avatar Grabber")
    # Ajout de la logique spécifique ici (par exemple, récupérer un avatar d'un utilisateur)
    message = "Avatar Grabber exécuté avec succès !"
    print(message)
    
    send_to_webhook(message)  # Envoie un message au webhook

if __name__ == "__main__":
    main()
