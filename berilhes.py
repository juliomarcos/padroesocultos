# -*- coding: cp1252 -*-
from geraIndices import *
padrao = 'aba'
fileName = 't1.txt'

s = open(fileName).read()
sLength = len(s) - 1 # \0

padraoLength = len(padrao)
padraoCounter = 0

indices = GeraIndicesPadraoOculto(sLength, len(padrao))
#print indices

def ContaPadroes(indices):
   def CheckLetter(t):
      #print t
      pInd = t[0]
      sInd = t[1]
      return s[sInd] == padrao[pInd]
      
   padraoCounter = 0
   for t in indices:
      tEnum = zip(range(len(t)), t)
      #print tEnum
      checkedList = map(CheckLetter, tEnum)
      #print checkedList
      if reduce(lambda a,b: a and b, checkedList):
         padraoCounter += 1
         
   return padraoCounter

nVezes = ContaPadroes(indices)

print 'Padrão', "\""+padrao+"\"", 'econtrado'
print 'Encontrado', nVezes, 'vezes' if padraoCounter > 1 else 'vez'

