import os
from abc import ABC, abstractmethod
from typing import List

from decouple import config
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config.logger import configure_logger
from src.models.article import Article

logger = configure_logger()


class BaseScraper(ABC):
    """
    class BaseScraper(ABC) -> Abstract class for web scraping.

    Methods:
        __init__: Initializes the scraper with a language model (LLM) and configures the API.
        extract: Performs the extraction of structured information from the provided content.
        scrape_with_playwright: Performs document loading and transformation using web scraping.

    Attributes:
        llm: The language model used for text generation.
        structured_llm: The language model with structured output.

    """

    def __init__(self):
        logger.info("Starting WebScraper...")
        os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

        try:
            self.llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0,
            )
            self.structured_llm = self.llm.with_structured_output(Article)
        except Exception as e:
            logger.error(f"Erro ao inicializar o WebScraper: {e}")
            raise e

    def __extract(self, content):
        """
        Extracts structured information from the provided content.
        :param content:
        :return:
        """
        logger.info(f"Extracting structured information from content: {content}")
        response = self.structured_llm.invoke(content)

        return response

    def scrape_with_playwright(self, urls: List[str], tags_to_extract: List[str]):
        logger.info(f"Starting scraping with Playwright for URLs: {urls}")

        try:
            loader = AsyncChromiumLoader(urls)
            docs = loader.load()

            bs_transformed = BeautifulSoupTransformer()
            docs_transformed = bs_transformed.transform_documents(
                documents=docs,
                tags_to_extract=tags_to_extract,
            )

            splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                chunk_size=2000,
                chunk_overlap=0
            )

            splits = splitter.split_documents(
                documents=docs_transformed
            )

            extracted_content = []
            for split in splits:
                extracted_content.append(
                    self.__extract(content=split.page_content)
                )
        except Exception as e:
            logger.error(f"Error while scraping with Playwright: {e}")
            raise e
        else:
            logger.info("Scraping with Playwright completed successfully.")
            return extracted_content

    @abstractmethod
    def scrape(self, url: str) -> List[Article]:
        """
        Execute a web scraper to extract content from articles on the G1 website based on the provided keyword.

        :param url: URL to scrape
        :return: List[Article]: A list of dictionaries containing structured information about the extracted
        """
        pass
