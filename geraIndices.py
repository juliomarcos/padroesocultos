# -*- coding: cp1252 -*-

def GeraIndicesPadraoOculto(sLen, pLen):
   #print 'sLen - 1 =', sLen
   #print 'pLen', pLen
   # cada posição tem um jMax
   # em um texto de tamanho 4 estes seriam os jMax
   # (2, 3, 4)
   jMaxes = list(reversed(list(reversed([x+2 for x in range(sLen)]))[:pLen]))
   #print 'jMaxes', jMaxes
      
   ultimoIndice = sLen - (pLen - 1)
   t = range(pLen)
   yield t
   print 'Ultimo Indice', ultimoIndice
   #print t
   while t[0] != ultimoIndice:
      t = ContinuaLista(t, sLen=sLen, pLen=pLen, jMaxes=jMaxes)
      yield t
      #print t

def ConstroiNovaLista(t, indiceQuebra):
   # (0, 2, 6) -> (0, 2, 3)
   # (1, 5, 6) -> (1, 2, 3)
   # (0, 3, 6) -> (0, 3, 4)
   k = indiceQuebra
   return t[:k] + tuple([t[k-1]+j+1 for j in range(len(t)-k)])

def IndiceQuebra(t, jMaxes):
   for i in range(len(t)):
      if t[i] >= jMaxes[i]: return i

def ContinuaLista(t, pLen, sLen, jMaxes):
   # complicados
   # (0, 2, 6) -> (0, 2, 3)
   # (1, 5, 6) -> (1, 2, 3)
   # (0, 3, 6) -> (0, 3, 4)
   # (0, 1, 4) -> (0, 2, 3)
   #
   # simples
   # (0, 1, 2) -> (0, 1, 3)
   for j in reversed(range(pLen)):
      #print t, j, jMaxes
      if t[j] > jMaxes[j]:
         indiceQuebra = IndiceQuebra(t, jMaxes)
         return ConstroiNovaLista(t, indiceQuebra)
      else:
         q = SomaUmComCarry(t, sLen, jMaxes)
         indiceQuebra = IndiceQuebra(q, jMaxes)
         #print q, indiceQuebra
         if indiceQuebra != None:
            return ConstroiNovaLista(q, indiceQuebra)
         else:
            return q

def SomaUmComCarry(t, sLen, jMaxes):
   m = list(t)
   tLen = len(t)

   m[-1] += 1
   carry = True
   i = tLen - 1
   while carry and i >= 0:
      if m[i] >= jMaxes[i]: # carry
         m[i-1] += 1
         i -= 1
      else:
         carry = False

   return tuple(m)

if __name__ == "__main__":

   import unittest
   class TestGeraIndiciesPadrao3(unittest.TestCase):

      def setUp(self):
         self.sLen = 5
         self.pLen = 3
         # um pouco diferente, coisa do \0
         self.jMaxes = list(reversed(list(reversed([x+1 for x in range(self.sLen)]))[:self.pLen]))
         print self.jMaxes
         
      def test_soma_um_com_carry(self):
         iValues = [(0,1,2), (0,1,5), (0,4,5)]
         eValues = [(0,1,3), (0,2,6), (1,5,6)]
         for i,e in zip(iValues, eValues):
            r = SomaUmComCarry(i, self.sLen, self.jMaxes)
            self.assertEqual(e, r)
            
      def test_constroi_nova_lista(self):
         iValues = [(0,2,6), (0,3,6), (1,5,6)]
         eValues = [(0,2,3), (0,3,4), (1,2,3)]
         ruptura = [2      , 2      , 1      ]        
         for i,e,k in zip(iValues, eValues, ruptura):
            r = ConstroiNovaLista(i,k)
            self.assertEqual(e, r)

      def test_continua_lista(self):
         tuplas = [((0,2,6), (0,2,3)),
                   ((1,5,6), (1,2,3)),
                   ((0,3,6), (0,3,4)),
                   ((0,1,4), (0,2,3))]

         for t in tuplas:
            #print t
            entrada = t[0]
            expected = t[1]
            result = ContinuaLista(entrada, self.pLen, self.sLen, self.jMaxes)
            self.assertEqual(expected, result)
         
   try:
      unittest.main()
   except SystemExit as inst:
      pass
               
