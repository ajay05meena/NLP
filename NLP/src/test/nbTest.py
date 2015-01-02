'''
Created on Jan 2, 2015

@author: akm
language detector 
'''

import algos.NavieBayes as nb
import json


def trainNBfromFiles():
    lines  =  open('/home/akm/Desktop/nb/train/en.txt','r')
    for line in lines:
        try:
            nb.navieBayesTrain('English',line)
        except:
            print line
    json.dump(nb.words, open('/home/akm/Desktop/nb/nbwords.txt','w'))
    json.dump(nb.labels,open('/home/akm/Desktop/nb/nblabels.txt','w'))
def main():
    ##trainNBfromFiles()
    testNB('aussi')
def testNB(word):
    nb.navieBayesTest(word)
if __name__=='__main__':
    main()