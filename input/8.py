import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/TON_WEBHOOK_ICI"

def send_to_webhook(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message})
    except Exception as e:
        print(f"[Erreur Webhook] {e}")

def main():
    print("[08] > Username Checker")
    # Ajout de la logique spécifique ici (par exemple, vérifier si un nom d'utilisateur est valide)
    message = "Username Checker exécuté avec succès !"
    print(message)
    
    send_to_webhook(message)  # Envoie un message au webhook

if __name__ == "__main__":
    main()
