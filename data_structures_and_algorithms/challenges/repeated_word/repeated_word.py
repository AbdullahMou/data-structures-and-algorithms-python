import re
def repeared_word(str):
    words = (re.sub(r'[^\w\s]','',str)).split(' ')
    repeared=[]
    for  i in words:
        i= i.lower()
        if i in repeared :
            return i
        else:
            repeared.append(i)