import json
from sentence_transformers import SentenceTransformer, util

# Carregar FAQs de um arquivo JSON
with open('faqs.json', 'r', encoding='utf-8') as f:
    faqs = json.load(f)

# Preparar modelo BERT
print("Carregando modelo BERT...")
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Pré-computar embeddings das perguntas FAQ
faq_questions = list(faqs.keys())
faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)

def responder_pergunta(pergunta_usuario):
    user_embedding = model.encode(pergunta_usuario, convert_to_tensor=True)
    cosine_scores = util.cos_sim(user_embedding, faq_embeddings)
    top_result = cosine_scores.argmax()
    resposta = faqs[faq_questions[top_result]]
    return resposta

if __name__ == "__main__":
    print("Chatbot FAQ iniciado. Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Bot: Até logo!")
            break
        resposta = responder_pergunta(user_input)
        print(f"Bot: {resposta}")
