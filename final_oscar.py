text_oscar = "The Artificial Intelligence field has played an amazing role in the world’s society the past decade. We ca attribute this to the researchers whom have dedicated their time and efforts to advance the field. Their contributions in the fields of NLP, computer vision, medical research and many others. I would love to have a role in it."

import nltk

tokenized_words = nltk.word_tokenize(text_oscar)

stop_words = set(nltk.corpus.stopwords.words('english'))
wordslist_oscar = [w for w in tokenized_words if not w in stop_words]

tagged_POS = nltk.pos_tag(wordslist_oscar)

print(tagged_POS)