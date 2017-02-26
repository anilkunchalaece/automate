
import pyttsx
import getMessages

engine = pyttsx.init();
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-65)

val = getMessages.main()
print(val)
output = " Hi There Anil... Got Message From" + val[0]['sender']+"Subject is" + val[0]['subject']
engine.say(output)
engine.runAndWait()
