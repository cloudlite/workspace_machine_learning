__author__ = 'leon'

from numpy import *


def loadDataSet():
    """ Sample data set """
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],  # abusive
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],  # abusive
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]  # abusive
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive
    return postingList, classVec


def loadDataSetFromFolder(dir):
    """
    Return: list of emails, class vector of each email
    """
    # TODO: load emails
    # TODO: abused email, normal email


def createVocabList(dataset):
    """
    Description: create a set of all vocabularies by union all documents
    Return: a list of set of words in all emails
    """
    vocabSet = set([])
    for doc in dataset:
        vocabSet = vocabSet | set(doc)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    """
    :param vocabList: a set of all possible words
    :param inputSet: input document to process
    :return: a vector(list) in the same size of vocabList, 1 - the word in vocablist is in inputSet, 0 - not in inputSet
    """
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print 'the word: %s is not in my vocabulary!' % word
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    """
    :param trainMatrix: list of vectors, each vector represents a vocab list in which 1 means the word is in email
    :param trainCategory: a classification vector represents whether the email is abusive
    :return: p0V: if email is not abusive, conditional probability of each word,
             p1V: if email is abusive, conditional probability of each word
             pAb: percentage of abusive emails out of all emails
    """
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])

    pAbusive = sum(trainCategory) / float(numTrainDocs)  # probability of abusive emails
    p0num = zeros(numWords)  # vector
    p1num = zeros(numWords)  # vector
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:  # abusive
            p1num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

    p0Vect = math.log(p0num / p0Denom)  # vector devide
    p1Vect = math.log(p1num / p1Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vect, p1Vect, pClass1):
    """
    :param vec2Classify: a list at size of the vocabulary set to classify
    :param p0Vect: gen by trainning algrithm
    :param p1Vect: gen by trainning algrithm
    :param pClass1: known value
    :return: 1 - abusive, 0 - normal
    """
    p0 = sum(vec2Classify * p0Vect) + math.log(1 - pClass1)
    p1 = sum(vec2Classify * p1Vect) + math.log(pClass1)
    if p0 > p1:
        return 0
    else:
        return 1


def test1():
    listOfEmails, listOfClasses = loadDataSet()


if __name__ == '__main__':
    test1()

