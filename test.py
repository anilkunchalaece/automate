
#import pyttsx
from gtts import gTTS
import pygame
import getMessages



#engine = pyttsx.init();
#rate = engine.getProperty('rate')
#engine.setProperty('rate',70)
val = getMessages.main()
print(val)
output = 'Hi Anil you got Email from '+val[0]['sender']+" Subject is " + val[0]['subject']
print(output)
tts = gTTS(text=output, lang='en')

tts.save("hello.mp3")
#import vlc
#p = vlc.MediaPlayer("hello.mp3")
#p.play()
pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
