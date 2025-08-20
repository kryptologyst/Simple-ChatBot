import os
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain

# Load API key
_ = load_dotenv(find_dotenv())
chatbot = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Persistent memory
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True
)

# Prompt
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        ("human", "{content}")
    ]
)

# Chain
chain = LLMChain(llm=chatbot, prompt=prompt, memory=memory)

print("🤖 Chatbot ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = chain.invoke(user_input)
    print("Bot:", response["text"])
import os
import warnings

from dotenv import load_dotenv, find_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory  # modern alternative to LLMChain

# Optional: quiet deprecation noise
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

# Load .env and API key
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

# 1) Base chat model (pick a current model)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 2) Persistent memory (writes to messages.json in cwd)
store = FileChatMessageHistory("messages.json")
memory = ConversationBufferMemory(
    chat_memory=store,
    memory_key="messages",
    return_messages=True,
)

# 3) Prompt that includes the running message history
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="messages"),
    ("human", "{content}"),
])

# 4) Runnable with message history (preferred over LLMChain)
#    It pulls/pushes messages via the supplied "history factory".
def history_factory(session_id: str):
    # You can swap session IDs to maintain separate conversations.
    # Here we just reuse the same file-backed store.
    return store

chain = (prompt | llm)
with_history = RunnableWithMessageHistory(
    chain,
    history_factory,
    input_messages_key="content",
    history_messages_key="messages",
)

# 5) Interact — memory is ON for all these calls
cfg = {"configurable": {"session_id": "default"}}

print("\n----------\n")
print("hello!")
print("\n----------\n")
print(with_history.invoke({"content": "hello!"}, cfg).content)

print("\n----------\n")
print("my name is Julio")
print("\n----------\n")
print(with_history.invoke({"content": "my name is Julio"}, cfg).content)

print("\n----------\n")
print("what is my name?")
print("\n----------\n")
print(with_history.invoke({"content": "what is my name?"}, cfg).content)

