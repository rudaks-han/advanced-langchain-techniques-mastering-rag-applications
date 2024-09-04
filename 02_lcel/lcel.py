from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

result = chain.invoke({"topic": "ice cream"})
print(result)

# from langchain_core.messages.human import HumanMessage
#
# messages = [HumanMessage(content='tell me a short joke about ice cream')]
# model.invoke(messages)