import sys
import os
import math
from utils import process_document_words, process_document_ngrams, get_documents, extract_vocab


alpha = 0.0001
classes = ["Austen", "Carroll", "Grahame", "Kipling"]
documents = get_documents()

def count_docs(documents):
    return len(documents)

def count_docs_in_class(documents, c):
    count=0
    for values in documents.values():
        if values[0] == c:
            count+=1
    return count

def concatenate_text_of_all_docs_in_class(documents,c):
    words_in_class = {}
    for d,values in documents.items():
        if values[0] == c:
            words_in_class.update(values[2])
    return words_in_class

def train_naive_bayes(classes, documents):
    vocabulary = extract_vocab(documents)
    conditional_probabilities = {}
    for t in vocabulary:
        conditional_probabilities[t] = {}
    priors = {}
    print("\n\n***\nCalculating priors and conditional probabilities for each class...\n***")
    for c in classes:
         priors[c] = count_docs_in_class(documents,c) / count_docs(documents)
         print("\nPrior for",c,priors[c])
         class_size = count_docs_in_class(documents, c)
         print("In class",c,"we have",class_size,"document(s).")
         words_in_class = concatenate_text_of_all_docs_in_class(documents,c)
         #print(c,words_in_class)
         print("Calculating conditional probabilities for the vocabulary.")
         denominator = sum(words_in_class.values())
         for t in vocabulary:
             if t in words_in_class:
                 conditional_probabilities[t][c] = (words_in_class[t] + alpha) / (denominator * (1 + alpha))
                 #print(t,c,words_in_class[t],denominator,conditional_probabilities[t][c])
             else:
                 conditional_probabilities[t][c] = (0 + alpha) / (denominator * (1 + alpha))
    return vocabulary, priors, conditional_probabilities

def apply_naive_bayes(classes, vocabulary, priors, conditional_probabilities, test_document):
    scores = {}
    #author, doc_length, words = process_document_ngrams(test_document,3)
    author, doc_length, words = process_document_words(test_document)
    for c in classes:
        scores[c] = math.log(priors[c])
        for t in words:
            if t in conditional_probabilities:
                for i in range(words[t]):
                    scores[c] += math.log(conditional_probabilities[t][c])
    print("\n\nNow printing scores in descending order:")
    for author in sorted(scores, key=scores.get, reverse=True):
        print(author,"score:",scores[author])

vocabulary, priors, conditional_probabilities = train_naive_bayes(classes, documents)
apply_naive_bayes(classes, vocabulary, priors, conditional_probabilities, sys.argv[1])
