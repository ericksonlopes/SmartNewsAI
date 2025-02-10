from pydantic import BaseModel, Field


class Article(BaseModel):
    """
    Represents an article with structured information.
    """
    headline: str = Field(description="The title of the article")
    description: str = Field(description="A short description of the article")
    date: str = Field(description="The date the article was published")
    publisher: str = Field(description="The publisher of the article")
    link: str = Field(description="The link to the article")
