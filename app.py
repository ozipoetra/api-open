from re_gpt import SyncChatGPT

session_token = ""
conversation_id = None # conversation ID here


with SyncChatGPT(session_token=session_token) as chatgpt:
    prompt = input("Enter your prompt: ")

    if conversation_id:
        conversation = chatgpt.get_conversation(conversation_id)
    else:
        conversation = chatgpt.create_new_conversation()

    for message in conversation.chat(prompt):
        print(message["content"], flush=True, end="")
