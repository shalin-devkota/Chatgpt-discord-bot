from revChatGPT.revChatGPT import Chatbot

config = {
    "email": "email-here",
    "password": "pwd-here",
   
}

chatbot = Chatbot(config, conversation_id=None)

def get_response(message):
    reply = chatbot.get_chat_response(message)
    return(reply['message'])
