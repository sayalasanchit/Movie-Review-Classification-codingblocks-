from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

# Initializing objects
tokenizer=RegexpTokenizer(r'\w+') # To extract all the words
ps=PorterStemmer()
en_stopwords=set(stopwords.words('english'))
# Removing negative words from stopwords
negative_words=["not", "won't", "wasn't", "weren't", "nor", "neither", "mustn't", "mightn't", "shouldn't", "haven't", "hasn't", "hadn't", "don't", "didn't", "shan't", "couldn't"] 
en_stopwords=[word for word in en_stopwords if word not in negative_words]

def getStemmedReview(review):
    review=review.lower()
    review=review.replace('<br/>', ' ')
    # Tokenize
    tokens=tokenizer.tokenize(review)
    filtered_tokens=[token for token in tokens if token not in en_stopwords]
    stemmed_tokens=[ps.stem(token) for token in filtered_tokens]
    stemmed_review=' '.join(stemmed_tokens)
    return stemmed_review

# Function that accepts input file and returns clean output file of movie reviews
def getStemmedDocument(inputFile, outputFile):
    out=open(outputFile, 'w', encoding="utf8")
    with open(inputFile, 'r', encoding="utf8") as f:
        reviews=f.readlines()
    for review in reviews:
        stemmed_review=getStemmedReview(review)
        print((stemmed_review), file=out)
    out.close()