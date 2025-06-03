import pika, json, random, time

time.sleep(20)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='calculs')
while True:
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    op = random.choice(['add', 'sub', 'mul', 'div', 'all'])  
    data = json.dumps({'n1': n1, 'n2': n2, 'op': op, 'client_id':'auto'})
    channel.basic_publish(exchange='', routing_key='calculs', body=data)
    print(f"[x] Envoyé: {data}", flush=True)
    time.sleep(random.uniform(3, 6))
