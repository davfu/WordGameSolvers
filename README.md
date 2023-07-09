# Word Game Solvers
A series of solvers for the popular 2-player iMessage games Anagrams, Word Hunt, and Word Bites.  

# Introduction
Anagrams is a word game where each player is given 6 alphabetical characters and asked to create as many words as possible.  The longer the word, the more points the player recieves.  The player with the most points in under 60 seconds wins the game.

<img width="310" alt="Screenshot 2023-07-08 at 5 07 40 PM" src="https://github.com/davfu/wordgamesolvers/assets/87512091/ca8f09f0-b9e3-4cd0-b2fc-1f92d58ea0c9">

Word Hunt is a game where each player is given a 4x4 board of alphabetical characters and asked to draw their finger along the board to construct as many words as possible.  The longer the word, the more points the player recieves.  The player with the most points in under 80 seconds wins the game.

<img width="307" alt="Screenshot 2023-07-08 at 5 10 15 PM" src="https://github.com/davfu/wordgamesolvers/assets/87512091/984e68ea-e35d-4c59-9ac9-3a7377132ccd">

Word Bites is a game where each player is given a 9x9 board with an assortment of 2x1, 1x2, or 1x1 tiles of characters.  The players are asked to drag the tiles together to create as many words as possible.  The longer the word, the more points the player recieves.  The player with the most points in under 90 seconds wins the game.  

<img width="309" alt="Screenshot 2023-07-08 at 5 16 18 PM" src="https://github.com/davfu/wordgamesolvers/assets/87512091/f96a29a4-4905-4d23-a602-548fd786002c">

# How It Works
For each game, the program constructs any and all combinations of the characters using a recursive Depth First Search algorithm.  However, for efficiency purposes, the program checks if the current partial string is the prefix of any existing words stored in a Trie data structure (consisting of 80,272 words) before calling the recursive function to extend the current partial string.  Once the program has found a valid word (by checking if it exists in the Trie) the word is added to a set of valid words found.  

# How To Use
1. Download the Github Repository
2. aa
3. Select which game you are playing (1 for Anagrams, 2 for Word Hunt, 3 for Word Bites)
4. Input the board:
   
   ~ 6 character string for Anagrams 
   
   ~ 16 character string for Word Hunt (from left to right, top to bottom)
   
   ~ Each 1x1, 2x1, and 1x2 character tiles for Word Bites
5. Input the solutions to the game !!! Easy dubs let's gOOO !!!

