morse = {
    # Letters
    "a": ".-","b": "-...","c": "-.-.","d": "-..","e": ".","f": "..-.","g": "--.",
    "h": "....","i": "..","j": ".---","k": "-.-","l": ".-..","m": "--","n": "-.",
    "o": "---","p": ".--.","q": "--.-","r": ".-.","s": "...","t": "-","u": "..-",
    "v": "...-","w": ".--","x": "-..-","y": "-.--","z": "--..",
    # Numbers
    "0": "-----","1": ".----","2": "..---","3": "...--","4": "....-",
    "5": ".....","6": "-....","7": "--...","8": "---..","9": "----.",
    # Punctuation
    "&": ".-...","'": ".----.","@": ".--.-.",")": "-.--.-","(": "-.--.",
    ":": "---...",",": "--..--","=": "-...-","!": "-.-.--",".": ".-.-.-",
    "-": "-....-","+": ".-.-.",'"': ".-..-.","?": "..--..","/": "-..-.",
}

morseReverse = {}
for k,v in morse.items():
    morseReverse[v] = k

def encode(s):
    r = ""
    for x in s:
        if x == " ":
            r += "/"   #词间停顿
        else:
            r = r + morse[x] + "/"    #空格表示字符间停顿 
    return r[:-1]

s = "Washington, this is pearl harbour, we are under japanese attack, japanese attack, repeat, repeat, this is not drill."
s1 = encode(s.lower())
print(s1)

def decode(s):
    r = ""
    words = s.split("//")
    for word in words:
        chars = word.split("/")
        for c in chars:
            r += morseReverse[c]
        r += " "
    return r

s2 = decode(s1)
print(s2)


import winsound,time,sys
def sendTelegram(s):
    words = s.split("//")
    for word in words:
        chars = word.split("/")
        for code in chars:
            for x in code:
                if x == ".":
                    winsound.Beep(1200,100)
                else:
                    winsound.Beep(1200,300)
                print(x,end="")
                sys.stdout.flush()
            print("/",end="")
            time.sleep(0.3)
        print("/",end="")
        time.sleep(0.4)

sendTelegram(s1)