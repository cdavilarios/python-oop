#! /usr/bin/env python3
# -*- coding: utf8 -*-

import sys
import preprocess


class Tweet:
    def __init__(self, message, time):
        self.message = message
        self.time = time


class TwitterUser:
    def __init__(self, name):
        self.name = name
        self.tweets = [] #This will be a list of all tweets
        self.relations = {} #This will be a dictionary in which the keys are
                            #TwitterUser objects and the values are the weight of the relation (an integer)

    def append(self, tweet):
        assert isinstance(tweet, Tweet) #this is a test, if tweet is not an instance
                                        #of Tweet, it will raise an Exception.
        self.tweets.append(tweet)

    def __iter__(self):
        # This function, a generator, should iterate over all tweets
        for tweet in sorted(self.tweets)
            yield tweet


    def __hash__(self):
        #For an object to be usable as a dictionary key, it must have a hash method. Call the hash() function over something that uniquely defined this object
        #and thus can act as a key in a dictionary. In our case, the user name is good, as no two users will have the same name:
        return hash(self.name)


    def addrelation(self, user):
        if user and user != self.name: #user must not be empty, and must not be the user itself
            if user in self.relations:
                #the user is already in our relations, strengthen the bond:
                self.relations[user] += 1
            elif user in graph:
                #the user exists in the graph, we can add a relation!
                self.relations[user] = 1
            #if the user does not exist in the graph, no relations will be added


    def computerelations(self, graph):
        for tweet in self:
            #tokenise the actual tweet content (use the tokeniser in preprocess!):
            tokens = #<INSERT YOUR CODE HERE>

            #Search for @username tokens, extract the username, and call self.addrelation()
            #<INSERT YOUR CODE HERE>


    def printrelations(self):
        #print the relations, include both users and the weight
        #<INSERT YOUR CODE HERE>


    def gephioutput(self):
        #produce CSV output that gephi can import
        for recipient, weight in self.relations.items():
            for i in range(0, weight):
                yield self.name + "," + recipient


class TwitterGraph:
    def __init__(self, corpusdirectory):
        self.users = {} #initialisation of dictionary that will store all twitter users. They keys are the names, the values are TwitterUser objects.
                        #the keys are the usernames (strings), and the values are
                        # TweetUser instances

        #Load the twitter corpus
        #tip: use preprocess.find_corpusfiles and preprocess.read_corpus_file,
        #do not use preproces.readcorpus as that will include sentence segmentation
        #which we do not want

        #Each txt file contains the tweets of one user.
        #all files contain three columns, separated by a TAB (\t). The first column
        #is the user, the second the time, and the third is the tweetmessage itself.
        #Create Tweet instances for every line that contains a @ (ignore other lines
        #to conserve memory). Add those tweet instances to the right TweetUser. Create
        #TweetUser instances as new users are encountered.

        #self.users[user], which user being the username (string), should be an instance of the
        #of TweetUser

        #<INSERT YOUR CODE HERE>


        #Compute relations between users
        for user in self:
            assert isinstance(user,TweetUser)
            user.computerelations(self)



    def __contains__(self, user):
        #Does this user exist?
        return user in self.users

    def __iter__(self):
        #Iterate over all users
        for user in self.users.values():
            yield user

    def __getitem__(self, user):
        #Retrieve the specified user
        return self.users[user]


#this is the actual main body of the program. The program should be passed one parameter
#on the command line: the directory that contains the *.txt files from twitterdata.zip.

#We instantiate the graph, which will load and compute all relations
twittergraph = TwitterGraph(sys.argv[1])

#We output all relations:
for twitteruser in twittergraph:
    twitteruser.printrelations()

#And we output to a file so you can visualise your graph in the program GEPHI
f = open('gephigraph.csv','wt',encoding='utf-8')
for twitteruser in twittergraph:
    for line in twitteruser.gephioutput():
        f.write(line + "\n")
f.close()

import preprocessor
cleaned_tweet = preprocessor.clean("Preprocessor is #awesome https://github.com/s/preprocessor")
