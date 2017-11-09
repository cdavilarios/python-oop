## Curse about Object Oriented Programming with Python
## Refered to https://github.com/gersongams/python-course/blob/master/Chapter%206%20-%20Object%20Oriented%20Programming.ipynb

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduceyourself(self):
        print("My name is " + self.name)
        print("My age is " + str(self.age))
    def ismale(self):
        if self.gender == "M":
            print(True)
        else:
            print(False)


class Teacher(Person): #this class inherits the class above!
    def stateprofession(self):
        print("I am a teacher!")

author = Teacher("Maarten",30,"F")
author.introduceyourself()
author.ismale()

author.stateprofession()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduceyourself(self):
        print("My name is " + self.name)
        print("My age is " + str(self.age))


## Inheritance *

class Teacher(Person): #this class inherits the class above!
    def __init__(self, name, age):
        self.courses = [] #initialise a new variable
        super().__init__(name,age) #call the init of Person

    def stateprofession(self):
        print("I am a teacher!")

    def introduceyourself(self):
        super().introduceyourself() #call the introduceyourself() of the Person
        self.stateprofession()
        print("I teach " + str(self.nrofcourses()) + " course(s)")
        for course in self.courses:
            print("I teach " + course)

    def addcourse(self, course):
        self.courses.append(course)

    def nrofcourses(self):
        return len(self.courses)


author = Teacher("Maarten",30)
author.addcourse("Python")
author.introduceyourself()

## Operator overloading

class Tweet:
    def __init__(self, message, time):
        self.message = message
        self.time = time # we will assume here that time is a numerical value

    def __lt__(self, other): # lower than
        return self.time < other.time

    def __gt__(self, other): # greater than
        return self.time > other.time


oldtweet = Tweet("this is an old tweet",20)
newtweet = Tweet("this is a new tweet",1000)
print(newtweet > oldtweet)

tweets = [newtweet,oldtweet]

for tweet in sorted(tweets):
    print(tweet.message)

help(sorted)

## IN OPERATOR

class Tweet:
    def __init__(self, message, time):
        self.message = message
        self.time = time

    def __lt__(self, other):
        return self.time < other.time

    def __contains__(self, word):
        return word in self

tweet = "I just flushed my toilet"
if 'flushed' in tweet:
    print("it is in the tweet!")
# print now write code to check if the word "flushed" is in the tweet
#and print something nice if that's the case

## Iteration over an object


class TwitterUser:
    def __init__(self, name):
        self.name = name
        self.tweets = [] #This will be a list of all tweets, these should be Tweet objects

    def append(self, tweet):
        assert isinstance(tweet, Tweet) #this code will check if tweet is an instance
                                        #of the Tweet class. If not, an exception
                                        #will be raised
        #append the tweet to our list
        self.tweets.append(tweet)

    def __iter__(self):
        for tweet in sorted(self.tweets):
            yield tweet

    def __len__(self):
        return len(self.tweets)


tweeter = TwitterUser("proycon")
tweeter.append(Tweet("My peanut butter sandwich has just fallen bottoms-down",4))
tweeter.append(Tweet("Tying my shoelaces",2))
tweeter.append(Tweet("Wiggling my toes",3))
tweeter.append(Tweet("Staring at a bird",1))

for tweet in tweeter:
    print(tweet.message)

print(len(tweeter) == 4)
