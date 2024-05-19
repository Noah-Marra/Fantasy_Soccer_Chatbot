import os
from groq import Groq

groq_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_key)

def groq_chat(messages: list[dict], model = 'llama3-70b-8192', temperature = 0.5, max_tokens = 2048, top_p = 0.95, stream = False, stop = None):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        stream=stream, 
        stop=stop
    )

    return chat_completion

# chat = groq_chat(messages=[{'role': 'user', 'content': 'how are you doing?'}])
# print (chat.choices[0].message.content)