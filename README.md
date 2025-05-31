# Chatbot FAQ - Automatização Inteligente

Este projeto é um protótipo de chatbot para responder automaticamente a perguntas frequentes (FAQs) em universidades ou serviços públicos usando Processamento de Linguagem Natural (PLN).

## Funcionalidades

✅ Carrega base de perguntas/respostas (FAQs)  
✅ Usa embeddings BERT para comparar perguntas  
✅ Responde automaticamente a perguntas semelhantes  
✅ Protótipo simples e rápido de rodar

## Como rodar

1. Clone o repositório:
```bash
git clone <seu-repo>
cd <seu-repo>
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o chatbot:
```bash
python bot.py
```

## Exemplo de uso

```
Você: Como emitir boleto de matrícula?
Bot: Acesse o Portal do Aluno > Financeiro > Segunda via.
```

## Requisitos

- Python 3.8+
- Conexão com internet (para baixar modelo BERT)
