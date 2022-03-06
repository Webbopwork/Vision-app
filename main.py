#print(1)
def wip(add=''): input('Sorry! This feature is still in development. '+add)

class save:
  def __init__(self, x): self.x = x

class window:
  def list(dict):
    x = save(None)
    import tkinter as Tk
    tk = Tk.Tk()
    for item in dict:
      def work(): 
        x.x = dict[item]
        tk.destroy()
      Tk.Button(text=item, command=work).pack()
    tk.mainloop()
    return x.x

def inside(path):
  with open(path, 'r') as f:
    x = f.read()
    f.close()
  return x

def dividing(thing, yes=' '):
  list = thing.split(yes)
  return list[0], yes.join(list[1:])

requirements = ['info.py','Info.py' 'data.py', 'Data.py', 'requirement.py', 'Requirement.py']
#input(requirements)

important = ['saved.txt', 'accounts.py']

splitter = '=a!*-_-*!A='

def intPlus(str):
  try: return int(str)
  except: raise ValueError('That is not an interger.')

def test(file, basic):
  try:
    with open(file, 'r') as f: f.close()
  except:
    with open(file, 'w') as f:
      f.write(basic)
      f.close()

def cover(str, around, between=''): return around+between+str+between+around

class tools:
  def __init__(self, account): self.username = account.username

  def calculator(self, text):
    try: return eval(text)
    except: raise ValueError('Can\'t include letters.')
  
  def generatePassword(self, lenght):
    from random import choice
    objects = '½§!1"2@#3£¤4$%5&6/7{(8[)9]=0}?+\\`´QqWwEeRrTtYyUuIiOoPpÅåAaSsDdFfGgHhJjKkLlÖöÄä^¨~\'*><|ZzXxCcVvBbNnNnMm;,:._-'
    x = ''
    for n in range(lenght):
      x = x + choice(objects)
    return x

  def showUsername(self):
    clear()
    input(self.username)
  
  def menu(self):
    while True:
      clear()
      x = work(input('[0] Generate password\n\n[1] Username\n\n[2] Calculator\n\n[3] Exit\n\nChoice: '))
      if x == 0:
        clear()
        try: 
          n = intPlus(input('Lenght: '))
          input('\n'+self.generatePassword(n))
        except ValueError as e: input('\n'+str(e))
      elif x == 1: self.showUsername()
      elif x == 2: 
        clear()
        try: input('\n'+str(self.calculator(input('Calculator: '))))
        except ValueError as e: input('\n'+str(e))
      elif x == 3: break

class encryption:
  def __init__(self, key, filename, variablename):
    self.key = key
    self.filename = filename
    self.variablename = variablename

  def encryptFile(self, path):
    from encryptionM import encrypt
    try:
      with open(path, 'r') as f:
        x = f.read()
        #input(x)
        f.close()
    except FileNotFoundError: raise FileNotFoundError('This file does not exist.')
    with open(path, 'w') as f:
      f.write(encrypt(x, self.key))
      f.close()

  def decryptFile(self, path):
    from encryptionM import decrypt
    try:
      with open(path, 'r') as f:
        x = f.read()
        #input(x)
        f.close()
    except FileNotFoundError: raise FileNotFoundError('This file does not exist.')
    with open(path, 'w') as f:
      f.write(decrypt(x, self.key))
      f.close()

  def save(self, dict):
    with open(self.filename, 'w') as f:
      f.write(self.variablename+' = '+str(dict))
      f.close()
  
  def menu(self):
    try: import encryptionM
    except ModuleNotFoundError:
      input('EncryptionM is not installed. Please contact support, update the program or install encryptionM induvidually.')
      return
    while True:
      clear()
      x = work(input('[0] Generate key\n\n[1] Encrypt\n\n[2] Decrypt\n\n[3] Encrypt file\n\n[4] Decrypt file\n\n[5] Exit\n\nChoice: '))
      if x == 0: 
        try:
          clear()
          self.save(generateKey())
          input('Restart program to use the new encryption pack.')
        except FileNotFoundError as e: input(e)
      elif x == 1:
        clear()
        from encryptionM import encrypt
        input('\n'+encrypt(input('Encrypt: '), self.key))
      elif x == 2:
        clear()
        from encryptionM import decrypt
        input('\n'+decrypt(input('Decrypt: '), self.key))
      elif x == 3: 
        clear()
        try: self.encryptFile(input('File path: '))
        except FileNotFoundError as e: print(e)
        input('\nFile succesfully encrypted!')
      elif x == 4: 
        clear()
        try: self.decryptFile(input('File path: '))
        except FileNotFoundError as e: print(e)
        input('\nFile succesfully decrypted!')
      elif x == 5: break


def split(list):
  dict = {}
  all = []
  usernames = []
  passwords = []
  for item in list:
    user, passw = item
    all.append(user)
    all.append(passw)
    usernames.append(user)
    passwords.append(passw)
    dict[user] = passw

  return all, usernames, passwords, dict

def work(item):
  try: return int(item)
  except: return item

def clear():
  #print("\033[H\033[J", end='')
  import sys
  import os
  my_os = sys.platform.lower()
  #if my_os == 'win32': os.system('clr')
  if my_os == 'win32': print("\033[H\033[J", end='')
  elif my_os == 'linux': os.system('clear')
  elif my_os == 'darwin': os.system("clear && printf '\e[3J'")
  elif my_os == 'aix': os.system('tmp_clear')
  else: print("\033[H\033[J", end='')
  #else: print('\n' * 50)

def setTitle(title):
  import sys
  import os
  my_os = sys.platform.lower()
  if my_os == 'win32': os.system('title '+title)
  elif my_os == 'darwin': os.system("""PROMPT_COMMAND='echo -ne "\\033]0;${USER}@${HOSTNAME}: ${PWD}\\007"'""")

class ThoughtsNet:
  def __init__(self, account, file, folder):
    import os
    self.folder = folder
    self.username = account.username
    try: os.mkdir(folder)
    except: pass
    self.path = os.path.join(folder, file)
  
  def open(self):
    try: inside(self.path)
    except: 
      with open(self.path, 'w') as f: f.close()

  def send(self, content):
    if inside(self.path) == '': x = ''
    else: x = '\n'
    with open(self.path, 'a') as f:
      f.write(x+cover(self.username, splitter, '\n')+'\n'+content)
      f.close()
  
  def get(self):
    with open(self.path, 'r') as f: 
      x = f.read()
      f.close()
    x = x.split(splitter+'\n')
    names = []
    messages = []
    try: x.remove('')
    except: pass
    #print(x)
    a = True
    for item in x:
      if a: 
        names.append(item.strip())
        a = False
      else:
        messages.append(item)
        a = True
    x = ''
    n = 0
    #print(names, messages)
    for item in names: 
      x = x + '\n' + item + '\n' + messages[n]
      #print(messages[n])
      n = n + 1
    
    return x, messages, names
  
  def search(self, messages, names, searchFor):
    results = []
    posts = []
    x = 0
    for item in names:
      posts.append(item+'\n'+messages[x])
      x = x + 1
    for post in posts:
      if searchFor in post: results.append(post)
    return results

class chat:
  def __init__(self, account, recipient):
    import os
    self.file = ''
    self.divider = '='
    self.folder = 'Chats'
    self.username = account.username
    self.recipient = recipient
    self.path = os.path.join(os.getcwd(), self.folder)
    try: os.mkdir(self.folder)
    except: pass
  
  def open(self):
    from accounts import accounts
    import os
    names = []
    for item in accounts:
      name, trash = item
      names.append(name)
    things = os.listdir(self.path)
    alt1 = self.recipient+self.divider+self.username
    alt2 = self.username+self.divider+self.recipient
    if alt1 in things: name = alt1
    elif alt2 in things: name = alt2
    elif not self.recipient in names: raise ValueError('That recipient does not exist.')
    else: 
      #raise ValueError('This conversation does not exist.')
      with open(os.path.join(self.path, alt2), 'w') as f:
        f.write('')
        f.close()
      name = alt2
    self.file = os.path.join(self.path, name)
  
  def send(self, message):
    if not splitter in message:
      if inside(self.file) == '': x = ''
      else: x = '\n'
      with open(self.file, 'a') as f:
        f.write(x+cover(self.username, splitter, '\n')+'\n'+message)
        f.close()
    else: raise ValueError('That can not be in sent as it includes a banned combination.')
  
  def get(self):
    with open(self.file, 'r') as f: 
      x = f.read()
      f.close()
    x = x.split(splitter+'\n')
    names = []
    messages = []
    try: x.remove('')
    except: pass
    #print(x)
    a = True
    for item in x:
      if a: 
        names.append(item.strip())
        a = False
      else:
        messages.append(item)
        a = True
    x = ''
    n = 0
    #print(names, messages)
    for item in names: 
      x = x + '\n' + item + '\n' + messages[n]
      #print(messages[n])
      n = n + 1
    
    return x, messages, names


class appStore:
  def __init__(self, account):
    import os
    self.search = None
    self.username = account.username
    self.loggedin = account.loggedin
    self.apps = []
    self.folder = 'Store'
    self.path = os.path.join(os.getcwd(), self.folder)
  
  def look(self):
    import os
    try: os.mkdir(self.folder)
    except: pass
    self.apps = os.listdir(self.path)
    return self.apps
  
  def getinfo(self, app):
    import os
    import sys
    datafile = 'data.txt'
    path = os.path.join(self.folder, app)
    with open(os.path.join(path, datafile)) as f:
      name = f.read()
      f.close()
    sys.path.insert(1, path)
    if name == 'info': from info import data as x
    elif name == 'Info': from Info import data as x
    elif name == 'Data': from Data import data as x
    elif name == 'requirement': from requirement import data as x
    elif name == 'Requirement': from Requirement import data as x
    else: x = {'author': 'Unknown'}
    return x
  
  def add(self, name, file, tags):
    import os
    try: os.mkdir(os.path.join(self.folder, name))
    except: raise FileExistsError('This app already exists')
    x = 0
    varname = 'data'
    namefile = 'data.txt'
    info = {'author': self.username, 'tags': tags}
    while True: 
      requirement = requirements[x]
      if len(requirements) >= x: x = 0
      if file != requirement: break
    folder = os.path.join(self.path, name)
    with open(file, 'r') as f:
      In = f.read()
      f.close()
    with open(os.path.join(folder, file), 'w') as f:
      f.write(In)
      f.close()
    with open(os.path.join(folder, requirement), 'w') as f:
      f.write(varname+' = '+str(info))
      f.close()
    with open(os.path.join(folder, namefile), 'w') as f:
      split = '.'
      f.write(split.join(requirement.split(split)[:-1]))
      f.close()
  
  def search(self, messages, names, searchFor):
    results = []
    posts = []
    x = 0
    for item in names:
      posts.append(item+'\n'+messages[x])
      x = x + 1
    for post in posts:
      if searchFor in post: results.append(post)
    return results

  def search(self, thing):
    splitting = ', '
    thing.split(splitting)

  def download(self, name):
    import os
    list = self.look()
    if not name in list: raise FileNotFoundError('This application does not exist.')
    path = os.path.join(self.path, name)
    file = os.listdir(path)[0]
    path = os.path.join(path, file)
    with open(path, 'r') as f:
      x = f.read()
      f.close()
    path = os.path.join(os.getcwd(), 'Downloads')
    try: os.mkdir(path)
    except: pass
    path = os.path.join(path, name)
    try: os.mkdir(path)
    except: pass
    path = os.path.join(path, file)
    with open(path, 'w') as f:
      f.write(x)
      f.close()

  def menu(self):
    Split = ', '
    while True:
      clear()
      choice = work(input('[0] Apps\n\n[1] Upload app\n\n[2] Dowload app\n\n[3] Close\n\nChoice: '))
      if choice == 0: 
        clear()
        list = []
        for item in self.look():
          info = self.getinfo(item)
          list.append(item+'\nBy: '+info['author']+'\nTags: '+Split.join(info['tags']))
        input('\n\n'.join(list)+'\n\n')
      elif choice == 1: 
        clear()
        self.add(input('App name: '), input('\nFile name: '), input(f'\nTags(Split with "{Split}"): ').split(Split))
        input('\nApp succesfully uploaded!')
      elif choice == 2:
        clear()
        self.download(input('App name: '))
        input('\nApp succesfully downloaded!')
      elif choice == 3: break


class account:
  def __init__(self, username=None, password=None):
    self.username = username
    self.password = password
    self.loggedin = False
  
  def login(self, username, password):
    from accounts import accounts
    all, usernames, passwords, details = split(accounts)
    if not username in usernames: raise ValueError('Username does not exist.')
    elif details[username] != password: raise ValueError('Password is not correct.')
    elif details[username] == password: 
      self.username = username
      self.password = password
      self.loggedin = True
    else: raise ValueError('You really should not be here.')
  
  def register(self, username, password):
    file = 'accounts.py'
    variable = 'accounts'
    from accounts import accounts
    all, usernames, passwords, details = split(accounts)
    if username in usernames: raise ValueError('Username is already taken.')
    else:
      accounts.append((username, password))
      with open(file, 'w') as f:
        f.write(variable+' = '+str(accounts))
        f.close()
      self.username = username
      self.password = password
      self.loggedin = True
  
  def logout(self): 
    savefile = 'saved.txt'
    self.loggedin = False
    with open(savefile, 'w') as f: f.close()

#app
file = 'accounts.py'
setTitle('Vision login')
try: 
  with open(file, 'r') as f: f.close()
except:
  with open(file, 'w') as f: 
    f.write('accounts = []')
    f.close()
acc = account()
while True:
  savefile = 'saved.txt'
  clear()
  try:
    with open(savefile, 'r') as f:
      x = f.read().split('\n')
      f.close()
    acc.login(x[0], x[1])
    choice = None
  except:
    choice = work(input('[0] Log in\n\n[1] Register\n\nChoice: '))
  clear()
  if choice == 0:
    try: 
      acc.login(input('Username: '), input('\nPassword: '))
      with open(savefile, 'w') as f:
        f.write(acc.username+'\n'+acc.password)
        f.close()
    except ValueError as err: input('\n'+str(err))
  elif choice == 1:
    try: 
      acc.register(input('Username: '), input('\nPassword: '))
      with open(savefile, 'w') as f:
        f.write(acc.username+'\n'+acc.password)
        f.close()
    except ValueError as err: input('\n'+str(err))
  if acc.loggedin: break

savedfile = 'saved.py'
savedvariable = 'saved'
thoughtsfile = 'thoughts.txt'
thoughtsfolder = 'ThoughtsNet'
failed = False
try:
  from encryptionM import generateKey
  test(savedfile, savedvariable+' = '+str(generateKey()))
except: failed = True
setTitle('Vision')
while acc.loggedin:
  clear()
  choice = work(input('[0] ThoughtsNet\n\n[1] Chat\n\n[2] Assistant\n\n[3] Store\n\n[4] Encryption\n\n[5] Tools\n\n[6] Log out\n\n[7] Exit\n\nChoice: '))
  if choice == 0:
    thought = ThoughtsNet(acc, thoughtsfile, thoughtsfolder)
    thought.open()
    while True:
      clear()
      x, messages, names = thought.get()
      print(x)
      x = input('\nThought: ')
      y, search = dividing(x, ' ')
      #input([y.upper == '!search', search])
      if x.upper() == '!UPDATE': pass
      elif y.upper() == '!SEARCH':
        clear()
        x, messages, names = thought.get()
        input('\n'.join(thought.search(messages, names, search)))
      elif x.upper() != '!STOP': thought.send(x)
      else: break
  elif choice == 1:
    clear()
    try: 
      chat = chat(acc, input('Recipient: '))
      chat.open()
      while True:
        clear()
        x, messages, names = chat.get()
        print(x)
        x = input('\nMessage: ')
        if x.upper() == '!UPDATE': pass
        elif x.upper() != '!STOP':
          try: chat.send(x)
          except ValueError as e: input(e)
        else: break
    except ValueError as e: input(e)
  elif choice == 2: 
    clear()
    import assistant
  elif choice == 3:
    clear()
    app = appStore(acc)
    app.menu()
  elif choice == 4:
    clear()
    fail = False
    try: from saved import saved
    except: encryption({}, savefile, savedvariable).save(generateKey())
    encr = encryption(saved, savedfile, savedvariable)
    encr.menu()
  elif choice == 5:
    tool = tools(acc)
    tool.menu()
  elif choice == 6: acc.logout()
  elif choice == 7: break