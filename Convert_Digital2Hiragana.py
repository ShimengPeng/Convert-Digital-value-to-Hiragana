import pykakasi
from kanjize import kanji2int,int2kanji
import re
from fuzzywuzzy import process,fuzz

def kanji2hiragana(text):
    kakasi=pykakasi.kakasi()
    kakasi.setMode('J','H')
    conv=kakasi.getConverter()
    
    kanji2hiragana=conv.do(text)
    return kanji2hiragana
 
 def Ditital2Hiragana(sentence):
     digital_get=re.compile('¥¥d+')
     digital_dix2list=list(digital_get.finiter(sentence))
     
     for rep in digital_idx2list:
         dig2int=int(rep.group())
         dig2kanji=int2kanji(dig2int)
         dig2hira=self.kanji2hiragana(dig2kanji)
         
         sentence=sentence.replace(str(dig2int),dig2hira)
 Digital2Hiragana('今日は30個リンゴを買いました、2000円ぐらいかかりました')
