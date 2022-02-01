import os
import sys
import random
#try: 
#  import speech_recognition as sr
#except:
#  os.system('pip install speechrecognition')
#  import speech_recognition as sr
#try:
#  import pyaudio
#except:
#  os.system('pip install pyaudio')
#  import pyaudio
#try:
#  import wave
#except:
#  os.system('pip install wave')
#  import wave

#import sounddevice as sd
#from scipy.io.wavfile import write

name = 'vision'
replace = {'<enter>': '\n', '<tab>': '  '}
prefix = '\n   > '
AUDIO_FILE = 'transcript.wav'

def find(str, list):
  In = False
  for item in list:
    if item in str:
      In = True
  return In

#https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          if not find(textnum, ['*', '+', '-', '/']):
            raise Exception("Illegal word: " + word)
        

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def split(text):
  return text.split(' ')

def choices(list):
  return list[0], list[1:]

def say(text):
  print(prefix + str(text).replace('\n', '\n     ') + '\n')

def fix(list):
  return ' '.join(list)

def setTitle(title):
  my_os = sys.platform.lower()
  if my_os == 'win32': os.system('title '+title)
  elif my_os == 'darwin': os.system("""PROMPT_COMMAND='echo -ne "\\033]0;${USER}@${HOSTNAME}: ${PWD}\\007"'""")

def clear():
  #print("\033[H\033[J", end='')
  my_os = sys.platform.lower()
  #if my_os == 'win32': os.system('clr')
  if my_os == 'win32': print("\033[H\033[J", end='')
  elif my_os == 'linux': os.system('clear')
  elif my_os == 'darwin': os.system("clear && printf '\e[3J'")
  elif my_os == 'aix': os.system('tmp_clear')
  else: print("\033[H\033[J", end='')

def calculate(fixed):
  multiplication = ['times', 'multiplied with', 'multiplied by', 'multiplied', 'multiply with', 'multiply by', 'multiply']
  subtraction = ['minus', 'subtracted with', 'subtracted by', 'subtracted', 'subtract with', 'subtract by', 'subtract']
  addition = ['plus', 'add', 'added with', 'added by', 'added']
  division = ['divided with', 'divided by', 'divided', 'divide']

  for item in multiplication: fixed = fixed.replace(item, '*')
  for item in division: fixed = fixed.replace(item, '/')
  for item in subtraction: fixed = fixed.replace(item, '-')
  for item in addition: fixed = fixed.replace(item, '+')

  return text2int(fixed)

#def record(seconds=5, fs=44100, AUDIO_FILE='transcript.wav'):
#  chunk = 1024
#  FORMAT = pyaudio.paInt16
#  channels = 1
#  r = sr.Recognizer()
#  with sr.Microphone() as source:
#    r.pause_threshold = .5
#    audio = r.listen(source)
#    try:
#      query = r.recognize_google(audio, language='en-us')
#      return query
#    except:
#      return ''
  #p = pyaudio.PyAudio()
  #stream = p.open(format=FORMAT, channels=channels, rate=fs, input=True, output=True, frames_per_buffer=chunk)
  #frames=[]
  #for i in range(int(44100 / chunk * seconds)):
  #  data = stream.read(chunk)
  #  frames.append(data)
  #stream.stop_stream()
  #stream.close()
  #p.terminate()
  #wf = wave.open(AUDIO_FILE, 'wb')
  #wf.setchannels(channels)
  #wf.setsampwidth(p.get_sample_size(FORMAT))
  #wf.setframerate(fs)
  #wf.writeframes(b"".join(frames))
  #wf.close()

  #with sr.AudioFile(AUDIO_FILE) as source:
  #  audio = r.record(source)
  #  transcript = r.recognize_google(audio)
  #  return transcript


#record()

#print(text2int('three hundred ten thousand'))
#clear()
setTitle('Assistant')
while True:
  choice = input('Action: ')
  list = split(choice)
  command, rest = choices(list)
  command = command.lower()
  fixed = fix(rest)
  try: first = rest[0]
  except: first = fixed
  try: second = rest[1]
  except: second = fixed
  if command == 'say': say(fixed)
  elif command == 'citate' or command == 'quote': say('"' + fixed + '"')
  elif command == 'clear': clear()
  elif command == 'run':
    if '.py' in fixed: 
      print('')
      os.system('python3 ' + first)
      print('')
    else: os.system(first)
  elif command == 'pog':
    say('''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⡿⠿⠛⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣏⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣀⠀⠀⠹⢿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣼
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠛⠛⠛⠛⠛⠛⠛⣻⣿
⣯⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣾⡟⠛
⠿⠿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠿⠟⠛⠉⠀⠀
⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠁⠀⠀⠀⠀⠀⠀
⠿⢿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠛⠛⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣶⣤⣶⣶⣶⣦⣄⣀⣠⣤⣶⣾⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
  elif command == 'alright': say("It's gonna be alright.")
  elif command == 'goat': say(random.choice(['Baaaahhh!', 'Bääää!', 'Baaaaahhhhhhh!', 'Bah.']))
  elif command == 'cheer': say('※\(^o^)/※')
  elif command == 'lenny': say('( ͡° ͜ʖ ͡°)')
  elif command == 'scream': say('╚(•⌂•)╝')
  elif command == 'make':
    with open(first, 'w') as f:
      f.close()
    say(first + ' made.')
  elif command == 'write':
    x = input(prefix)
    print('')
    for item in replace:
      x = x.replace(item, replace[item])
    with open(first, 'w') as f:
      f.write(x)
      f.close()
  elif command == 'read':
    try:
      with open(first, 'r') as f:
        say(f.read())
        f.close()
    except: say('I can not find that file.')
  elif command == 'add':
    try:
      with open(first, 'r') as f:
        f.close()
      x = input(prefix)
      print('')
      for item in replace:
        x = x.replace(item, replace[item])
      with open(first, 'a+') as f:
        f.write(x)
        f.close()
    except: say('I can not find that file.')
  elif command == 'remove': 
    try: 
      os.remove(first)
      say(first+' has been removed.')
    except: say('Can not find that file.')
  elif command == 'command': 
    print('')
    os.system(fixed)
    print('')
  elif command == 'name': name = fixed
  elif command == 'title': setTitle(fixed)
  elif command == 'what':
    if first.lower() == 'is':
      fixed = fix(rest[1:])
      say(calculate(fixed))
  elif command == 'calculate':
    say(calculate(fixed))
  elif command in ['exit', 'quit', 'kill', 'stop', 'end']: break
  else: say('Command not found.')
