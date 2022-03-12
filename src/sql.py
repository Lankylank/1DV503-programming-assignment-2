import CDatabaseManager

def select_all(dbm: CDatabaseManager, tableName: str):
  sql = ("SELECT * "
         "FROM ") + tableName
  dbm.Execute(sql)
  return dbm.Fetchall()