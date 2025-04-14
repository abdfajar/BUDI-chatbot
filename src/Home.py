import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="BUDI | Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**GitHub:**",
"[yvann-hub/Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot)")

    st.write("**Medium:** "
"[@yvann-hub](https://medium.com/@yvann-hub)")

    st.write("**Twitter:** [@yvann_hub](https://twitter.com/yvann_hub)")
    st.write("**Mail** : barbot.yvann@gmail.com")
    st.write("**Created by Yvann**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>BUDI, Asisten anda yang sadar Data 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>Saya BUDI, chatbot cerdas yang dibuat dengan menggabungkan 
        kekuatan Langchain dan Streamlit. 
        Saya menggunakan model bahasa yang besar (LLM / Large Language Model) 
        untuk menyediakan interaksi yang peka terhadap konteks. 
        Tujuan saya adalah membantu Anda lebih memahami data Anda. Saya mendukung PDF, TXT, CSV, transkrip Youtube 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 Laman BUDI")
st.write("""
- **BUDI-Chat**: Chat umum dengan sumber data (PDF, TXT,CSV) dengan [vectorstore](https://github.com/facebookresearch/faiss) (indeks bagian yang berguna (maks 4) untuk menanggapi pengguna) |  menggunakan [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **BUDI-Sheet** (beta): Dialog dengan data tabular (CSV) | untuk informasi yang tepat | memproses seluruh file | bekerja dengan [CSV_Agent]](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) untuk manipulasi data dan pembuatan grafik
- **BUDI-Youtube**: Meringkas video YouTube dengan [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**BUDI sedang dalam pengembangan rutin dari OSS. Jangan ragu untuk berkontribusi dan membantu saya membuatnya lebih sadar data!**
""", unsafe_allow_html=True)





