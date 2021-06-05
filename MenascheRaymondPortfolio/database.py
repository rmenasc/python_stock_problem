"""
   Author:             Raymond G. Menasche
   Date:               05/21/2021
   Version:            1.0
   Project Title:      Stocks with Databases and Data Vizualization
   File:               database.py
   Type:               Class Database API
"""

class Database:
  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()
  
  """
  Creates a new table if one does not exist.
  """  
  def create_new_table(self, table, fields):
    sql = "CREATE TABLE IF NOT EXISTS " + table + " ( id integer PRIMARY KEY "
    for field in fields:
      sql += ", " + field + " TEXT"
      
    sql += ");"
    
    try:
      self.cursor.execute(sql)
      self.conn.commit()
    except:
      print("Issue creating table")
  
  """
  Creates an Insert statement and passes the values to it. The values parameter is a
  dict containing {field name: value}
  """  
  def insert(self, table, values):
    sql = "INSERT INTO " + table + " ("
    placeholder = "?"
    counter = 0
    value_list = list()
    for key, value in values.items():
      if counter == 0: 
        sql += key
        value_list.append(value)
      else:
        sql += ", " + key
        placeholder += ", ?"
        value_list.append(value)
      counter += 1
      
    sql += ") VALUES (" + placeholder + ")"
    val = tuple(value_list)
    print(val)
    try:
      self.cursor.execute(sql, val)
      self.conn.commit()
    except:
      print("Exception during insert") #for de-bugging
      
      
  """
  Searches for a row with the parameters and values provided. The values paramenter is a
  dict containing {field name: value}
  """
  def search(self, table, values):
    sql = "SELECT * FROM " + table + " WHERE "
    placeholder = "?"
    counter = 0
    value_list = list()
    for key, value in values.items():
      if counter == 0:
        sql += key + " = " + placeholder
        value_list.append(value)
      else:
        sql += " AND " + key + " = " + placeholder
        value_list.append(value)
      counter += 1 
    val = tuple(value_list)
    print(sql)
    print(val)
    try:
      self.cursor.execute(sql, val)
      return self.cursor.fetchall()
    except:
      print("Exception during select ") #for de-bugging 
    
    
  """
  Updates an entry by passing the name of the table and the values. The values paramenter
  is a dict containing {field name: value}. The conditions parameter is also a dict that 
  places a field name and a value after the WHERE statement. The condition parameters are
  separated by an AND. This function does not support OR conditions. 
  """
  def update(self, table, values, conditions):
    sql = "UPDATE " + table + " SET "
    placeholder = "?"
    counter = 0
    value_list = list()
    for key, value in values.items():
      if counter == 0:
        sql += key + " = " + placeholder
        value_list.append(value)
      else:
        sql += ", " + key + " = " + placeholder
        value_list.append(value)
      counter += 1
    sql += " WHERE "
    counter = 0
    for key, value in conditions.items():
      if counter == 0:
        sql += key + " = " + placeholder
        value_list.append(value)
      else:
        sql += " AND " + key + " = " + placeholder
        value_list.append(value)
      counter += 1
    
    val = tuple(value_list)
    
    try:
      self.cursor.execute(sql, val)
      self.conn.commit()
    except:
      print("Exception during update") #for de-bugging
