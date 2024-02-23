from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models
from nltk.tokenize import word_tokenize
import gensim
import re


class TopicModeling:

    def __init__(self, df):
        self.docs = df['title']

    def topic_modeling(self):
        texts = []
        lm = WordNetLemmatizer()

        for text in self.docs:
            text = re.sub(r'\W+', ' ', text)
            tokens = word_tokenize(text.lower())
            not_stopped_tokens = [w for w in tokens if w not in stopwords.words('english')]
            token_lemma = [lm.lemmatize(i) for i in not_stopped_tokens]
            texts.append(token_lemma)

        dictionary = corpora.Dictionary(texts)
        dictionary.filter_extremes(no_below=2, no_above=0.6)
        corpus = [dictionary.doc2bow(text) for text in texts]

        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
        print(ldamodel.print_topics(num_topics=4, num_words=5))
