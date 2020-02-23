#!/usr/bin/python3

import sys

class Word:
	def __init__(self,chars,length):
		self.charsAmount=len(chars)
		self.word=[0]*length
		self.chars=chars
		self.length=length
		self.getWord()
		
		
	def roll(self):
		i=self.length-1
		while self.word[i] == self.charsAmount-1:
			self.word[i]=0
			i-=1
			if(i<0):
				return False
		self.word[i]+=1
		return True
	
	def getWord(self):
		string=''
		for letterNr in self.word:
			string+=self.chars[int(letterNr)]
		return string

	def setWord(self, word):
		self.word=word

def main():
    if len(sys.argv) == 1:
        print("please give list of chars as an input")
        exit()
    chars=sys.argv[1]
    if len(sys.argv) > 2:
        lenMax=int(sys.argv[2])
    else:
        lenMax=len(chars)
    wordsList=[]
    for length in range(1,lenMax+1):
        w=Word(chars,length)
        wordsList.append(w.getWord())
        while w.roll():
            wordsList.append(w.getWord())
    for word in wordsList:
	    print(word)


if __name__ == "__main__":
    main()

                    #Tests:
# w=word(chars,4)
# print(w.getWord())
# w.roll()
# print(w.getWord())

# w.setWord([0,0,0,3])
# print(w.getWord())

# w.roll()
# print(ciastko)
# print(w.getWord())
# print(ciastko)

# w.setWord([3,3,3,3])
# print(w.getWord())
# w.roll()
# print(w.getWord())
