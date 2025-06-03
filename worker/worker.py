import pika, json, random, time, sys

worker_type = sys.argv[1] 
time.sleep(20)  
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='calculs')
channel.queue_declare(queue='resultats')

def calculer(op, n1, n2):
    if op == 'add':
        return n1 + n2
    elif op == 'sub':
        return n1 - n2
    elif op == 'mul':
        return n1 * n2
    elif op == 'div':
        return n1 / n2 if n2 != 0 else 'inf'

def callback(ch, method, properties, body):
    data = json.loads(body)
    n1, n2, op = data['n1'], data['n2'], data['op']
    if op == worker_type or op == 'all':
        result = calculer(worker_type, n1, n2)
        time.sleep(random.randint(5, 15))
        response = json.dumps({
            'n1': n1,
            'n2': n2,
            'op': worker_type,
            'result': result,
            'client_id': data.get('client_id')
        })
        channel.basic_publish(exchange='', routing_key='resultats', body=response)
        print(f"[x] {worker_type.upper()} résultat envoyé: {response}", flush=True)
    else:
        ch.basic_publish(exchange='', routing_key='calculs', body=body)
channel.basic_consume(queue='calculs', on_message_callback=callback, auto_ack=True)
print(f" [*] Worker {worker_type} en attente de calculs...")
channel.start_consuming()
