import codecs
import glob
import re
# Python program to find the k most frequent words 
# from data set 
from collections import Counter 
import pandas as pd
import matplotlib.pyplot as plt

def wordcountf(file):
    wordsInFile = codecs.open(file, encoding='utf-8') #'open' words in file
    words = wordsInFile.read().split() # reads them
    return len(words)
    
def uniquef(file):
    wordsInFile = codecs.open(file, encoding='utf-8') #'open' words in file
    words = wordsInFile.read().split() # reads them, separated by space
    unique = set(words)
    return round((float(len(unique))/len(words)), 2)

# This is just 1 - uniquef.
def repeatedf(file):
    wordsInFile = codecs.open(file, encoding='utf-8') #'open' words in file
    words = wordsInFile.read().split() # reads them, separated by space
    unique = set(words)
    return round(1 - (float(len(unique))/len(words)), 2)

# The following code is from Jadzia626's answer on
#  https://stackoverflow.com/questions/405161/detecting-syllables-in-a-word
def syllables(theText):    
  #  theText = codecs.open(file)
    cleanText = ""
    for ch in theText:
        if ch in "abcdefghijklmnopqrstuvwxyz'’":
            cleanText += ch
        else:
            cleanText += " "

    vowels   = "aeiouy'’"
    dExep    = ("ei","ie","ua","ia","eo")
    theWords = cleanText.lower().split()
    allSylls = 0
    for inWord in theWords:
        nChar  = len(inWord)
        nSyll  = 0
        wasVow = False
        wasY   = False
        if nChar == 0:
            continue
        if inWord[0] in vowels:
            nSyll += 1
            wasVow = True
            wasY   = inWord[0] == "y"
        for c in range(1,nChar):
            isVow  = False
            if inWord[c] in vowels:
                nSyll += 1
                isVow = True
            if isVow and wasVow:
                nSyll -= 1
            if isVow and wasY:
                nSyll -= 1
            if inWord[c:c+2] in dExep:
                nSyll += 1
            wasVow = isVow
            wasY   = inWord[c] == "y"
        if inWord.endswith(("e")):
            nSyll -= 1
        if inWord.endswith(("le","ea","io")):
            nSyll += 1
        if nSyll < 1:
            nSyll = 1
        # print("%-15s: %d" % (inWord,nSyll))
        allSylls += nSyll
    if len(theWords) > 0:
      return allSylls/len(theWords)
    return 0 
    #this is if len(theWords <= 0), which means that when calclating the average we need to make sure we're not counting the 0 values.


#The following function is from D Greenberg's answer on
#https://stackoverflow.com/questions/4576077/python-split-text-on-sentences

def split_into_sentences(text):
  alphabets= "([A-Za-z])"
  prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
  suffixes = "(Inc|Ltd|Jr|Sr|Co)"
  starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
  acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
  websites = "[.](com|net|org|io|gov)"
  text = " " + text + "  "
  text = text.replace("\n"," ")
  text = re.sub(prefixes,"\\1<prd>",text)
  text = re.sub(websites,"<prd>\\1",text)
  if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
  text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
  text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
  text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
  text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
  text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
  text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
  text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
  if "”" in text: text = text.replace(".”","”.")
  if "\"" in text: text = text.replace(".\"","\".")
  if "!" in text: text = text.replace("!\"","\"!")
  if "?" in text: text = text.replace("?\"","\"?")
  text = text.replace(".",".<stop>")
  text = text.replace("?","?<stop>")
  text = text.replace("!","!<stop>")
  text = text.replace("<prd>",".")
  sentences = text.split("<stop>")
  sentences = sentences[:-1]
  sentences = [s.strip() for s in sentences]
  return sentences

#returns an array of the flesch scores for each of the articles in folderName
def flesch(folderName):
  artSylls = [] #(avg # of syllables per word) per article
  artSenLen = [] #avg sentence length per article
  fleschArticles = []

  for filepath in glob.glob(folderName):
    #print(filepath)
    articleFILE = codecs.open(filepath)
    read = articleFILE.read()
    sentences = split_into_sentences(read)
    numOfWords = 0
    for i in range(len(sentences)):
      numOfWords += len(sentences[i].split(" "))
    artSenLen += [numOfWords / len(sentences)]

    articleWORDS = []
    for word in read.split():
      articleWORDS += word + " "
    artSylls += [syllables(articleWORDS)]
  
  #print(artSylls) #this array contains the avg number of syllables per word in each of the NYT articles
  NYTarticlesAvgSylls = sum(artSylls)/len(artSylls)
  #print("avg syllables per word per article: " + str(NYTarticlesAvgSylls))
  #print(artSenLen)
  #print(len(artSylls) == len(artSenLen))
 
  for i in range(len(artSylls)):
    fleschArticles += [206.835 - (1.015 * artSenLen[i]) - (84.6 * artSylls[i])]
  #print("FLESCH ARTICLES!!!!! " + str(fleschArticles))
  return fleschArticles

def unique_words(folderName):
  uniquePercentages = []
  for filepath in glob.glob(folderName):
    wordsInFile = codecs.open(filepath)
    words = wordsInFile.read().split()
    unique = set(words)
    uniquePercentages += [round((float(len(unique))/len(words)), 2)]
  return uniquePercentages

#This returns a collection of the k most frequent words in the files in 
#"foldername" that have more than minLen letters
def word_frequencies(foldername, k, minLen):
   #via https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
    data_set = []
    for filepath in glob.glob(foldername):
      wordsInFile = codecs.open(filepath)
      words = wordsInFile.read().lower().split()
      #print("ahem")
      #print(words)
      #correctedWords = []
      i = 0
      for word in words:
        #following via
        #https://towardsdatascience.com/very-simple-python-script-for-extracting-most-common-words-from-a-story-1e3570d0b9d0
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        word = word.replace("?","")
        word = word.replace("''", "")
        #correctedWords += word
        #if len(word) < minLen:
         # continue
        words[i] = word
        i += 1

        #if len(word) < minLen:
         # words.remove(word)
    
      data_set += words
    #print(data_set)
  
    # split() returns list of all the words in the string 
    #split_it = data_set.split() 
  
    # Pass the split_it list to instance of Counter class. 
    counter = Counter(data_set) 
   # del counter["something"]
   # for word in counter:
    #  print(word + str(counter[word]))
    updated = Counter()
    for word in counter.keys():
      if len(word) >= minLen:
        updated[word] = counter[word]
    # most_common() produces k frequently encountered 
    # input values and their respective counts. 
    #return counter.most_common(k)
    return updated.most_common(k)


#This returns a set of all words in the files of a folder "foldername".
def set_of_words(foldername):
  #via https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
  data_set = []
  for filepath in glob.glob(foldername):
    wordsInFile = codecs.open(filepath)
    words = wordsInFile.read().lower().split()
    #print("ahem")
    #print(words)
    #correctedWords = []
    i = 0
    for word in words:
      #following via
      #https://towardsdatascience.com/very-simple-python-script-for-extracting-most-common-words-from-a-story-1e3570d0b9d0
      word = word.replace(".","")
      word = word.replace(",","")
      word = word.replace(":","")
      word = word.replace("\"","")
      word = word.replace("!","")
      word = word.replace("â€œ","")
      word = word.replace("â€˜","")
      word = word.replace("*","")
      word = word.replace("?","")
      word = word.replace("''", "")
      #correctedWords += word
      #if len(word) < minLen:
       # continue
      words[i] = word
      i += 1
    
    data_set += words
  #print(data_set)
  return set(data_set)

def _main():

  #sentences = split_into_sentences(codecs.open('test.txt').read())
  #print(sentences)
  #print(len(sentences))
  #print(sentences[0].split())
  #print(len(sentences[0].split()))
  #for s in sentences:
    #print(len(s.split()))
  avgSenLens = []
  for filepath in glob.glob("WashPost/*/*.txt"):
    sentences = split_into_sentences(codecs.open(filepath).read())
    currFile_avgSenLen = []
    for s in sentences:
      #print(len(s.split()))
      currFile_avgSenLen += [len(s.split())]
    #print(currFile_avgSenLen)
    avgSenLens += [sum(currFile_avgSenLen)/len(currFile_avgSenLen)]
  #print(len(avgSenLens))
  print(sum(avgSenLens)/len(avgSenLens))
  

  common = word_frequencies("AllArtsAndEds/*/*.txt", 100, 4)
  #print(common)
 # print(common)
  #NOW PLOT COMMON
  #print(set_of_words("testing/*.txt"))
  articleCorpus = set_of_words("AllArticles/*/*.txt")
  editorialCorpus = set_of_words("AllEditorials/*/*.txt")
  NYTCorpus = set_of_words("NYT/*/*.txt")
  BGCorpus = set_of_words("BostGl/*/*.txt")
  WPCorpus = set_of_words("WashPost/*/*.txt")

  #print(len(articleCorpus))
  #print(len(editorialCorpus))
  inArticlesOnly = articleCorpus - editorialCorpus
  #print(len(inArticlesOnly))
  inEditorialsOnly = editorialCorpus - articleCorpus
  #print(len(inEditorialsOnly))
  inNYTOnly = NYTCorpus - BGCorpus - WPCorpus
  #print(len(inNYTOnly))
  inBGOnly = BGCorpus - NYTCorpus - WPCorpus
  #print(len(inBGOnly))
  inWPOnly = WPCorpus - BGCorpus - NYTCorpus
  #print(len(inWPOnly))
  #total num of words = 55005


  #numOfWordsInArticles = len(allwords) this is 31841
  #num of words in editorials = 23164
  #num of words in BG = 19722
  #in BG Articles = 10323
  #in BG Editorials = 9399
  #num of words in NYT = 17538
  #num of words in NYT Articles = 10155
  #num of words in NYT Editorials = 7383
  #num of words in WP = 17745
  #in WP Articles = 11363
  #in WP Editorials = 6382

  


  #Percentage of unique words for each group:
  #editorialsUnique = unique_words("AllEditorials/*/*.txt")
  #print(editorialsUnique)
  #this is [0.61, 0.57, 0.56, 0.59, 0.59, 0.58, 0.62, 0.6, 0.54, 0.53, 0.63, 0.53, 0.57, 0.59, 0.61, 0.6, 0.53, 0.6, 0.58, 0.57, 0.62, 0.61, 0.59, 0.62, 0.55, 0.62, 0.6, 0.57,0.56, 0.52, 0.57, 0.57, 0.6, 0.55, 0.55, 0.64]
  #articlesUnique = unique_words("AllArticles/*/*.txt")
  #print(articlesUnique)
  # this is [0.56, 0.54, 0.56, 0.52, 0.65, 0.66, 0.57, 0.57, 0.51,0.58, 0.55, 0.53, 0.53, 0.54, 0.61, 0.58, 0.54, 0.48, 0.58, 0.55, 0.58, 0.58, 0.54, 0.55, 0.51, 0.59, 0.46, 0.66, 0.49, 0.54, 0.54, 0.58, 0.55, 0.51, 0.6, 0.62]
  #NYTUnique = unique_words("NYT/*/*.txt")
  #NYTArtUnique = unique_words("AllArticles/20NYTArt/*.txt")
  #NYTEdUnique = unique_words("AllEditorials/21NYTEd/*.txt")
  #WPUnique = unique_words("WashPost/*/*.txt")
  #WPArtUnique = unique_words("AllArticles/30WashPostArt/*.txt")
  #WPEdUnique = unique_words("AllEditorials/31WashPostEd/*.txt")
  #BGUnique = unique_words("BostGl/*/*.txt")
  #BGArtUnique =  unique_words("AllArticles/10BostGlArt/*.txt")
  #BGEdUnique =  unique_words("AllEditorials/11BostGlEd/*.txt")

  
  #for word in test.read().split():
    #print(word)
    #sentences += word + " "
  #print("sentences: " + sentences)
  #print("avg syllables of test.txt: " + str(syllables(sentences)))

 # flesch("AllArtsAndEds/BGArt/*.txt")


  #The following are the flesch readability scores per article
  #in each newspaper's articles/editorials
  #these were already calculated using the flesch() function.


  BGArtFLESCH = [65.73733253364323, 31.17559511434513, 54.91958649719382, 75.05713724164168, 53.09729455709714, 28.3745271629779, 31.638799992482348, 63.218393586492795, 56.31988297793299, 54.0694970161978, 28.170187908496757, 42.87420493341128]
  
  BGEdFLESCH = [54.949984805984116, 43.431414603960434, 44.43590163934428, 34.44680962757528, 32.44274514200299, 50.964908175069894, 60.882937710437744, 27.216678122863215, 57.77308139021375, 32.03633210332106, 47.57773494860501, 52.673898457684174]
  
  #Average Flesch score for the Boston Globe:
  #fleschBG = (sum(BGArtFLESCH) + sum(BGEdFLESCH))/(len(BGArtFLESCH) + len(BGEdFLESCH))
  #print("bg flesch " + str(fleschBG)) #THIS IS 46.81186942704062
  
  #Average Flesch score for BG Articles only
  #fleschBGArt = (sum(BGArtFLESCH))/len(BGArtFLESCH)
  #print("fleschBGP art: " + str(fleschBGArt)) #THIS IS 48.72103662682608

   #Average Flesch score for BG Editorials only
  #fleschBGED = (sum(BGEdFLESCH))/len(BGEdFLESCH)
  #print("flesch BG ed: " + str(fleschBGED)) #this is 44.90270222725517


  NYTArtFLESCH = [36.05410234614078, 35.9335214785215, 36.72083333333336, 59.75238242647936, 28.200202794819376, 46.17216152945767, 40.71401062363151, 37.553146302034236, 61.25693181818184, 55.568579785909876, 46.97833835275634, 56.90929844097997]
  NYTEdFLESCH = [27.73693954659953, 52.711472805202504, 40.98621012658228, 42.95604269972455, 40.23683639633569, 35.480228375677996, 27.870275601766167, 39.04289308176104, 54.06586842105264, 34.59676790950988, 42.20628920863314,41.97984277799381]

  #Average Flesch score for NYT:
  #fleschNYT = (sum(NYTArtFLESCH) + sum(NYTEdFLESCH))/(len(NYTArtFLESCH) + len(NYTEdFLESCH))
  #print("NYT Flesch" + str(fleschNYT)) #THIS IS 42.57013234096188

  #Average Flesch score for NYT Articles only
  #fleschNYTArt = (sum(NYTArtFLESCH))/len(NYTArtFLESCH)
  #print("flesch nyt art: " + str(fleschNYTArt)) #this is 45.151125769353825
  #fleschNYTED = (sum(NYTEdFLESCH))/len(NYTEdFLESCH)

  #Average Flesch scores for NYT Editorials only
  #print("flesch nyt ed: " + str(fleschNYTED)) #this is 39.98913891256993


  WPArtFLESCH = [44.891600101295154, 45.63042271335377, 45.06408424908429, 40.82797123623013, 31.867047522750283, 60.86585495701557, 50.94425407925411, 38.758395252838, 33.15309128025666, 41.969657408947285, 42.33668564816506, 57.6761259338314]
  WPEdFLESCH = [39.7529284369115, 40.16899156885438, 39.3021424829754, 45.86320312500001, 25.140715996805966, 37.59338267322744, 48.4234454734455, 29.214325699745558, 25.348675605340617, 18.792806347930906, 47.939624329159216, 42.3256102540835]

  #Average Flesch scores for WP:
  #fleschWP = (sum(WPArtFLESCH) + sum(WPEdFLESCH))/(len(WPArtFLESCH) + len(WPEdFLESCH))
  #print("WP Flesch " + str(fleschWP)) #THIS IS 40.57712676568757

  #Average Flesch scores for WP articles only:
  #fleschWPArt = (sum(WPArtFLESCH))/len(WPArtFLESCH)
  #print("flesch WP art: " + str(fleschWPArt)) #THIS IS 44.498765865251805

  #Average Flesch scores for WP editorials only:
  #fleschWPED = (sum(WPEdFLESCH))/len(WPEdFLESCH)
  #print("flesch WP ed: " + str(fleschWPED)) #this is 36.65548766612333

  #Average Flesch scores for all articles, editorials, newspapers:
  #FLESCHofALL = (sum(BGArtFLESCH) + sum(BGEdFLESCH) + sum(NYTArtFLESCH) + sum(NYTEdFLESCH) + sum(WPArtFLESCH) + sum (WPEdFLESCH)) / (len(BGArtFLESCH) + len(BGEdFLESCH) + len(NYTArtFLESCH) + len(NYTEdFLESCH) + len(WPArtFLESCH) + len (WPEdFLESCH))
  #print(FLESCHofALL) #this is 43.319709511230016

  #Average Flesch scores for all editorials 
  #editorialsFLESCH = (sum(BGEdFLESCH) + sum(NYTEdFLESCH) + sum (WPEdFLESCH)) / (len(BGEdFLESCH) + len(NYTEdFLESCH) + len (WPEdFLESCH))
  #print(editorialsFLESCH) #THIS IS 40.515776268649475

  #Average Flesch scores for all articles
  #articlesFLESCH = (sum(BGArtFLESCH) + sum(NYTArtFLESCH) + sum (WPArtFLESCH)) / (len(BGArtFLESCH) + len(NYTArtFLESCH) + len (WPArtFLESCH))
  #print(articlesFLESCH) #THIS IS 46.12364275381057



  

  
  


#Flesh Readability Formula =     
#now change arrays containing avg syllables per word for each article to flesh readabillity score for each article
#RE = 206.835 – (1.015 x ASL) – (84.6 x ASW) 
#RE = Readability Ease 
#ASL = Average Sentence Length (i.e., the number of words divided by the number of sentences) 
#ASW = Average number of syllables per word (i.e., the number of syllables divided by the number of words) 



if __name__ == '__main__':
    _main()
