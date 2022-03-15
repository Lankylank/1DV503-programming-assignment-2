

#######  QUERIES  ########
# Remove TODO after it is completed
'''3 queries where we use atleast 2 multirelational queries'''
#TODO - 2
#TODO - 3


'''Grouping, use columns from different tables'''
#TODO
# Maybe incorporate grouping when creating our View table?



#############################################################
#############################################################
############################################################

####### RELATIONS  ########
# TABLE_NAME   ---   RELATION_NAME     ---     TABLE_NAME
'''game'''        '''price'''                 '''store'''
'''game'''        '''game_genre'''            '''genre'''
'''game'''        '''game_platform'''         '''platform'''


########  TABLES  #########  
#####################################################
# game_information
'''(PK) game_title'''  '''year'''   '''publisher'''
#####################################################
##########################
# game_store
'''(PK) store_name'''
##########################
#######################
# genre
'''(PK) genre_name'''
#######################
#########################
# platform
'''(PK) platform '''
########################

# game_platform
'''(FK) game_title'''  '''(FK) platform'''

# price
'''(FK) game_title'''  '''(FK)store_name'''

# game_genre
'''(FK) game_title'''  '''(FK) genre_name'''





'''
Option 0.
----------
1. [Option]: --custom search.--
2. ask for users input
    2.1 choose platform
    2.2 choose genre
    2.3 choose price range
3. print result
4. ask for user input
    4.1. [Option]: choose a game from the results
        4.1.1 get all info about game
        4.1.2. get price/store info
        4.1.3. get genre
        4.1.4. get platform
        4.1.5. get publiser/year (published 2019 by "publisher name")
    4.2 [Option]: return to menu 


Option 1.    --list all game in the database.--
---------  

1. [Option]: list all game in the database.
2. print results
3. Ask for user input
  3.1. [Option]: Choose a game from the results
       3.1.1. get all info about the game
       3.1.2. get price/store info
       3.1.3. get genre
       3.1.4. get platform
       3.1.5. get publiser/year (published year 2019 by "publisher name")
  3.2. [Option]: return to menu


Option 2.    --get all info of a game--
---------  

1. [Option]: get all info of a game
2. Ask for user input
    2.1 provide a game name
3. print results
4. [Option]: return to menu


Option 3.   --List all games within a give price range--
---------

1. [Option]: List all games within a give price range
2. Ask for user input
    2.1 lowestPrice
    2.2 highestPrice
3. print result
4. Ask for user input
      4.1. [Option]: Choose a game from the results
          4.1.1. get all info about the game
          4.1.2. get price/store info
          4.1.3. get genre
          4.1.4. get platform
          4.1.5. get publiser/year (published year 2019 by "publisher name")
      4.2. [Option]: return to menu

Option 4.   --list all games from a specific year--
--------

1. [Option]: list all games from a specific year
2. Ask for user input
    2.1 provide a year
3. print results
4. Ask for user input
      4.1. [Option]: Choose a game from the results
          4.1.1. get all info about the game
          4.1.2. get price/store info
          4.1.3. get genre
          4.1.4. get platform
          4.1.5. get publiser/year (published year 2019 by "publisher name")
      4.2. [Option]: return to menu


Option 5.   --list all games from a specific publisher--
--------

1. [Option]: list all games from a specific publisher
2. show all publishers available
3. Ask for user input
    2.1 provide a publisher
4. print results
5. Ask for user input
      5.1. [Option]: Choose a game from the results
          5.1.1. get all info about the game
          5.1.2. get price/store info
          5.1.3. get genre
          5.1.4. get platform
          5.1.5. get publiser/year (published year 2019 by "publisher name")
      6.2. [Option]: return to menu



Option 6.  --list all games from a specific platform--
--------

1. [Option]: list all games from a specific platform
2. show all platforms available
3. Ask for user input
    2.1 provide a platform
4. print results
5. Ask for user input
      5.1. [Option]: Choose a game from the results
          5.1.1. get all info about the game
          5.1.2. get price/store info
          5.1.3. get genre
          5.1.4. get platform
          5.1.5. get publiser/year (published year 2019 by "publisher name")
      6.2. [Option]: return to menu



Option 7.  -- list all games from a specific genre--
--------

1. [Option]: list all games from a specific genre
2. show all genre's available
3. Ask for user input
    2.1 provide a genre
4. print results
5. Ask for user input
      5.1. [Option]: Choose a game from the results
          5.1.1. get all info about the game
          5.1.2. get price/store info
          5.1.3. get genre
          5.1.4. get platform
          5.1.5. get publiser/year (published year 2019 by "publisher name")
      6.2. [Option]: return to menu

Option 8.   --list all games from a specific store--
--------

1. [Option]: list all games from a specific store
2. show all stores available
3. Ask for user input
    2.1 provide a store name
4. print results
5. Ask for user input
      5.1. [Option]: Choose a game from the results
          5.1.1. get all info about the game
          5.1.2. get price/store info
          5.1.3. get genre
          5.1.4. get platform
          5.1.5. get publiser/year (published year 2019 by "publisher name")
      6.2. [Option]: return to menu


'''