import winsound,time,sys
def sendTelegram(sEncoded):
    words = sEncoded.split("//")        #按//分割成词
    for word in words:
        chars = word.split("/")         #按/分割成字符
        for code in chars:
            for x in code:
                if x == ".":
                    winsound.Beep(1200,100) #1200Hz, 100ms ~ 嘀
                else:
                    winsound.Beep(1200,300) #1200Hz, 300ms ~ 嗒
                print(x,end="") 
            print("/",end="")
            sys.stdout.flush()
            time.sleep(0.3)                 #字符间间隔300ms
        print("/",end="")
        time.sleep(0.4)                     #词间间隔700ms = 300 + 400ms

f = open("encoded.txt","rt")
sEncoded = f.read()
f.close()

sendTelegram(sEncoded)