from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from langchain_gigachat.chat_models import GigaChat
import os
from dotenv import load_dotenv
from logger import logger
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
gigachat_api = os.getenv("API_GIGACHAT")

async def generating(text:str, prompt: str):
    try:
        logger.info('Connecting to gigachat API')
        giga = GigaChat(
            credentials=gigachat_api,
            verify_ssl_certs=False,
            model = 'GigaChat-2-Pro'
        )
        tools = []
        # agent_executor = create_react_agent(giga,
        #                                     tools,
        #                                     checkpointer=MemorySaver(),
        #                                     prompt = prompt)

        try:
            logger.info('Starting generating process')
            messages = [SystemMessage(
                content=prompt
            ),
                HumanMessage(content=text)]
            res = giga.invoke(messages)
            return res.content
        except Exception as e:
            logger.error('Error in generating process: %s', e)
    except Exception as e:
        logger.error('Error in connecting to gigachat API: %s', e)