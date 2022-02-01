import random
def generateKey(items='AaBbCcDdEeFfGgHhJjLlMmNnOoUuPpKkIiQqRrSsTtYyZzWwÅåÄäÖö 1234567890<>?=)(/&%¤#"!\'\\^¨*-_.:,;|~´±+§½@¥€$[]{}£⌂₧৹₷æÆɐĆćĦʯģğĤɤĥɥ'):
  #items='AaBbCcDdEeFfGgHhJjLlMmNnOoUuPpKkIiQqRrSsTtYyZzWwÅåÄäÖö 1234567890<>?=)(/&%¤#"!\'\\^¨*-_.:,;|~´±+§½@¥€$[]{}£¡æø¶`\n₫₿₣₼₳₯௹¤৲৻⏕‽⏖⏔⌁⁒₢₡₺₪₹₽﷼₦℃©×÷℉®¦—№™℗⁅⁆⌈⌉⌊⌋«»‹›⟩⟨⟦⟧⟪⟫⟬⟭⁙⁖⁚‥⁏⁞⁛¬✓✕⁘‼⁔⁀⁐⌂₧৹₷æÆɐĆćĦʯģğĤɤĥɥĵĶÏÌŇōŊŇɰmłṆÜ↕↛↞↠↢↣↨↭↮↯↤⇁⇃⇂⇆⇋⇌⇎⇑⇖▢▣▦▨▩▮▯▭▶▧'
  used = ''
  key = {}
  for item in items:
    while True:
      x = random.choice(items)
      #if not x in used:
      if not x in used and not item == x:
        key[item] = x
        used = used + x
        break
  return key

def backward(my_map): return dict(map(reversed, my_map.items()))

def encrypt(text, key):
  x = ''
  for item in text:
    try: x = x + key[item]
    except: x = x + item
  return x

def decrypt(text, key):
  key = backward(key)
  x, work = '', False
  for item in text:
    for p in key:
      if key[p] == item: 
        x = x + key[item]
        work = True
        break
    if not work: x = x + item
    #try: x = x + key[item]
    #except: x = x + item
  return x