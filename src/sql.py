import CDatabaseManager

def select_all(dbm: CDatabaseManager, tableName: str):
  sql = ("SELECT * "
         "FROM ") + tableName
  dbm.Execute(sql)
  return dbm.Fetchall()


def select_all_of(dbm: CDatabaseManager, tableName: str, collumn: str, row: str):
  sql = ("SELECT * FROM ") + tableName + " WHERE " + collumn + "= '" + row + "'"
  dbm.Execute(sql)
  return dbm.Fetchall()


def exists(dbm: CDatabaseManager, tableName: str, collumn: str, row: str):
  sql = ("SELECT EXISTS (SELECT " + 
          collumn + " FROM " + 
          tableName + " WHERE " + 
          collumn + "= '" + 
          row + "')")
  dbm.Execute(sql)
  flag = dbm.Fetchall()
  return flag[0]  # retarded tuple