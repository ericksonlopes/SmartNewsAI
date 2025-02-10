from langchain.agents import Tool

from src.scrapers.g1_scraper import G1Scraper

g1_scraper_tool = Tool(
    name="Executar Scraper",
    func=G1Scraper().scrape,
    description="Executa um scraper para extrair conteúdo de artigos no site do G1 com base na URL fornecida. "
                "Retorna uma lista de objetos `Article` contendo informações estruturadas sobre os artigos extraídos."
)
