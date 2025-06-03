import pika, json, time

time.sleep(20)  
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='resultats')

def callback(ch, method, properties, body):
    data = json.loads(body)
    if data.get('client_id') == 'user':
        print(f"[x] Résultat reçu: {data}", flush=True)
    print(f"[Résultat] {data}", flush=True)
channel.basic_consume(queue='resultats', on_message_callback=callback, auto_ack=True)
print(' [*] En attente des résultats...')
channel.start_consuming()
