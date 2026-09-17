import json
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)

channel = connection.channel()
channel.queue_declare(queue="pagamentos", durable=True)

def processar_pagamento(ch, method, properties, body):
    mensagem = json.loads(body)

    print("Pagamento recebido:")
    print(f"ID: {mensagem['pagamento_id']}")
    print(f"Status: {mensagem['status']}")
    print(f"Valor: R$ {mensagem['valor']:.2f}")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue="pagamentos",
    on_message_callback=processar_pagamento,
    auto_ack=False
)

print("Aguardando pagamentos...")
channel.start_consuming()