from llama_index.core.llms import ChatMessage

def transform_past_messages(past_messages: list[dict], messages = []):
    for message in past_messages:
        messages.append(ChatMessage(role=message['role'], content=message['text']),)
    
    return messages