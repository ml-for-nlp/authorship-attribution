# Authorship attribution tutorial

This tutorial shows an example use of the Naive Bayes algorithm. The system is trained on five texts by four authors: Austen, Kipling, Carroll and Grahame. It is then required to guess the author of an additional text (which, spoiler, is by Jane Austen).


## Requirements

You'll need the docopt package to run the code.


## Run the code

To run the code, type:

    python3 attribution.py --words data/emma.txt

Or alternatively:

    python3 attribution.py --chars 3 data/emma.txt
