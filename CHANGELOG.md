# Changelog

Todas as alterações relevantes deste projeto serão registradas neste arquivo.

## [1.0.0] - 2026-09-17

### Adicionado

- Estrutura inicial do microsserviço de pagamentos e notificações.
- Ambiente RabbitMQ utilizando Docker Compose.
- Configuração das portas 5672 e 15672.
- Healthcheck para o RabbitMQ.
- Dependência Pika para comunicação com RabbitMQ.
- Documentação da arquitetura do projeto.
- Producer para publicação de eventos de pagamento.
- Consumer para consumo dos eventos de pagamento.