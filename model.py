from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')

nltk.download('punkt')

def tokenize(value_type, value):
    if(value_type == 'url'):
        article = Article(value)
        article.download()
        article.parse()
        article.nlp()
        corpus = article.text   
    elif(value_type == 'text'):
        corpus=value
    sentence_list = nltk.sent_tokenize(corpus)
    return sentence_list

def bot_response(user_input, sentence_list):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ' '
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_score = cosine_similarity(cm[-1], cm)
    sentence_list.pop()
    similarity_score_list = similarity_score.flatten()   
    sorted_similarity_score_list = sorted(similarity_score_list, reverse=True)    
    sorted_similarity_score_list = sorted_similarity_score_list[1:]
    answer_index = np.where(similarity_score_list==sorted_similarity_score_list[0])[0][0]
    answer = sentence_list[answer_index]
    return answer

sentence_list = tokenize('url','https://www.internetsociety.org/resources/doc/2017/artificial-intelligence-and-machine-learning-policy-paper/?gclid=CjwKCAjwiaX8BRBZEiwAQQxGx0qpU6qYi2LRF8bPdQZFxTR2e1EXuLQGMBML5m6NUk7WqOefCuRGfRoCDegQAvD_BwE')
