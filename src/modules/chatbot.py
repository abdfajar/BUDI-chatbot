import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts.prompt import PromptTemplate
from langchain.callbacks import get_openai_callback

#fix Error: module 'langchain' has no attribute 'verbose'
import langchain
langchain.verbose = False

class Chatbot:

    def __init__(self, model_name, temperature, vectors):
        self.model_name = model_name
        self.temperature = temperature
        self.vectors = vectors

    qa_template = """
        Anda adalah asisten AI yang membantu bernama BUDI yang mempunyai arti Bogor Untuk Digitalisasi Informasi. 
        Pengguna memberi Anda sebuah berkas yang isinya diwakili oleh potongan konteks berikut, gunakan potongan tersebut untuk menjawab pertanyaan di bagian akhir.
        Jika Anda tidak tahu jawabannya, katakan saja Anda tidak tahu. JANGAN mencoba mengarang jawaban.
        Jika pertanyaannya tidak terkait dengan konteks, jawablah dengan sopan bahwa Anda hanya akan menjawab pertanyaan yang terkait dengan konteks.
        Gunakan detail sebanyak mungkin saat menjawab..

        Konteks: {context}
        =========
        Pertanyaan: {question}
        ======
        """

    QA_PROMPT = PromptTemplate(template=qa_template, input_variables=["context","question" ])

    def conversational_chat(self, query):
        """
        Start a conversational chat with a model via Langchain
        """
        llm = ChatOpenAI(model_name=self.model_name, temperature=self.temperature)

        retriever = self.vectors.as_retriever()


        chain = ConversationalRetrievalChain.from_llm(llm=llm,
            retriever=retriever, verbose=True, return_source_documents=True, max_tokens_limit=4097, combine_docs_chain_kwargs={'prompt': self.QA_PROMPT})

        chain_input = {"question": query, "chat_history": st.session_state["history"]}
        result = chain(chain_input)

        st.session_state["history"].append((query, result["answer"]))
        #count_tokens_chain(chain, chain_input)
        return result["answer"]


def count_tokens_chain(chain, query):
    with get_openai_callback() as cb:
        result = chain.run(query)
        st.write(f'###### Tokens used in this conversation : {cb.total_tokens} tokens')
    return result 

    
    
