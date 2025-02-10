from typing import List

from src.config.logger import configure_logger
from src.models.article import Article
from src.scrapers.base_scraper import BaseScraper

logger = configure_logger()


class G1Scraper(BaseScraper):
    def __init__(self):
        super().__init__()
        logger.info("G1Scraper initialized")

        self.tags_to_extract = ["ul"]

    def scrape(self, url: str) -> List[Article]:
        """
        Execute a web scraper to extract content from articles on the G1 website based on the provided keyword.

        :param url: URL to scrape
        :return: List[Article]: A list of dictionaries containing structured information about the extracted
        """
        logger.info(f"Starting scraping for URL: {url}")

        try:
            extracted_content = self.scrape_with_playwright(urls=[url], tags_to_extract=self.tags_to_extract)
        except Exception as e:
            logger.error(f"Error while scraping: {e}")
            raise e
        else:
            logger.info("Scraping successfully completed")
            return extracted_content
