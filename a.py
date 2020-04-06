#coding=utf-8
import romkan

def sameLastChars(s1, s2):
    return s1[-len(s2):] == s2

def replaceLastCharsWith(s1, i, s2):
    return s1[:-i] + s2



def ConjTe(s):
    if (sameLastChars(s, "suru")):
        return replaceLastCharsWith(s,4,  "shite")

    elif (sameLastChars(s, "kuru")):
        return replaceLastCharsWith(s,4, "kite")
    
    elif (s == "iku"):
        return u"exception: iku (行く) -> itte (行って)"

    elif (s == "kaeru"):
        return u"exteption: okaeru (帰る) -> okaette (帰って)"

    
    else:
        if s[-3:] in teFromDict:
            return replaceLastCharsWith(s, 3, teFromDict[s[-3:]])
        elif s[-2:] in teFromDict:
            return replaceLastCharsWith(s, 2, teFromDict[s[-2:]])
        elif s[-1:] in teFromDict:
            return replaceLastCharsWith(s, 1, teFromDict[s[-1:]])
        else:
            raise Exception("Cannot convert.")
        


# Present Short Affirmative
def verbPresentShortAffirmative(s): 
    if s[-1] != 'u':
        raise Exception("error: not dictionary form verb")
    else:
        return s

def adjectivePresentShortAffirmative(s): 
    if s[-1] == 'i':
        return s
    elif sameLastChars(s, "na"):
        return replaceLastCharsWith(s, 2, "da")
    else:
        raise Exception("error: not dictionary form Adjective")

def nounPresentShortAffirmative(s): 
    return s + "da"



# Present Long Affirmative
def verbPresentLongAffirmative(s):    
    #exceptions    
    if (s == "kaeru"):
        return "kaerimasu"

    elif (sameLastChars(s, "suru")):
        return replaceLastCharsWith(s, 4, "shimasu")

    elif (sameLastChars(s, "kuru")):
        return replaceLastCharsWith(s, 4, "kimasu")

    # ru verb
    elif (s[-3] == 'i' or s[-3] == 'e') and sameLastChars(s, "ru"):
        return replaceLastCharsWith(s, 2, "masu")

    elif s[-1] != 'u':
        raise Exception("error: not dictionary form verb")

    else:
        return replaceLastCharsWith(s, 1, "imasu")

def adjectivePresentLongAffirmative(s): 
    if s[-1] == 'i':
        return s + "desu"
    elif sameLastChars(s, "na"):
        return replaceLastCharsWith(s, 2, "desu")
    else:
        raise Exception("error: not dictionary form Adjective")

def nounPresentLongAffirmative(s): 
    return s + "desu"



# Present Short Negative
def verbPresentShortNegative(s): 
    #exceptions
    if (sameLastChars(s, "suru")):
        return replaceLastCharsWith(s, 4, "shinai")
    
    elif (sameLastChars(s, "kuru")):
        return replaceLastCharsWith(s, 4, "konai")

    elif (s == "aru"):
        return "nai"

    elif (s == "kaeru"):
        return "kaeranai"

    # ru verb
    elif (s[-3] == 'i' or s[-3] == 'e') and sameLastChars(s, "ru"):
        return replaceLastCharsWith(s, 2, "nai")

    # u verb end with う
    elif ((s[-2] == 'a' or s[-2] == 'e' or s[-2] == 'i' or s[-2] == 'o' or s[-2] == 'u') and (s[-1] == 'u')):
        return replaceLastCharsWith(s, 1, "wanai")
    

    elif s[-1] != 'u':
        raise Exception("error: not dictionary form verb")

    else:
        return replaceLastCharsWith(s, 1, "anai")

def adjectivePresentShortNegative(s): 
    if s[-1] == 'i':
        return replaceLastCharsWith(s, 1, "kunai")
    elif sameLastChars(s, "na"):
        return replaceLastCharsWith(s, 2, "janai")
    else:
        raise Exception("error: not dictionary form Adjective")

def nounPresentShortNegative(s): 
    return s + "janai"



# Present Long Negative
def verbPresentLongNegative(s): 
    #exceptions    
    if (s == "kaeru"):
        return "kaerimasen"

    elif (sameLastChars(s, "suru")):
        return replaceLastCharsWith(s, 4, "shimasen")

    elif (sameLastChars(s, "kuru")):
        return replaceLastCharsWith(s, 4, "kimasen")

    # ru verb
    elif (s[-3] == 'i' or s[-3] == 'e') and sameLastChars(s, "ru"):
        return replaceLastCharsWith(s, 2, "masen")

    elif s[-1] != 'u':
        raise Exception("error: not dictionary form verb")

    else:
        return replaceLastCharsWith(s, 1, "imasen")

def adjectivePresentLongNegative(s): 
    if s[-1] == 'i':
        return replaceLastCharsWith(s, 1, "kunaidesu")
    elif sameLastChars(s, "na"):
        return replaceLastCharsWith(s, 2, "janaidesu")
    else:
        raise Exception("error: not dictionary form Adjective")

def nounPresentLongNegative(s): 
    return s + "janaidesu"



# Past Short Affirmative
def verbPastShortAffirmative(s): 
    s0 = ConjTe(s)
    if (sameLastChars(s0, "te")):
        return replaceLastCharsWith(s0, 2, "ta")
    
    elif (sameLastChars(s0, "de")):
        return replaceLastCharsWith(s0, 2, "da")
    
    # elif (s0 == "Cannot convert."):
    #     return s0

    else:
        raise Exception("error")

def adjectivePastShortAffirmative(s): 
    if s[-1] == 'i':
        return replaceLastCharsWith(s, 1, "katta")
    elif sameLastChars(s, "na"):
        return replaceLastCharsWith(s, 2, "datta")
    else:
        raise Exception("error: not dictionary form Adjective")

def nounPastShortAffirmative(s): 
    return s + "datta"



# Past Long Affirmative
def verbPastLongAffirmative(s): 
    s0 = verbPresentLongAffirmative(s)
    return replaceLastCharsWith(s0, 2, "shita")

def adjectivePastLongAffirmative(s): 
    if s[-1] == 'i':
        return replaceLastCharsWith(s, 1, "kattadesu")
    elif sameLastChars(s, "na"):
        return replaceLastCharsWith(s, 2, "deshita")
    else:
        raise Exception("error: not dictionary form Adjective")

def nounPastLongAffirmative(s): 
    return s + "deshita"



# Past Short Negative
def verbPastShortNegative(s): 
    s0 = verbPresentShortNegative(s)
    return replaceLastCharsWith(s0, 1, "katta")

def adjectivePastShortNegative(s): 
    if s[-1] == 'i':
        return replaceLastCharsWith(s, 1, "kunakatta")
    elif sameLastChars(s, "na"):
        return replaceLastCharsWith(s, 2, "janakatta")
    else:
        raise Exception("error: not dictionary form Adjective")

def nounPastShortNegative(s): 
    return s + "janakatta"



# Past Long Negative
def verbPastLongNegative(s): 
    return verbPresentLongNegative(s) + "deshita"

def adjectivePastLongNegative(s): 
    if s[-1] == 'i':
        return replaceLastCharsWith(s, 1, "kunakattadesu")
    elif sameLastChars(s, "na"):
        return replaceLastCharsWith(s, 2, "janakattadesu")
    else:
        raise Exception("error: not dictionary form Adjective")

def nounPastLongNegative(s): 
    return s + "janakattadesu"


teFromDict = {

    "iru" : "ite",
    "eru" : "ete",

    "u"   : "tte",
    "tu"  : "tte", "tsu" : "tte", 
    "aru" : "atte",
    "uru" : "utte",
    "oru" : "otte",

    "mu" : "nde",
    "bu" : "nde",
    "nu" : "nde",

    "ku" : "ite",
    "gu" : "ide",

    "su" : "shite"
}



while 1:
    pos = None
    isPresent = None
    isLong = None
    isAffirmative = None

    cmd = input("> ")
    cmdarr = cmd.split(" ")

    if    'n' in cmdarr[0]:
        pos = 'noun'
    elif  'ad' in cmdarr[0]:
        pos = 'adj'
    elif  'v' in cmdarr[0]:
        pos = 'verb'

    if   'pr' in cmdarr[0]: 
        isPresent = True
    elif 'pa' in cmdarr[0]:
        isPresent = False
        
    if    'l' in cmdarr[0]:
        isLong = True
    elif  's' in cmdarr[0]:
        isLong = False

    if    '1' in cmdarr[0]:
        isAffirmative = True
    elif  '0' in cmdarr[0]:
        isAffirmative = False
    

    try:    
        if 'te' in cmdarr[0]:
            print(romkan.to_hiragana(ConjTe(cmdarr[1].strip())))

        elif pos == 'noun':
            if isPresent:
                if isLong:
                    if isAffirmative:
                        print(romkan.to_hiragana(nounPresentLongAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(nounPresentLongNegative(cmdarr[1].strip())))
                else: # short
                    if isAffirmative:
                        print(romkan.to_hiragana(nounPresentShortAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(nounPresentShortNegative(cmdarr[1].strip())))
            else: # past
                if isLong:
                    if isAffirmative:
                        print(romkan.to_hiragana(nounPastLongAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(nounPastLongNegative(cmdarr[1].strip())))
                else: # short
                    if isAffirmative:
                        print(romkan.to_hiragana(nounPastShortAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(nounPastShortNegative(cmdarr[1].strip())))
        elif pos == "adj":
            if isPresent:
                if isLong:
                    if isAffirmative:
                        print(romkan.to_hiragana(adjectivePresentLongAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(adjectivePresentLongNegative(cmdarr[1].strip())))
                else: # short
                    if isAffirmative:
                        print(romkan.to_hiragana(adjectivePresentShortAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(adjectivePresentShortNegative(cmdarr[1].strip())))
            else: # past
                if isLong:
                    if isAffirmative:
                        print(romkan.to_hiragana(adjectivePastLongAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(adjectivePastLongNegative(cmdarr[1].strip())))
                else: # short
                    if isAffirmative:
                        print(romkan.to_hiragana(adjectivePastShortAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(adjectivePastShortNegative(cmdarr[1].strip())))
        elif pos == "verb":
            if isPresent:
                if isLong:
                    if isAffirmative:
                        print(romkan.to_hiragana(verbPresentLongAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(verbPresentLongNegative(cmdarr[1].strip())))
                else: # short
                    if isAffirmative:
                        print(romkan.to_hiragana(verbPresentShortAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(verbPresentShortNegative(cmdarr[1].strip())))
            else: # past
                if isLong:
                    if isAffirmative:
                        print(romkan.to_hiragana(verbPastLongAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(verbPastLongNegative(cmdarr[1].strip())))
                else: # short
                    if isAffirmative:
                        print(romkan.to_hiragana(verbPastShortAffirmative(cmdarr[1].strip())))
                    else: # negative
                        print(romkan.to_hiragana(verbPastShortNegative(cmdarr[1].strip())))

                
    except NameError:
        print("bad format")
    
    except:
        print("dictionary form not given")
