import os

from decouple import config
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI

from src.config.logger import configure_logger
from src.tools.g1_scraper_tool import g1_scraper_tool
from src.tools.generate_search_url import generate_search_url_tool

logger = configure_logger()


class NewsSearchAgent:
    def __init__(self):
        os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

        self.verbose = False

        self.tools = [
            generate_search_url_tool,
            g1_scraper_tool
        ]

        try:
            # Inicializando o agente
            self.llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0,
            )
        except Exception as e:
            logger.error(f"Error initializing the agent: {e}")
            raise e

        try:
            self.agent_chain = initialize_agent(
                tools=self.tools,
                llm=self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=self.verbose
            )
        except Exception as e:
            logger.error(f"Error initializing the agent chain: {e}")
            raise e

    def generate_response(self, text):
        try:
            result = self.agent_chain.invoke(text)
            return result.get('output')
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            raise e
