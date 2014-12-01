__author__ = 'leon'
import numpy as np
import os


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
    email_list = []
    classVec = [0 for i in range(25)] + [1 for i in range(25)]

    try:
        file_no = 1
        while True:
            fr = open(dir + '/' + 'normal/' + str(file_no) + '.txt').read()
            email_list.append(fr.split())
            file_no += 1
    except IOError:
        print 'File not exist.'

    try:
        file_no = 1
        while True:
            fr = open(dir + '/' + 'spam/' + str(file_no) + '.txt').read()
            email_list.append(fr.split())
            file_no += 1
    except IOError:
        print 'File not exit.'

    return email_list, classVec


def createVocabList(dataset):
    """
    Description: create a set of all vocabularies by union all documents
    Return: a list of set of words in all emails
    """
    vocabSet = set([])
    for doc in dataset:
        vocabSet = vocabSet | set(doc)
    return list(vocabSet)


def Doc2Vec(vocabList, inputDoc):
    """
    :param vocabList: a set of all possible words
    :param inputDoc: input document to process
    :return: a vector(list) in the same size of vocabList, 1 - the word in vocablist is in inputDoc, 0 - not in inputDoc
    """
    returnVec = [0] * len(vocabList)
    for word in inputDoc:
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
    p0num = np.ones(numWords)  # vector
    p1num = np.ones(numWords)  # vector
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:  # abusive
            p1num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

    p0Vect = np.log(p0num / p0Denom)  # vector devide
    p1Vect = np.log(p1num / p1Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vect, p1Vect, pClass1):
    """
    :param vec2Classify: a list at size of the vocabulary set to classify
    :param p0Vect: gen by trainning algrithm
    :param p1Vect: gen by trainning algrithm
    :param pClass1: known value
    :return: 1 - abusive, 0 - normal
    """
    p0 = sum(vec2Classify * p0Vect) + np.log(1 - pClass1)
    p1 = sum(vec2Classify * p1Vect) + np.log(pClass1)
    if p0 > p1:
        return 0
    else:
        return 1


def test1(testDoc):
    listOfEmails, listOfClassification = loadDataSet()
    vocabList = createVocabList(listOfEmails)
    trainMatrix = []
    for email in listOfEmails:
        trainMatrix.append(Doc2Vec(vocabList, email))
    p0Vect, p1Vect, pAbusive = trainNB0(trainMatrix, listOfClassification)
    testDocVect = Doc2Vec(vocabList, testDoc)
    print testDoc, 'classified as: ', classifyNB(testDocVect, p0Vect, p1Vect, pAbusive)


def test2(testDoc):
    """
    :param testDoc: email to classify
    :return: classification result of target email
    """
    email_list, classVec = loadDataSetFromFolder(
        '/Users/cloudlite/Developer/GitHub/workspace_machine_learning/machine_learning_in_action/classifyspam/emails')
    vocabList = createVocabList(email_list)
    trainMatrix = []
    for email in email_list:
        trainMatrix.append(Doc2Vec(vocabList, email))
    p0Vect, p1Vect, pAbusive = trainNB0(trainMatrix, classVec)
    testDocVect = Doc2Vec(vocabList, testDoc)
    print testDoc
    print 'classified as: '
    if classifyNB(testDocVect, p0Vect, p1Vect, pAbusive) == 1:
        print 'Spam email.'
    else:
        print 'Normal email'


if __name__ == '__main__':
    target = "Microsoft Office Professional Plus 2007/2010 $129".split()
    test2(target)