import streamlit as st

from src.services.news_search_agent import NewsSearchAgent


def news_search_interface():
    st.title("🦜🔗 Search for news on portals!")

    options = st.multiselect(
        "Which portal do you want to search?",
        ["G1"],
    )

    if options:
        with st.form("my_form"):

            text = st.text_area("Search for news about...", "")
            submitted = st.form_submit_button("Submit")

            if submitted:
                text += " " + "Search among the news on the site: " + " ".join(options)
                agent = NewsSearchAgent()
                response = agent.generate_response(text)
                st.markdown(response)
