#palwesh sahu a

import nltk
import summarizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from summarizer import summarize
#text1 = "indian bjp congress aap party democracy mla minister prime opposition cm governance cabinet candidates political government elecation cheif affers president end"
#text1 = "physics Chemistry college school science study studying coaching Maths"
text1 = "computer laptop repairs shop motherboard mouse screen monitor keyboard"
text1=text1.lower()

keyword=(word_tokenize(text1))
storiesall = input(' :')
storiesall=storiesall.lower()
data = (word_tokenize(storiesall))

#stop_words
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(storiesall)
stories = [w for w in word_tokens if not w in stop_words]
stories = []
for w in word_tokens:
    if w not in stop_words:
        stories.append(w)

title="your message"
print(summarize(title, storiesall))
#print(title)
#aa = summarize(title, storiesall)
#print(aa)
#identfying and keyword matching
keylen=len(keyword)
datalen=len(data)
print("__________________________________________________________________________________")
print("\n help related")
print("__________________________________________________________________________________")

b=0
for i in range(0,keylen):
	a=0	
	for j in range(0,datalen):
		if(keyword[i]==data[j]):
			a=a+1
			if(a>1):
				print(data[j])
				b=1
if(b==1):
	print("______________________\nComputers\n______________________")
else:
	print("other ")
