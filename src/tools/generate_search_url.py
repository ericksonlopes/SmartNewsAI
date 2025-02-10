from langchain.agents import Tool

from src.config.logger import configure_logger

logger = configure_logger()


def generate_search_url_g1(keyword: str) -> str:
    """
    Generate a search URL for the G1 website.
    :param keyword: Keyword to search
    :return: URL
    """
    try:
        logger.info(f"Generating search URL for keyword: {keyword}")

        base_url = "https://g1.globo.com/busca/?q="
        url = f"{base_url}{keyword.replace(' ', '+')}"

    except Exception as e:
        logger.error(f"Error generating search URL: {e}")
        raise e
    else:
        logger.info("Search URL generated")
        return url


generate_search_url_tool = Tool(
    name="Gerar URL de Busca",
    func=generate_search_url_g1,
    description="Gera uma URL de busca no site do G1 com base na palavra-chave fornecida. "
                "A URL gerada pode ser usada para realizar buscas diretamente no site do G1."
)
