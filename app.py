import gradio as gr
import os 

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from configs import config
from halo import Halo

# os.system('sudo apt update')
# os.system('sudo apt install ffmpeg -y')

files = os.listdir('uploads')
files = [f'uploads/{file}' for file in files]

text = ''

for file in files : 
    
    spinner = Halo(text = f'Ingesting {file}' , spinner = 'dots')
    spinner.start()

    text += config.wrapper.extraction_wrapper[file.split('.')[-1]](file)

    spinner.stop()

embeddings = HuggingFaceEmbeddings(model_name = 'all-MiniLM-L6-v2')

chunks = [
    text[index : index + 1024] 
    for index 
    in range(0 , len(text) , 1024)
]

vectorstore = FAISS.from_texts(chunks , embedding = embeddings)

vectorstore.save_local('vectorstore')

model = ChatGroq(
    temperature = 0 ,
    model_name = 'mixtral-8x7b-32768' ,
    groq_api_key = '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')

prompt = ChatPromptTemplate.from_messages(
    [
        (
            'human' ,
            '''
            Use the following context as your learned knowledge, inside <context></context> XML tags.
            <context>
                {context}
            </context>
        
            When answer to user:
            - If you don't know, just say that you don't know.
            - If you don't know when you are not sure, ask for clarification.
            - Return your answer in markdown
            Avoid mentioning that you obtained the information from the context.
            And answer according to the language of the user's question.
        
            Given the context information, answer the query.
            Query: {query}
            '''
        )
    ]
)

chain = prompt | model

def search(query) : 

    vectorstore = FAISS.load_local(
        'vectorstore' , 
        embeddings = embeddings , 
        allow_dangerous_deserialization = True
    )

    similar_docs = vectorstore.similarity_search(query)

    context = ' '.join([
        doc.page_content 
        for doc 
        in similar_docs
    ])

    response = chain.invoke({
        'context' : context ,
        'query' : query
    })

    return response.content

iface = gr.Interface(
    fn=search,
    inputs=gr.Textbox(label="Query"),
    outputs=gr.Textbox(label="Response")
)

# Launch the interface
iface.launch(share = True , debug = True)