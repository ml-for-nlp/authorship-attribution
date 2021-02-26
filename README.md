# Authorship attribution tutorial

This tutorial shows an example use of the Naive Bayes algorithm. The system is trained on five texts by four authors: Austen, Kipling, Carroll and Grahame. It is then required to guess the author of an additional text (which -- spoiler alert -- is Jane Austen's *Emma*).


## Requirements

You'll need the docopt package to run the code from the terminal. If you need to install it on your system, do:

    sudo pip3 install docopt


## Run the code

To run the code, type:

    python3 attribution.py --words data/emma.txt

Or alternatively:

    python3 attribution.py --chars 3 data/emma.txt

The first alternative computes a model over words, as we saw in class. The second alternative uses character ngrams of the size given to the system.

The output of the code tells you which operations the classifier is currently performing: computing prior probabilities, conditional probabilities, etc. Then, for illustration, it outputs the 10 features with highest conditional probability for the class under consideration (i.e. for each author). It gives you an idea of which words / ngrams are most important for each author. Finally, you get sorted log figures for the probability of each class. The first entry in that list is the author guessed by the system.


## Exercises

* First, read the code and make sure you understand what it does. If it helps you, you can add comments in the file.

* Can you interpret the output? Just looking at the most frequent words/ngrams, what do you notice about the similarities and differences between authors?

* Change parameters and see what happens! What do you get with longer ngrams? What happens if you modify the smoothing parameter alpha?


## Write up your experiments

Write a little report of what you've done (this is just practice for the exam!) Your report should contain the following sections:

* Description of the task
* Your hypothesis: it could be anything you like. You can keep it simple. For instance, you might posit that the system will not work so well anymore if you choose very long char ngrams (it will overfit to the particular book in the training set and not generalise to the test book).
* The experiments you ran: which parameters did you change? did you modify the system? Explain everything you did in detail.
* Results: write a little table showing your results and discuss it with respect to your hypothesis. Was it confirmed or disproved?


## Open-ended project

For those who want to go further... The opposite of authorship attribution is obfuscation. You are Jane Austen and you don't want to have your texts identify you. What can you do to prevent this? Try out different methods and see if you can fool the system.
