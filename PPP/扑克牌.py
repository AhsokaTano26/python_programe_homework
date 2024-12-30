suits = ['红','梅','黑','方']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
cards = [x+y for x in suits for y in ranks]
print(cards)