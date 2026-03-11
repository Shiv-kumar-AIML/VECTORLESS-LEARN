from collections import defaultdict
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def build_index(sections):

    index = defaultdict(set)

    for section in sections:

        words = nltk.word_tokenize(section["content"].lower())

        for w in words:

            if w.isalpha() and w not in stop_words:
                index[w].add(section["id"])

    return index