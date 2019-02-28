# Authorship attribution tutorial

This tutorial shows an example use of the Naive Bayes algorithm. The system is trained on five texts by four authors: Austen, Kipling, Carroll and Grahame. It is then required to guess the author of an additional text (which -- spoiler alert -- is Jane Austen's *Emma*).


## Requirements

You'll need the docopt package to run the code. If you're on PythonAnywhere, this will be installed by default. If you need to install it on your system, do:

    sudo pip3 install docopt


## Run the code

To run the code, type:

    python3 attribution.py --words data/emma.txt

Or alternatively:

    python3 attribution.py --chars 3 data/emma.txt

The first alternative computes a model over words, as we saw in class. The second alternative uses character ngrams of the size given to the system.

The output of the code tells you which operations the classifier is currently performing: computing prior probabilities, conditional probabilities, etc. Then, for illustration, it outputs the 10 features with highest conditional probability for the class under consideration (i.e. for each author). It gives you an idea of which words / ngrams are most important for each author. Finally, you get sorted log figures for the probability of each class. The first entry in that list is the author guessed by the system.


## Try it out

Change parameters and see what happens! What do you get with longer ngrams? Can you interpret the output? Does the system still perform the way you expect?


## Obfuscation

The opposite of authorship attribution is obfuscation. You are Jane Austen and you don't want to have your texts identify you. What can you do to prevent this? Try out different methods and see if you can fool the system.
