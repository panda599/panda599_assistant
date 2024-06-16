from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
def get_chat_response(prompt, memory):
     model = ChatOpenAI(model = "gpt-3.5-turbo", api_key = "sk-HsWVP4ZpGbH2DQZD40DbDb41F1Ff44Bc8553D73a517613Df",base_url="https://api.aigc369.com/v1")
     chain = ConversationChain(llm= model,memory=memory)
     response = chain.invoke({"input":prompt})
     return response["response"]

#memory =ConversationBufferMemory(return_messages = True)
#print(get_chat_response("牛顿提出过哪些著名的定率",memory))
#print(get_chat_response("我的上一个问题是啥",memory))



