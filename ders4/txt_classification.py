import nltk
from collections import Counter
from string import punctuation
from snowballstemmer import stemmer

text = "Doğum yardımlarının kapsamı genişletiliyor. İkiz, üçüz, dördüz gibi çoklu doğum yapan ihtiyaç sahibi anneler için 'Muhtaç Ailelere Çoklu Doğum Yardımı' programı başlatılıyor. Aile ve Sosyal Politikalar Bakanlığı, annelere ikiz ve üzeri çocukları için çocuk başına aylık 150 lira ödeme yapılacak."

def to_split(s):
    return s.split()

def to_lower(s):
    return s.lower()

def to_punctuate(s):
    return "".join(c for c in s if c not in punctuation)

def to_filter_stopwords(kelimeler):
    stop_word_list = nltk.corpus.stopwords.words("turkish")
    return [kelime for kelime in kelimeler if kelime not in stop_word_list ]

def to_tokenize(s):
    wpt = nltk.WordPunctTokenizer()
    kelimeler = wpt.tokenize(s)
    kelimeler = to_filter_stopwords(kelimeler)
    # text = " ".join(kelimeler)
    return kelimeler

def to_stem(kelimeler):
    stem_find = stemmer("turkish")
    stems = stem_find.stemWords(kelimeler)
    print(stems)

# kelimeler = to_split(to_lower(text))
# kelime_sayilari = Counter(kelimeler)
# print(len(kelimeler))
# kelimeler = to_filter_stopwords(kelimeler)
# print(len(kelimeler))

kelimeler = to_tokenize(to_punctuate(text))
to_stem(kelimeler)
