import CDatabaseManager

def SelectAll(dbm: CDatabaseManager, tableName: str):
  sql = ("SELECT * "
         "FROM ") + tableName
  dbm.Execute(sql)
  return dbm.Fetchall()


def SelectAllOf(dbm: CDatabaseManager, tableName: str, collumn: str, row: str):
  sql = ("SELECT * FROM ") + tableName + " WHERE " + collumn + "= '" + row + "'"
  dbm.Execute(sql)
  return dbm.Fetchall()


def Exists(dbm: CDatabaseManager, tableName: str, collumn: str, row: str):
  sql = ("SELECT EXISTS (SELECT " + 
          collumn + " FROM " + 
          tableName + " WHERE " + 
          collumn + "= '" + 
          row + "')")
  dbm.Execute(sql)
  flag = dbm.Fetchall()
  return flag[0][0]  # retarded tuple


def CustomSearch(dbm: CDatabaseManager, platform: str, genre: str, 
                      lowestPrice: str, highestPrice: str):
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