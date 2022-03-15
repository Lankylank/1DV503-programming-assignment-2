import CDatabaseManager


def Select(dbm: CDatabaseManager, tableName: str, thisCollumn: str) -> list:
  sql = "SELECT " + thisCollumn + " FROM " + tableName
  dbm.Execute(sql)
  return dbm.Fetchall()


def SelectThis(dbm: CDatabaseManager, tableName: str, thisCollumn: str, whereCollumn: str, this: str) -> list:
  sql = "SELECT " + thisCollumn + " FROM " + tableName + " WHERE " + whereCollumn + "= '" + this + "'"
  dbm.Execute(sql)
  return dbm.Fetchall()


# Bad function name
def SelectMany(dbm: CDatabaseManager, tableName: str, selectCollumns: list, whereCollumn: str, this: str) -> list:
  collumns = str()
  for collumn in selectCollumns:
    collumns += collumn + ","
  collumns = collumns.removesuffix(",")
  

  sql = "SELECT " + collumns + " FROM " + tableName + " WHERE " + whereCollumn + "= '" + this + "'"
  dbm.Execute(sql)
  return dbm.Fetchall()


def SelectAll(dbm: CDatabaseManager, tableName: str, column: str) -> list:
  sql = ("SELECT * "
         "FROM " + tableName +
         " ORDER BY " + column + " ASC")
  dbm.Execute(sql)
  return dbm.Fetchall()


# Variable names might be wrong
def SelectAllOf(dbm: CDatabaseManager, tableName: str, collumn: str, this: str) -> list:
  sql = ("SELECT * FROM ") + tableName + " WHERE " + collumn + "= '" + this + "'"
  dbm.Execute(sql)
  return dbm.Fetchall()


# Incorrect function name
def SelectAllDistinct(dbm: CDatabaseManager, selectColumn: str, tableName: str):
  sql = ("SELECT DISTINCT " + selectColumn + " FROM " + tableName + " ORDER BY " + selectColumn + " ASC")
  dbm.Execute(sql)
  return dbm.Fetchall()


def SelectDistinctBetween(dbm: CDatabaseManager, tableName: str, collumn: str, whereCollumn: str, min: str, max: str) -> list:

  sql = ("SELECT DISTINCT " + collumn + " FROM " + tableName + " WHERE " + whereCollumn + " BETWEEN " + min + " AND " + max)

  dbm.Execute(sql)
  return dbm.Fetchall()


def Exists(dbm: CDatabaseManager, tableName: str, collumn: str, row: str) -> bool:
  sql = ("SELECT EXISTS (SELECT " + 
          collumn + " FROM " + 
          tableName + " WHERE " + 
          collumn + "= '" + 
          row + "')")
  dbm.Execute(sql)
  flag = dbm.Fetchall()
  return flag[0][0]  # retarded tuple


##############################################################################################


def CustomSearch(dbm: CDatabaseManager, platform: str, genre: str, 
                      lowestPrice: str, highestPrice: str) -> list:
                      # FORMAT, return only a title
  sql = ("SELECT DISTINCT title_table.title "
        "FROM title_table "
        "JOIN title_platform_table USING (title) "
        "JOIN title_genre_table USING (title) "
        "JOIN title_game_store_table USING (title) "
        "WHERE title_platform_table.platform = '" + platform + "' "
        "AND title_genre_table.genre = '" + genre + "' "
        "AND title_game_store_table.price "
        "BETWEEN "+ lowestPrice + " AND " + highestPrice + " ") # BETWEEN is inclusive

  dbm.Execute(sql)
  return dbm.Fetchall()


# This uses all junction tables so copy pasted from test1
def GameVerbose(dbm: CDatabaseManager, game: str):
  sql = ("SELECT title_table.*, "
        "GROUP_CONCAT(DISTINCT(title_genre_table.genre) SEPARATOR ', '), "
        "GROUP_CONCAT(DISTINCT(title_platform_table.platform) SEPARATOR ', '), "
        "GROUP_CONCAT(DISTINCT(title_game_store_table.game_store) SEPARATOR ', '), "
        "price_statistics.min, price_statistics.max, price_statistics.avg "
        "FROM title_table "
        "JOIN title_genre_table USING (title) "
        "JOIN title_platform_table USING (title) "
        "JOIN title_game_store_table USING (title) "
        "JOIN price_statistics USING (title) "
        "WHERE title_table.title = '" + game + "'"
        "GROUP BY title_table.title")

  dbm.Execute(sql)
  return dbm.Fetchall()


def GameBasic(dbm: CDatabaseManager, game: str):
  sql = ("SELECT title_table.*, "
       "price_statistics.avg "
       "FROM title_table "
       "JOIN price_statistics USING (title) "
       "WHERE title_table.title = '" + game + "'")
  
  dbm.Execute(sql)
  return dbm.Fetchall()