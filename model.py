import clean_text as ct
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import joblib as jl

# Loading
df=pd.read_csv('Train.csv')
df=df.sample(frac=0.1) # Shuffling and slicing
X=df['review'].values
Y=[1 if x=='pos' else 0 for x in df['label'].values]

# Stemming and Vectorization
X_clean=[ct.getStemmedReview(i) for i in X]
cv=CountVectorizer()
X_vec=cv.fit_transform(X_clean).toarray()

# Training
from sklearn.naive_bayes import MultinomialNB
mnb=MultinomialNB()
mnb.fit(X_vec, Y)

# Dumping
jl.dump(mnb, 'model.pkl')
jl.dump(cv, 'vectorizer.pkl')