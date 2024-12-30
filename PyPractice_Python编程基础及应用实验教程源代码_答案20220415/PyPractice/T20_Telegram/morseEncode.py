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

def encode(sMessage):
    r = ""
    for x in sMessage.lower():
        if x == " ":
            r += "/"   #再加一根/，两根/表示词间停顿
        else:
            r = r + morse[x] + "/"    #/表示字符间停顿
    return r[:-1]      #切片去除末尾多余的/

f = open("message.txt","rt")
sMessage = f.read()
f.close()

print("Message:",sMessage)

sEncoded = encode(sMessage)
f = open("encoded.txt","wt")
f.write(sEncoded)
f.close()

print("Encoded message:",sEncoded)
print("Encoded message has been saved to file encoded.txt.")



