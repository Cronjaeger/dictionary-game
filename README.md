# dictionary-game
Play the dictionary game (or variants thereof) in your browser.


## What is The Dictionaty Game?
[The Dictionary Game](https://en.wikipedia.org/wiki/Fictionary) is a simple parlour game played with a dictionary and a group of players over a number of rounds. Each round occurs in two phases. In the first phase, a word is chosen from the dictionary (typically picked at random or chosen by a player who does not themself take part in that round) and read out to the players whereafter players are given the word (but not the definition of the word) and asked to compose a definition of the word. These definitions are then written down and anonymously put in a hat (or some other suitable vessel) together with the real definition (typically written down by the player who chose the word). In the second phase, all candidate definitions are read out, and each player must make a guess as to which of the definitions presented to them is the real one. Players score points at the end of each round according to the following rules:
  * Each player who correctly identifies the dictionary definition scores one point.
  * If a player's guess is incorrect, the author of the definition that fooled them scores an additional point.
The game typically proceeds over a set number of rounds after which whoever has the most points is considered the winner.

## What is in this software repository?
This project intends to implement the dictionary game in a modular fashion. Currently, the roadmap is to produce the following:

* A backend that can run on a web-server and host an instance of the game.
* A web-browser front-end that allows players to connect to an instance of the game and play against each other
* An example dictionary-service that provides words and definitions to the backend through a simple REST API. (If you want to implement a version of the game based on a different source of terms and definitions, this is the bit that should be re-implemented.)

## What is the project status?
Nothing has been implemented yet. Currently the roadmap is to implement the following:

  * a dictionary service. Currently the plan is to implement whatever is easiest to implement of the following
    * Titles and First sentences from Wikipedia articles
    * Terms and definitions from urbandictionary.com
    * Terms and definitions from some old dictionary out of print (e.g. an old digitized version of Webster's)
  * the backend game-server
  * a simple browser-based frontend
