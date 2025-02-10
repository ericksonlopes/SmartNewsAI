# SmartNewsAI

SmartNewsAI is an intelligent news discovery application that leverages web scraping and natural language processing to provide users with relevant news articles from various portals. The project uses Streamlit for the user interface and LangChain for web scraping and language model integration.

## Features

- **User Interface**: Built with Streamlit, allowing users to interact with the application through a web-based interface.
- **News Search**: Users can select a news portal and enter a search query to find relevant news articles.
- **Web Scraping**: Utilizes custom scrapers to extract content from news websites.
- **Language Model Integration**: Uses OpenAI's GPT models to process and generate responses based on user queries.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ericksonlopes/SmartNewsAI.git
    cd SmartNewsAI
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install pipenv
    pipenv install
    ```

4. Install Playwright:
    ```sh
    playwright install
    ```

## Configuration

1. Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

2. Configure the logger by editing the `src/config/logger.py` file if necessary.

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run main.py
    ```

2. Open your web browser and navigate to the provided URL (usually `http://localhost:8501`).

<div align="center">
    <img src="doc/app.png" alt="app.png">
</div>

3. Use the interface to select a news portal, enter a search query, and submit the form to get relevant news articles.

## Project Structure

- `src/`: Contains the source code for the project.
- `config/`: Configuration files for logging and other settings.
- `interface/`: Streamlit interface code.
- `models/`: Data models used in the project.
- `scrapers/`: Web scraping classes and methods.
- `services/`: Core services including the `NewsSearchAgent`.
- `tools/`: Tools for generating search URLs and scraping content.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.