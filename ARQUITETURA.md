# Arquitetura do Microsserviço de Pagamentos e Notificações

## 1. Visão geral

O projeto consiste em um microsserviço responsável pelo processamento de eventos de pagamento e pela comunicação entre componentes por meio do RabbitMQ.

A comunicação é realizada de forma assíncrona utilizando uma fila de mensagens.

## 2. Componentes

### Producer

O `producer.py` é responsável por gerar e publicar eventos de pagamento no RabbitMQ.

O evento é enviado em formato JSON contendo informações como:

- ID do pagamento;
- status do pagamento;
- valor do pagamento.

### RabbitMQ

O RabbitMQ atua como intermediário de mensagens.

Ele recebe as mensagens publicadas pelo Producer e as mantém em uma fila até que sejam consumidas pelo Consumer.

A aplicação utiliza a fila:

`pagamentos`

### Consumer

O `consumer.py` é responsável por consumir as mensagens disponíveis na fila `pagamentos`.

Após receber uma mensagem, o Consumer interpreta os dados e apresenta o resultado no console.

O recebimento utiliza confirmação manual (`acknowledgment`), garantindo que a mensagem seja confirmada após o processamento.

## 3. Fluxo da mensagem

O funcionamento ocorre da seguinte maneira:

1. O Producer cria um evento de pagamento.
2. O evento é convertido para JSON.
3. O Producer publica a mensagem no RabbitMQ.
4. O RabbitMQ armazena a mensagem na fila `pagamentos`.
5. O Consumer recebe a mensagem.
6. O Consumer processa os dados.
7. O Consumer envia o `ack` para confirmar o processamento.

## 4. Fila x Tópico

Neste projeto será utilizada uma **fila (queue)**.

Na fila, as mensagens ficam armazenadas até serem consumidas por um consumidor.

O RabbitMQ também permite trabalhar com exchanges e diferentes padrões de roteamento, mas para este projeto foi adotada uma fila simples por ser suficiente para o fluxo proposto.

## 5. Comunicação

A comunicação entre Producer, RabbitMQ e Consumer ocorre utilizando o protocolo AMQP.

O RabbitMQ será executado em um container Docker.

As principais portas utilizadas são:

- `5672`: comunicação AMQP;
- `15672`: painel de gerenciamento do RabbitMQ.

## 6. Estrutura do projeto

```text
microsservico-pagamentos/
├── ARQUITETURA.md
├── CHANGELOG.md
├── README.md
├── docker-compose.yml
└── src/
    ├── consumer.py
    ├── producer.py
    └── requirements.txt