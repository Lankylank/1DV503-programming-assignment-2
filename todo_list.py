

#######  QUERIES  ########
# Remove TODO after it is completed
'''3 queries where we use atleast 2 multirelational queries'''
#TODO - 1
#TODO - 2
#TODO - 3

'''Make use of SQL JOIN'''
#TODO


'''Use Aggregation , do some calculation (calculating avg of something)'''
#TODO
# Example calculate avg price for a specific game.
# Extra if time allows: calculate procentage to easier compare game prices  


'''Grouping, use columns from different tables'''
#TODO
# Maybe incorporate grouping when creating our View table?


'''Create and use a View'''
#TODO


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



