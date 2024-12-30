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

morseReversed = {}
for k,v in morse.items():
    morseReversed[v] = k

def decode(sEncoded):
    r = ""
    words = sEncoded.split("//")           #按//分割为词
    for word in words:
        chars = word.split("/")     #把词按/分割成单个字符的Morse码
        for c in chars:
            r += morseReversed[c]   #查字典，解码成原始字符
        r += " "                    #词之间加空格
    return r

f = open("encoded.txt","rt")
sEncoded = f.read()
f.close()

print("Encoded message:",sEncoded)
sMessage = decode(sEncoded)
print("Decoded message:",sMessage)