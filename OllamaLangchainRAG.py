#First, follow the instructions for Ollama to set up and run a local Ollama instance:
# Download Ollama (or Conda install) and Fetch a model via ollama pull llama2 (Or whatever model you fill in the code)
#In Conda may need also: conda install conda-forge::chromadb

#Remember to pip install requirements.txt
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
print("OllamaLangchainRAG.py is running")

llm = Ollama(model="llama2") #Natural Farmer Model Specified here

user_prompt = "how can langsmith help with testing?" #Enter your question here

#Establish Ollama Embeddings
embeddings = OllamaEmbeddings()

#Website based loaded - TO BE UPDATED WITH LOCAL SOLUTION
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide") #change website for Docs
docs = loader.load()
print("Loaded documents")
      
#Build index
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)
print("Built index")

#Chain together the user prompt and the document context into the prompt
prompt = ChatPromptTemplate.from_template("""Answer the following question utilizing the provided context:

<context>
{context}
</context>

Question: {input}""") #Add Master Prompt Chain Here When It's Ready

document_chain = create_stuff_documents_chain(llm, prompt)

## Could run ourselves directly via:
# document_chain.invoke({
#     "input": "how can langsmith help with testing?",
#     "context": [Document(page_content="langsmith can let you visualize test results")]
# })

# Or we can create a retrieval chain to do it for us
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
print("Created retrieval chain")

# Now we can ask a question by invoking the chain
response = retrieval_chain.invoke({"input": user_prompt})
                # ***** REMEMBER TO SET user_prompt to the user's question ******
print(response["answer"])
print("context: " + context)
# Note from Docs: LangSmith offers several features that can help with testing:...


