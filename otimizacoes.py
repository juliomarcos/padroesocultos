# -*- coding: cp1252 -*-
import re

# Otimização sugerida pelo colega Félix Zanetti
def RemoveCharsNotInPattern(string, padrao):
   pat = r"[^%s]" % padrao
   return re.sub(pat, '', string)
