import streamlit as st

from src.services.news_search_agent import NewsSearchAgent


def news_search_interface():
    st.title("🦜🔗 Procure Notícias em portais!")

    options = st.multiselect(
        "Qual portal deseja buscar?",
        ["G1"],
    )

    if options:
        with st.form("my_form"):

            text = st.text_area("Procure notícias sobre...", "")
            submitted = st.form_submit_button("Submit")

            if submitted:
                text += " " + "Procurar entre as notícias do site: " + " ".join(options)
                agent = NewsSearchAgent()
                response = agent.generate_response(text)
                st.markdown(response)
