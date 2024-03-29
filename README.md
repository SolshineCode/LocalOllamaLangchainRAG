# LocalOllamaLangchainRAG
Uses Langchain and ChromaDB locally to interface with Ollama LLMs and deliver RAG chunk from a custom library along with the user's prompts.

Inference and RAG are done entirely locally, with the only internet connection required is for if the URL specifies a website for the RAG references. URL can be a localhost.

Steps
- Create Conda Env (optional but advised) or run from terminal or powershell.
- Installing Ollama and pulling model via Ollama.
- Install requirements.txt in env
- Edit .py if you want specific model (model in .py currently named "example")
- Call the .py program by navigating to file and calling the program with two arguments as follows:
-- Pass your question + URL here in quotes as:
--- Your Question/Prompt is 1st argument when calling the program to run
--- URL for library or reference website is 2nd argument when calling the program to run
- Wait and watch for the following print messages:
  OllamaLangchainRAG.py is running
  Loaded documents
  Built index
  Created retrieval chain
- Finally print(response["answer"]) and print("Context: " + str(response["context"])) will execute
- Response from the LLM will be printed
- As the final action, the context from the RAG retrieval step will be printed
