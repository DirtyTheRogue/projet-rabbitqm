import pika, json

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='calculs')

print("=== Client interactif pour envoyer des calculs ===")

while True:
    try:
        n1 = int(input("Entrez n1 : "))
        n2 = int(input("Entrez n2 : "))
        op = input("Entrez l'opération (add, sub, mul, div, all) : ").strip().lower()
        if op not in ['add', 'sub', 'mul', 'div', 'all']:
            print("Opération invalide. Choisissez parmi add, sub, mul, div, all.")
            continue
        data = json.dumps({'n1': n1, 'n2': n2, 'op': op, 'client_id': 'user'})
        channel.basic_publish(exchange='', routing_key='calculs', body=data)
        print(f"[x] Message envoyé: {data}")
    except KeyboardInterrupt:
        print("\n[!] Arrêt demandé par l'utilisateur.")
        break
    except ValueError:
        print("[!] Veuillez entrer des entiers pour n1 et n2.")
    except Exception as e:
        print(f"[!] Erreur : {e}")

connection.close()
