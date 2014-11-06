__author__ = 'leon'

import bayes as bayes

mySent = 'This book is the best book on Python or M.L. I have ever laid eyes upon.'


def textparse(bigstring):
    import re

    list_of_tokens = re.split(r'\W*', bigstring)
    return [token.lower() for token in list_of_tokens if len(token) > 0]


def spamtest():
    doclist = []
    classlist = []
    fulltext = []
    for i in range(1, 26):  # size of training set
        wordlist = textParse(open('email/spam/%d.txt' % i).read())
        doclist.append(wordlist)
        fulltext.extend(wordlist)
        classlist.append(1)

        wordlist = textParse(open('email/ham/%d.txt' % i).read())
        doclist.append(wordlist)
        fulltext.extend(wordlist)
        classlist.append(0)

    vocab_list = createVocabList(doclist)
    trainingset = range(50)
    testset = []
    for i in range(10):
        randindex = int(random.uniform(0, len(trainingset)))
        testset.append(trainingset[randindex])
        del (trainingset[randindex])

    trainmat = [];
    trainclasses = []
    for docIndex in trainingset:
        trainmat.append(setOfWords2Vec(vocab_list, doclist[docIndex]))
        trainclasses.append(classlist[docIndex])

    p0v, p1v, pspam = trainNB0(array(trainmat), array(trainclasses))
    errorcount = 0

    for docIndex in testset:
        wordvector = setOfWords2Vec(vocab_list, doclist[docIndex])
        if classifyNB(array(wordvector), p0v, p1v, pspam) != classlist[docIndex]:
            errorcount += 1
    print 'the error rate is: ', float(errorcount) / len(testset)


listOPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
trainMat = []
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))

print trainMat
p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
print p0V
print p1V
print pAb