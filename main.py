#Logging
#Logging allows you to output status messages to a file. it helps inform us of which parts of our code may have executed and which problems may have arisen
#logging levels are debug, info, warning, error, critical
import logging
import math
#print(dir(logging)) #items in caps are constants, capitalized items are classes and the lower case letters are methods

#basic config sets the logging level to 30 by default
#loggers will only write logging messages for logging levels greater than or equal to the set level
#By default the logging messages are created in append mode. if we want them to be overwritten we have to change the file mode to w in the logger config

#create basic config constants
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

#create and configure logger
logging.basicConfig(filename='D:\\python\\pythonLogs.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')

#create a logger
logger = logging.getLogger()

#test the logger
logger.info("This is the second logging message")

#check the logging level
#print(logger.level)


#JSON
#use pythons JSON library to send and recieve JSON data packets
import json
#print(dir(json))

#read json data
#json.load(f): allows us to load json data from a a file or file like object
#json.loads(s): allows us to load json data from a string

#write json data
#json.dump(j,f): writes a JSON object to a file or file like object
#json.dumps(j): outputs json object as a string

#we use json.loads when our data arrives in form of a string

movie2={}
movie2["title"]="minority report"
movie2["director"]="Steven Spielberg"
movie2["composer"]="John Williams"
movie2["actors"]=["Tom Cruise","Collin Farrel","Samantha Morton","Max vON Sydow"]
movie2["isAwesome"]=True
movie2["budget"]=102000000
movie2["cinematographer"]="Janusz kami\u0144ski"

#write the movie data in JSON format to afile
file2=open("D:\\python\\moviedata.txt","w",encoding="utf-8")

#our data contains non ascii characters so we have to set ensure ascii to False
json.dump(movie2,file2,ensure_ascii=False)
file2.close()

#for cryptographically secure random number generators in python, use the os.urandom() or SystemRandom

