
directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stopWords = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def scan(stuff):
    words = stuff.split()
    #if isinstance(words, basestring): # Python 3: isinstance(arg, str)
    ret = []
    for word in words:
        isNumber = False
        myNumber = -1
        try:
            int(word)
            isNumber = True
        except:
            pass
        if isNumber:
            ret.append(('number',int(word)))
        else:
            ret.append((find(word),word))
    return ret
    
#def isStopWord(word):
#    if word in stopWords:
#        return True
#    else:
#        return False

def find(word):
    if word in directions:
        return 'direction'
    elif word in verbs:
        return 'verb'
    elif word in stopWords:
        return 'stop'
    elif word in nouns:
        return 'noun'
    else:
        return 'error'
    




