#Purpose: Send the question and retrieved context to Qwen through Ollama.
"""
Goals:
-load prompt template
-format retrieved context
-call Qwen
-return generated answer
"""
import ollama
from retrieval import retrieve
from system.config import settings

language_model = settings.LANGUAGE_MODEL
input_query = input("I am SANDI, ask me a question:")
retrieved_knowledge = retrieve(input_query)

print("Retrieval Knowledge: ")
for chunk, similarity in retrieved_knowledge:
  print(f' - (similarity: {similarity:.2f}) {chunk}')

  instruction_prompt = f'''You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{'\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])}
'''
stream = ollama.chat(
  model=language_model,
  messages=[
    {'role': 'system', 'content': instruction_prompt},
    {'role': 'user', 'content': input_query},
  ],
  stream=True,
)

# print the response from the chatbot in real-time
print('Chatbot response:')
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

