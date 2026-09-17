import json
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672)
)

channel = connection.channel()

channel.queue_declare(queue="pagamentos", durable=True)

pagamento = {
    "pagamento_id": 1,
    "status": "APROVADO",
    "valor": 150.00
}

mensagem = json.dumps(pagamento)

channel.basic_publish(
    exchange="",
    routing_key="pagamentos",
    body=mensagem,
    properties=pika.BasicProperties(delivery_mode=2)
)

print(f"Pagamento enviado: {mensagem}")

connection.close()