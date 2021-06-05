"""
   Author:             Raymond G. Menasche
   Date:               05/21/2021
   Version:            1.0
   Project Title:      Stocks with Databases and Data Vizualization
   File:               holding_store.py
   Type:               Class HoldingStore
"""

class HoldingStore:

    TABLE = "holdings"
    FIELDS = ("stock_id", "num_shares", "purchase_date")

    def __init__(self, db):
        self.db = db

    def insert(self, args):
        self.db.create_new_table(self.TABLE, self.FIELDS)
        values = {
            self.FIELDS[0]: args[0],
            self.FIELDS[1]: args[1],
            self.FIELDS[2]: args[2]}
        self.db.insert(self.TABLE, values)

    def update(self, args):
        values = {
            self.FIELDS[0]: args[0],
            self.FIELDS[1]: args[1],
            self.FIELDS[2]: args[2]}
        conditions = {"id": args[3]}
        self.db.update(self.TABLE, values, conditions)

    def search_holding(self, id):
        values = {"id": id}
        return self.db.search(self.TABLE, values)
