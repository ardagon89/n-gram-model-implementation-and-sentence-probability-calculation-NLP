#!/usr/bin/env python
# coding: utf-8

# In[46]:


def get_tokens_words(filename):
    file1 = open(filename,"r")
    tokenslist = []
    wordslist = []
    for line in file1.readlines():
        tokenslist.append(line.split())
        wordslist.append([token.split('_')[0].lower() for token in line.split()])
        
    return tokenslist, wordslist

def get_unigram_count(wordslist):
    unigram_count = {}
    total_tokens = 0
    for line in wordslist:
        for word in line:
            if word not in unigram_count:
                unigram_count[word] = 1
            else:
                unigram_count[word] += 1
        total_tokens += len(line)
        
    return unigram_count, total_tokens

def get_unigram_prob(unigram_count, total_tokens):
    unigram_prob = {}
    for key in unigram_count:
        unigram_prob[key] = unigram_count[key]/total_tokens
    
    return unigram_prob

def get_bigram_count(wordslist):
    bigram_count = {}
    for line in wordslist:
        for i in range(1, len(line)):
            if (line[i-1], line[i]) not in bigram_count:
                bigram_count[(line[i-1], line[i])] = 1
            else:
                bigram_count[(line[i-1], line[i])] += 1
    
    return bigram_count

def get_bigram_prob(bigram_count, unigram_count, wordslist):
    bigram_prob = {}
    for key in bigram_count:
        bigram_prob[key] = bigram_count[key]/unigram_count[key[0]]
    total_bigrams = sum([len(line)-1 for line in wordslist])
    
    return bigram_prob, total_bigrams

def get_bigram_laplace_prob(bigram_count, unigram_count, word_count_V):
    bigram_laplace_prob = {}
    for key in bigram_count:
        bigram_laplace_prob[key] = (bigram_count[key]+1)/(unigram_count[key[0]]+word_count_V)
        
    return bigram_laplace_prob

def get_no_smooth_prob(sentence, unigram_prob, bigram_prob):
    no_smooth_prob = 1
    for i in range(len(sentence)):
        if i==0:
            if sentence[i] in unigram_prob:
                no_smooth_prob *= unigram_prob[sentence[i]]
                print(sentence[i]+':'+str(unigram_prob[sentence[i]]))
            else:
                no_smooth_prob = 0
                print(sentence[i]+':'+str(0))
        else:
            if (sentence[i-1], sentence[i]) in bigram_prob:
                no_smooth_prob *= bigram_prob[(sentence[i-1], sentence[i])]
                print(str((sentence[i-1], sentence[i]))+':'+str(bigram_prob[(sentence[i-1], sentence[i])]))
            else:
                no_smooth_prob = 0
                print(str((sentence[i-1], sentence[i]))+':'+str(0))
    print()
    return no_smooth_prob

def get_laplace_smooth_prob(sentence, unigram_prob, bigram_laplace_prob, unigram_count, word_count_V):
    laplace_smooth_prob = 1
    for i in range(len(sentence)):
        if i==0:
            if sentence[i] in unigram_prob:
                laplace_smooth_prob *= unigram_prob[sentence[i]]
                print(sentence[i]+':'+str(unigram_prob[sentence[i]]))
            else:
                laplace_smooth_prob = 0
                print(sentence[i]+':'+str(0))
        else:
            if (sentence[i-1], sentence[i]) in bigram_laplace_prob:
                laplace_smooth_prob *= bigram_laplace_prob[(sentence[i-1], sentence[i])]
                print(str((sentence[i-1], sentence[i]))+':'+str(bigram_laplace_prob[(sentence[i-1], sentence[i])]))
            else:
                laplace_smooth_prob *=  1/(unigram_count[sentence[i-1]]+word_count_V)
                print(str((sentence[i-1], sentence[i]))+':'+str(1/(unigram_count[sentence[i-1]]+word_count_V)))
    print()
    return laplace_smooth_prob

def get_N_c(bigram_count):
    N_c={}
    for key in bigram_count:
        if bigram_count[key] in N_c:
            N_c[bigram_count[key]].append(key)
        else:
            N_c[bigram_count[key]] = [key]
            
    return N_c

def get_cstar_pstar(N_c, total_bigrams):
    c_star = {}
    p_star = {}
    p_star[0] = len(N_c[1])/total_bigrams
    for key in N_c:
        if key+1 in N_c:
            c_star[key] = (key+1)*len(N_c[key+1])/len(N_c[key])
        else:
            c_star[key] = 0
        p_star[key] = c_star[key]/total_bigrams
        
    return c_star, p_star

def get_GT_smooth_prob(sentence, unigram_prob, bigram_count, p_star):
    GT_smooth_prob = 1
    for i in range(len(sentence)):
        if i==0:
            if sentence[i] in unigram_prob:
                GT_smooth_prob *= unigram_prob[sentence[i]]
                print(sentence[i]+':'+str(unigram_prob[sentence[i]]))
            else:
                GT_smooth_prob = 0
                print(sentence[i]+':'+str(0))
        else:
            if (sentence[i-1], sentence[i]) in bigram_count:
                GT_smooth_prob *= p_star[bigram_count[(sentence[i-1], sentence[i])]]
                print(str((sentence[i-1], sentence[i]))+':'+str(p_star[bigram_count[(sentence[i-1], sentence[i])]]))
            else:
                GT_smooth_prob *=  p_star[0]
                print(str((sentence[i-1], sentence[i]))+':'+str(p_star[0]))
    print()
    return GT_smooth_prob

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        tokenslist, wordslist = get_tokens_words("NLP6320_POSTaggedTrainingSet-Windows.txt")
        unigram_count, total_tokens = get_unigram_count(wordslist)
        unigram_prob = get_unigram_prob(unigram_count, total_tokens)
        bigram_count = get_bigram_count(wordslist)
        bigram_prob, total_bigrams = get_bigram_prob(bigram_count, unigram_count, wordslist)
        word_count_V = len(unigram_count)
        bigram_laplace_prob = get_bigram_laplace_prob(bigram_count, unigram_count, word_count_V)
        sentence = 'The standard Turbo engine is hard to work'.lower().split()
        print()
        no_smooth_prob = get_no_smooth_prob(sentence, unigram_prob, bigram_prob)
        print('No smoothed prob:',no_smooth_prob)
        print()
        laplace_smooth_prob = get_laplace_smooth_prob(sentence, unigram_prob, bigram_laplace_prob, unigram_count, word_count_V)
        print('Laplace smoothed prob:',laplace_smooth_prob)
        N_c = get_N_c(bigram_count)
        possible_bigrams = word_count_V**2
        c_star, p_star = get_cstar_pstar(N_c, total_bigrams)
        print()
        GT_smooth_prob = get_GT_smooth_prob(sentence, unigram_prob, bigram_count, p_star)
        print('Good Turing prob:',GT_smooth_prob)
    elif len(sys.argv) == 2:
        tokenslist, wordslist = get_tokens_words(sys.argv[1])
        unigram_count, total_tokens = get_unigram_count(wordslist)
        unigram_prob = get_unigram_prob(unigram_count, total_tokens)
        bigram_count = get_bigram_count(wordslist)
        bigram_prob, total_bigrams = get_bigram_prob(bigram_count, unigram_count, wordslist)
        word_count_V = len(unigram_count)
        bigram_laplace_prob = get_bigram_laplace_prob(bigram_count, unigram_count, word_count_V)
        sentence = 'The standard Turbo engine is hard to work'.lower().split()
        print()
        no_smooth_prob = get_no_smooth_prob(sentence, unigram_prob, bigram_prob)
        print('No smoothed prob:',no_smooth_prob)
        print()
        laplace_smooth_prob = get_laplace_smooth_prob(sentence, unigram_prob, bigram_laplace_prob, unigram_count, word_count_V)
        print('Laplace smoothed prob:',laplace_smooth_prob)
        N_c = get_N_c(bigram_count)
        possible_bigrams = word_count_V**2
        c_star, p_star = get_cstar_pstar(N_c, total_bigrams)
        print()
        GT_smooth_prob = get_GT_smooth_prob(sentence, unigram_prob, bigram_count, p_star)
        print('Good Turing prob:',GT_smooth_prob)
    elif len(sys.argv) == 3:
        tokenslist, wordslist = get_tokens_words(sys.argv[1])
        unigram_count, total_tokens = get_unigram_count(wordslist)
        unigram_prob = get_unigram_prob(unigram_count, total_tokens)
        bigram_count = get_bigram_count(wordslist)
        bigram_prob, total_bigrams = get_bigram_prob(bigram_count, unigram_count, wordslist)
        word_count_V = len(unigram_count)
        bigram_laplace_prob = get_bigram_laplace_prob(bigram_count, unigram_count, word_count_V)
        sentence = 'The standard Turbo engine is hard to work'.lower().split()
        if sys.argv[2] == 'NS':
            print()
            no_smooth_prob = get_no_smooth_prob(sentence, unigram_prob, bigram_prob)
            print('No smoothed prob:',no_smooth_prob)
        elif sys.argv[2] == 'LS':
            print()
            laplace_smooth_prob = get_laplace_smooth_prob(sentence, unigram_prob, bigram_laplace_prob, unigram_count, word_count_V)
            print('Laplace smoothed prob:',laplace_smooth_prob)
        elif sys.argv[2] == 'GTS':
            N_c = get_N_c(bigram_count)
            possible_bigrams = word_count_V**2
            c_star, p_star = get_cstar_pstar(N_c, total_bigrams)
            print()
            GT_smooth_prob = get_GT_smooth_prob(sentence, unigram_prob, bigram_count, p_star)
            print('Good Turing prob:',GT_smooth_prob)
        else:
            print('Wrong input. Enter correct smoothing code.')
    else:
        print('Wrong number of arguments provided. Enter correct arguments.')
