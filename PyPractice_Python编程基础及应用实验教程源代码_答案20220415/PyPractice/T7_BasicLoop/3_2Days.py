guoPowers = []    #天天练的郭大侠
wangPowers = []   #三天打渔、两天晒网的王大侠

guoPower,wangPower = 100,100
for x in range(365*10):
    guoPower *= 1.001
    if x % 5 in [0,1,2]:
        wangPower *= 1.002
    else:
        wangPower *= 0.999
    guoPowers.append(guoPower)
    wangPowers.append(wangPower)

print(guoPower,wangPower)

from matplotlib import pyplot as plt
plt.plot(list(range(365*10)),guoPowers,label="Master GUO")
plt.plot(list(range(365*10)),wangPowers,label="Master WANG")
plt.legend()
plt.show()
