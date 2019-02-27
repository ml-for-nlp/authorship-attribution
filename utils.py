import os

def get_documents():
    documents = {}
    files = [os.path.join('./data/training/', f) for f in os.listdir('./data/training/') if os.path.isfile(os.path.join('./data/training/', f))]
    for f in files:
        #author, doc_length, words = process_document_ngrams(f,3)
        author, doc_length, words = process_document_words(f)
        documents[f] = [author, doc_length, words]
    return documents

def extract_vocab(documents):
    vocabulary = []
    for values in documents.values():
        vocabulary += list(values[2].keys())
    print("First 20 words in the vocabulary:",vocabulary[:20])
    return vocabulary

def process_document_words(filename):
    words={}
    doc_length = 0
    f=open(filename,'r', encoding='utf-8')
    c = 0
    for l in f:
        l=l.rstrip('\n')
        if c < 1:
            #print(l)
            author = l.replace("#Author: ","")
        else:
            for w in l.split():
                if w in words:
                    words[w]+=1
                else:
                    words[w]=1
                doc_length += 1
        c+=1
    f.close()
    return author, doc_length, words

def process_document_ngrams(filename, n):
    ngrams={}
    doc_length = 0
    f=open(filename,'r', encoding='utf-8')
    c = 0
    for l in f:
        l=l.rstrip('\n')
        if c < 1:
            #print(l)
            author = l.replace("#Author: ","")
        else:
            for i in range(len(l)-n):
                ngram=l[i:i+n]
                if ngram in ngrams:
                    ngrams[ngram]+=1
                else:
                    ngrams[ngram]=1
                doc_length += 1
        c+=1
    f.close()
    return author, doc_length, ngrams
