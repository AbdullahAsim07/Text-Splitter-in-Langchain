from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader("ml.pdf")
docs=loader.load()
text="""Jev Aik naya aur tez-raftar Artificial Intelligence (AI) model hai jisay TypeSafe AI ne September 2026 mein mutarif karwaya hai. Aam AI models ke bar-aks, jo lambay jumlay ya kahaniyan likhte hain, Jev ko khas tor par software systems ke andar fori aur durust faislay karne ke liye banaya gaya hai. Yeh model kisi bhi maloomat ka tajziya karke sirf chand milliseconds mein "haan ya na," mukhtalif options mein se sahi intikhab, ya rating ki soorat mein wazeh jawab deta hai. Apni is khaasiyat ki wajah se Jev ghalat maloomat (hallucinations) paida nahi karta, aur isay customer support tickets ki chhanti, spam emails rokne, aur AI agents ke kaam ko tez aur sasta banane ke liye istemal kiya jata hai.
"""
splitter=CharacterTextSplitter(
    # per chunk ka size kitne hona chahye
    chunk_size=100,
    # aik rag based ma application chunk overlap kam sa 10 hone aur zyada 20 hone chaye is sa word katte ga aur embeeding karne ma masla nhi atta hai 
    chunk_overlap=0,
    separator=''
)
result=splitter.split_text(text)
print(result)
results=splitter.split_documents(docs)
print(results)
print(results[0])
print(results[0].metadata)
print(results[0].page_content)