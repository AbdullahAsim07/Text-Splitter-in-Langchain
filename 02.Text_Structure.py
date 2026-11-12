# koi bhi text aik structure ma  organize karte hai pehle ap is text ko paragraph sa chunks ma aur chunka sa sentence ma organize karte hoo is techinque ko hum recursive text splitter technique kahte hia jaise paragraph ka liye /n/n hai aur line break ka liye /n aur chracter  ka lye "" hai '_'yeh words ka liye hai 
from langchain_text_splitters import RecursiveCharacterTextSplitter
text="""Jev Aik naya aur tez-raftar Artificial Intelligence (AI) model hai jisay TypeSafe AI ne September 2026 mein mutarif karwaya hai. Aam AI models ke bar-aks, jo lambay jumlay ya kahaniyan likhte hain, Jev ko khas tor par software systems ke andar fori aur durust faislay karne ke liye banaya gaya hai. Yeh model kisi bhi maloomat ka tajziya karke sirf chand milliseconds mein
 "haan ya na," mukhtalif options mein se sahi intikhab, ya rating ki soorat mein wazeh jawab deta hai. Apni is khaasiyat ki wajah se Jev ghalat maloomat (hallucinations) paida nahi karta, aur isay customer support tickets ki chhanti, spam emails rokne, aur AI agents ke kaam ko tez aur sasta banane ke liye istemal kiya jata hai.
"""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,

)
chunks=splitter.split_text(text)
print(chunks)
print(len(chunks))