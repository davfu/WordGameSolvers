# Word Game Solvers
A series of solvers for the popular 2-player iMessage games Anagrams, Word Hunt, and Word Bites.  

# Introduction
Anagrams is a word game where each player is given 6 alphabetical characters and asked to create as many words as possible.  The longer the word, the more points the player recieves.  The player with the most points in under 60 seconds wins the game.

Word Hunt is a game where each player is given a 4x4 board of alphabetical characters and asked to draw their finger along the board to construct as many words as possible.  The longer the word, the more points the player recieves.  The player with the most points in under 80 seconds wins the game.

Word Bites is a game where each player is given a 9x9 board with an assortment of 2x1, 1x2, or 1x1 tiles of characters.  The players are asked to drag the tiles together to create as many words as possible.  The longer the word, the more points the player recieves.  The player with the most points in under 90 seconds wins the game.  

<img width="250" alt="Screenshot 2023-07-08 at 5 16 18 PM" src="https://github.com/davfu/wordgamesolvers/assets/87512091/f96a29a4-4905-4d23-a602-548fd786002c">

# How It Works
For each game, the program constructs any and all combinations of the characters using a recursive Depth First Search algorithm.  However, for efficiency purposes, the program checks if the current partial string is the prefix of any existing words stored in a Trie data structure (consisting of 80,272 words) before calling the recursive function to extend the current partial string.  Once the program has found a valid word (by checking if it exists in the Trie) the word is added to a set of valid words found.  

# Examples:
# Anagrams:
Anagrams given board:

<img width="250" alt="Screenshot 2023-07-08 at 5 16 18 PM" src=https://github.com/davfu/wordgamesolvers/assets/87512091/2404b16c-a548-42f3-8023-8cbc746ca6d7>

Input the board and receive a list of valid words:

<img width="500" alt="Screenshot 2023-07-08 at 10 26 07 PM" src="https://github.com/davfu/wordgamesolvers/assets/87512091/4046c22d-53f4-47b0-bbac-73ea0d618168">

Create the words in Anagrams and easy wins let's goOOOO !!!

<img width="250" alt="Screenshot 2023-07-08 at 5 16 18 PM" src=https://github.com/davfu/wordgamesolvers/assets/87512091/c25e4226-9894-496a-ac47-c6189b20918a>

# Word Hunt
Word Hunt given board:

<img width="250" alt="ss wordhunt board" src=https://github.com/davfu/wordgamesolvers/assets/87512091/e4060c93-47f4-4ee1-85b2-093cc1ecafbe>

Input the board and receive a list of valid words:

<img width="500" alt="Screenshot 2023-07-08 at 10 24 07 PM" src="https://github.com/davfu/wordgamesolvers/assets/87512091/ef9fb62a-0de6-43d3-9064-63f089fbb9e5">

Create the words in Word Hunt and easy easy dubs let's GOOOOOOO !!!!

<img width="250" alt="ss wordhunt find" src=https://github.com/davfu/wordgamesolvers/assets/87512091/b3343e58-3fbb-4307-baa4-1abf5fc034ab>

# Word Bites
Word Bites given board:

<img width="250" alt="wordbites board" src=https://github.com/davfu/wordgamesolvers/assets/87512091/af0c594f-741a-45cc-9863-1b424d575c33>

Input the board and receive a list of valid words:

<img width="500" alt="wordbites output" src=https://github.com/davfu/wordgamesolvers/assets/87512091/6b210e0b-a6d0-4961-9a64-c2776d93d089>

Ouput:

<img width="500" alt="wordbites input" src=https://github.com/davfu/wordgamesolvers/assets/87512091/7bdcba64-bd1b-4426-86f1-b2ca12489528>

WE TAKE THESE DUBS LGGG !!!!!

<img width="250" alt="wordbites win" src=https://github.com/davfu/wordgamesolvers/assets/87512091/62892cb9-a7cf-4735-8903-9013d35e2883>
