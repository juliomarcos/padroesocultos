# -*- coding: cp1252 -*-
import re

# Otimiza��o sugerida pelo colega F�lix Zanetti
def RemoveCharsNotInPattern(string, padrao):
   pat = r"[^%s]" % padrao
   return re.sub(pat, '', string)
