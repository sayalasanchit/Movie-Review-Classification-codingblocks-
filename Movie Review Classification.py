import joblib as jl
import clean_text as ct

# Loading
mnb=jl.load('model.pkl')
cv=jl.load('vectorizer.pkl')

# Input and prediction
Xt=[]
Xt.append(input("Enter a movie review in English: "))
Xt_clean=[ct.getStemmedReview(i) for i in Xt]
Xt_vec=cv.transform(Xt_clean).toarray()
pred=mnb.predict(Xt_vec)

if pred[0]==1:
	print('Positive review')
else:
	print('Negative review')