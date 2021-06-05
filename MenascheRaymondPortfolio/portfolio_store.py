"""
   Author:             Raymond G. Menasche
   Date:               05/21/2021
   Version:            1.0
   Project Title:      Stocks with Databases and Data Vizualization
   File:               portfolio_store.py
   Type:               Class PortfolioStore
"""

class PortfolioStore:

    TABLE = "portfolios"
    FIELDS = ("owner_id")

    def __init__(self, db):
        self.db = db

    def insert(self, args):
        self.db.create_new_table(self.TABLE, self.FIELDS)
        values = { self.FIELDS[0]: args[0] }
        self.db.insert(self.TABLE, values)

    def update(self, args):
        values = { self.FIELDS[0]: args[0] }
        conditions = { "id": args[1] }
        self.db.update(self.TABLE, values, conditions)

    def search_portfolio(self, id):
        values = {"id": id}
        return self.db.search(self.TABLE, values)
