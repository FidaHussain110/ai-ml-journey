documents = [
    "Python is a high-level programming language commonly used in data science and artificial intelligence.",

    "Machine learning is a subset of artificial intelligence where computers learn patterns from data.",

    "Deep learning uses neural networks with multiple layers to learn complex patterns.",

    "A neural network consists of interconnected nodes called neurons that process information.",

    "Large Language Models are AI systems trained on massive amounts of text data.",

    "Tokens are small pieces of text that language models process instead of entire sentences.",

    "Embeddings convert text into numerical vectors that capture semantic meaning.",

    "Vector databases store embeddings and enable similarity search across documents.",

    "RAG stands for Retrieval Augmented Generation and combines search with language models.",

    "Prompt engineering is the practice of designing effective inputs for language models.",

    "LangChain is a framework used to build applications powered by large language models.",

    "Fine-tuning adapts a pre-trained model to perform better on a specific task.",

    "Hallucination occurs when a language model generates incorrect or fabricated information.",

    "Cosine similarity is a mathematical technique used to measure similarity between vectors.",

    "Transformers are neural network architectures that power modern language models."
]

# helper function for printing borders
def print_border(symbol):
    print(120 * symbol)

# query is passed in form of a list of words (user's input words)
def search_engine(query):  
    
    print(120 * '-')
    print("Evaluating Documents....")
    print(120 * '-','\n\n')
    

    
    if len(documents) == 0:
        return 'No documents exist'
    
    #highest_score keeps track of score for each doc and best_doc stores that doc
    best_doc = ''
    highest_score = 0
    count = 0
    
    for doc in documents:
       
        print(f"Evaluating document number {count}")
        count = count+1

        doc = doc.lower() # Convert all characters to lowercase
        splitted_doc = doc.split()  # convert each doc into a list of words to make comparison
        score = 0

        for query_word in query:
            if query_word in splitted_doc:
                score += 1
        if score > highest_score:
            highest_score = score  
            best_doc = doc
        if highest_score == 0:
            return "No matching documents found."

    return best_doc

# Starting point of the project
print_border('=')
print('     MINI VECTOR SEARCH ENGINE       ')
print_border('=')


greeting_messages = ['Good morning!','Good afternoon', 'Good night'] # Will add the fn which greet users according to the time they are using this RAG.

# Taking user input
print("\n\n\nUser Query ")
query = input('>').lower() # Convert all characters to lowercase

# Do not allow users to enter empty strings 
while True:
    if len(query.strip()) == 0:
        print("Query cannot be empty ❌")
        print("\nEnter your query again.")
        query = input('>').lower() # Convert all characters to lowercase

    else:
        query = query.split() # Converting string into a list of words for word by word comparision to documents
        matched_doc = search_engine(query) # calling the earch_engine() function to match documents

        print_border('-')
        print('TOP MATCH')
        print_border('-')

        # Printing the best doc in the data set 
        print(matched_doc)
        print_border('=')
        break
        
        

