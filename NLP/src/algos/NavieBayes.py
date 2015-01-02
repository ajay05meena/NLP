'''
Created on Jan 2, 2015

@author: akm
'''

'''
    <li>traning data result is stored in a file using json dump </li>
    <li>Labels stores all the lablel:doccount mapping in a text file called nblabels</li> 
    <li>stores in the file nblabels.txt</li>
    <li>wordsLabel stores all the words:labels mapping in a text file called nbwords</li>
    <li> In training phase  we fills these two dictionaries for future probabilty calculation </li>
    <li> total doccount is sum of all values of labels Dictionnary
    <li> total labels is number of keys in label dictionary
    <li> total doccount for a label is value of key in labels dictionary
    <li> total word count can be calculated from words dictionary
    <li> Testing phase
    <li> probabilty of doc d exist in class c is likehood * prior probiltly
    <li> prior probabilty is probabilty of class
    <li> likehood probabilty is probabilty of word exist in this class 
    <li> Issue in this classfier is it depends on training data size it works well when data in different class is almost similiar
            as if data in two class is different than it is not classfy word correctly
    
    
'''

import json

import  util.MyTokenizer as tokenizer


try:
    labels  = json.load(open('/home/akm/Desktop/nb/nblabels.txt'))
    words   = json.load(open('/home/akm/Desktop/nb/nbwords.txt'))
except:
    labels = {}
    words = {}
def main():
    newLabel = 'english'
    text = 'good morning'
    navieBayesTrain(newLabel,text)
def navieBayesTest(word):
    global labels
    global words
    totalDocument = getTotalDocument(labels)
    for label in labels:
        allWordsInLabel = words[label]
        if word in allWordsInLabel:
            wordCountInLabel = allWordsInLabel[word]
            totalWordCount = getWordCount(words,word)
            
            priorProbabilty = float(labels[label])/float(totalDocument)
            likehoodProbabilty = float(wordCountInLabel)/float(totalWordCount)
            print 'Probabilty of word ' + str(word) + ' in class ' + str(label) + ' is ' + str(priorProbabilty*likehoodProbabilty) 
    ##json.dump(words, open('/home/akm/Desktop/nb/nbwords.txt','w'))
    ##json.dump(labels,open('/home/akm/Desktop/nb/nblabels.txt','w'))       
def getTotalDocument(paramlabels):
    total = 0
    for label in paramlabels:
        total = total + paramlabels[label]
    return total          
def getWordCount(words,wordparam):
    totalcount = 0
    for label in words:
        allwords = words[label]
        if wordparam in allwords:
            totalcount = totalcount + allwords[wordparam]
    return totalcount
def navieBayesTrain(newLabel,text):
    print "Traing started"
    registerLabel(newLabel)
    newWords = tokenizer.tokenizer(text)
    for newWord  in newWords:
        registerWords(newLabel,newWord)
    incrementLabel(newLabel)
    
def registerLabel(newLabel):
    global labels
    if newLabel not in labels:
        labels.update({newLabel:1})
def registerWords(newLabel,wordParam):
    global words
    if newLabel not in words:
        words.update({newLabel:{wordParam:1}})
    else:
        allWordsInLabel = words[newLabel]
        if wordParam not in allWordsInLabel:
            allWordsInLabel.update({wordParam:1})
        else:
            allWordsInLabel[wordParam] = allWordsInLabel[wordParam]+1
def incrementLabel(newLabel):
    global labels
    labels[newLabel] = labels[newLabel] + 1
if __name__=='__main__':
    main()