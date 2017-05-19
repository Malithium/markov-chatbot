------------------------------------------------------------------------------------------------
1. Installation
------------------------------------------------------------------------------------------------
In order to run this program, you will need to have python 3+ installed on your machine
you will then have to install the NLTK library onto your machine using pip:

> pip install nltk

once installed open the python interpreter and do the following:

> import nltk
> nltk.download()

this will bring up the GUI for the NLTK downloader, you will want to install the following dependencys:

 - averaged_perceptron
 - punkt
 - universal_tagset

This should be all that is needed to run the program, the NLTK will ask you to download any packages should
the above not be sufficent

-------------------------------------------------------------------------------------------------
2. Running the program
-------------------------------------------------------------------------------------------------
We need to generate a 'brain.json' in order to chat to the chat bot, open the python interpreter where the
python scripts are located. do the following:

> import toJson
> toJson.createMarkovChain("a text file name")

this will begin the process of building the brain.json file, this process requires user input. once the 
brain.json has been generated we can use it in our chatbot, to start talking to the chatbot do the following:

> from chat import chatBot
> t = chatBot("Brain.json")
> t.chat()

You should now be able to talk to the chatbot

---------------------------------------------------------------------------------------------------
3. Provided resources
---------------------------------------------------------------------------------------------------
There is a folder called 'TextFiles' that contains the textual media used in developing and testing 
this program. The source URLS for this media is below

https://www.gutenberg.org/wiki/Main_Page. Last accessed 18/05/2017
http://www.imsdb.com/. Last accessed 18/05/2017