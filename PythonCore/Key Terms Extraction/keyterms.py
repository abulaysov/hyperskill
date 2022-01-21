import nltk
from lxml import etree
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer


file_xml = etree.parse('news.xml').getroot()


def lematizer(text):
    obj = WordNetLemmatizer()
    stop_words = stopwords.words('english') + ['ha', 'wa', 'u', 'a']
    punct = list(string.punctuation)
    result = []
    for i in text:
        result.append(obj.lemmatize(i))
    for i in result:
        if i in stop_words:
            while i in result:
                result.remove(i)
        elif i in punct:
            while i in result:
                result.remove(i)
    new_result = []
    for i in result:
        if nltk.pos_tag([i])[0][1] == 'NN':
            new_result.append(i)
    return new_result


def sorted_(d: dict):
    new_dict = {}
    for i in d:
        if d[i] != 0.0:
            new_dict[i] = d[i]
    l1 = sorted(new_dict.keys(), reverse=True)
    l2 = sorted(d, key=lambda x: d[x])[-5:][::-1]
    result = []
    for i in l2:
        for j in l1:
            if d[i] == d[j]:
                result.append(i)
                break
        if len(result) == 5:
            break
    return result


def vectorizarot(dataset, terms):
    vectorizer = TfidfVectorizer(input='dataset', use_idf=True,
                                 analyzer='word', ngram_range=(1, 1))
    tfidf_matrix = vectorizer.fit_transform(dataset)
    voc = vectorizer.get_feature_names_out()
    result = []
    for i in range(10):
        d = {}
        for key, value in zip(voc, tfidf_matrix.toarray()[i]):
            d[key] = value
        tokens = sorted_(d)
        result.append(tokens)
    return {terms[i]: result[i] for i in range(10)}


def main(file_xml):
    terms_news = []
    result = []
    for i in file_xml[0]:
        tokens = nltk.tokenize.word_tokenize(i.getchildren()[1].text.lower())
        result.append(lematizer(tokens))
        terms_news.append(i.getchildren()[0].text)
    result = [' '.join(i) for i in result]
    return terms_news, result


if __name__ == '__main__':
    for i, j in vectorizarot(main(file_xml)[1], main(file_xml)[0]).items():
        print(f'{i}:')
        print(*j)
