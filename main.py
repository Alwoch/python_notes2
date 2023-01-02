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

movie2 = {}
movie2["title"] = "minority report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = [
  "Tom Cruise", "Collin Farrel", "Samantha Morton", "Max vON Sydow"
]
movie2["isAwesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz kami\u0144ski"

#write the movie data in JSON format to afile
file2 = open("D:\\python\\moviedata.txt", "w", encoding="utf-8")

#our data contains non ascii characters so we have to set ensure ascii to False
json.dump(movie2, file2, ensure_ascii=False)
file2.close()

#for cryptographically secure random number generators in python, use the os.urandom() or SystemRandom

#DECORATORS
#There are two types of decorators, the function decorators and class decorators
#A decorator is a function that takes another function as its argument and extends the behaviour of that function without explicityly modifying it. It therefore allows you to add ditional functionality to that function without modifying it

#*args and **kwargs means a function can take in an unlimited number of arguments and key word arguments
import functools


def start_end_function(func):

  @functools.wraps(func)  #preseve function identity
  def wrapper(*args, **kwargs):
    print('start')
    result = func(*args, **kwargs)
    print('end')
    return result

  return wrapper


def print_first_name():
  print('Alex')


#This is what would happen without a decorator. (we would pass the function explicitly into the other function)
#printed_name=start_end_function(print_first_name)
#print(printed_name)


#with a decorator
@start_end_function
def add_numbers(x):
  return x + 5
  #print(x+5)


#print(help(add_numbers(10)))
#print(add_numbers.__name__


def repeat(numtimes):

  def repeat_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(numtimes):
        result = func(*args, **kwargs)
      return result

    return wrapper

  return repeat_decorator


@repeat(numtimes=4)
def greet(name):
  print(f'Hello {name}')


#greet('sophia')

#we can also nest or stack decorators ontop of each other and they will be executed in the order in which they are listed

#class decorators
#class decorators are the same as function decorators but are used when we want to maintain or update a state


class CountCalls:

  def __init__(self, func):
    self.func = func
    self.num_calls = 0

  def __call__(self, *args, **kwargs):
    self.num_calls += 1
    print(f'This executed {self.num_calls} times')
    return self.func(*args, **kwargs)


@CountCalls
def say_hello(name):
  print(f'Hello {name}')


#say_hello('nakabuye')
#say_hello('imelda')
#say_hello('sharon')

#use cases
#-we can write a timer decorator to calculate the execution time
#-debug decorator to print more info about a function
#-a check decorator to scheck if a function fullfills certain requirements and adapt its behaviour accordingly
#-register functions like plugins using decorators
#-cache return values
#add or update state

#PYTHON SPECIAL METHODS AND ATTRIBUTES
#using special methods we can;
#-empower our classes with certain behavior for standard syntax
#-override operators
#-define iteration
#-access inner workings of classes etc


#__dict__ is a dict containing all the objects attributes of a class
class SnowFlake:
  pass


flake = SnowFlake()
#print(dir(flake))


class Martian:
  """This is a doc string"""

  def __init__(self, fn, ln):
    self.first_name = fn
    self.last_name = ln


#print(Martian.__doc__)  #gives us the docstring in the martian class
m1 = Martian("nakakande", "hudah")
m1.nick_name = 'naks'
#print(m1.__dict__) #gives us a dictionary with the objects is the class

#GENERATORS
#help us loop and load large files of data, large enough to crush our work stations
#we can use generators to search for infinite elements in an infinite loop of possibilities
# a generator is a function that acts like an iterator
#generates the items we loop over by providing an iterableobject
#a generator can be thought of as an on-demand iterable object
#The difference between a generator and an iterator is that an iterator loops over objects in memory while generators provide on-demand iteration. its for this reason that generators are memory saving


def g():
  yield 1
  yield 2
  yield 3


#print(g())

# for i in g():
#   print(i)

#function that yields each lowercase letter in the english alphabet

import string  #provides methods for working with strings


def lower_case_letters():
  for l in string.ascii_lowercase:
    yield l


for letter in lower_case_letters():
  print(letter)

#a function that uses yield instead of return is known as a generator function or simply a generator for short
from itertools import count
def prime_numbers():
  #handle the first prime number 
  yield 2
  prime_cache=[2] #set up prime cache

  #loop over positive, odd integers
  for n in count(3,2):
    is_prime=True

    for p in prime_cache:
      if n%p==0:
        is_prime=False
        break

    if is_prime:
      prime_cache.append(n)
      yield n 

# for p in prime_numbers():
#   print(p)
#   if p>100:
#     break

#we can also use generator expressions to generate generator objects
#generator expressions are very similar to list comprehensions and just have only one difference which is generator expressions use parentheses

#thie generator expression generates the square of all positive integers
squares=(x**2 for x in count(1))

for x in squares:
  print(x)

  if x>500:
    squares.close()

#type(squares) will give us generator
