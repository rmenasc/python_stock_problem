"""
   Author:             Raymond G. Menasche
   Date:               05/08/2021
   Version:            1.0
   Project Title:      Stock Problem with Objects and Files
   File:               holding.py
   Type:               Class
"""
from datetime import datetime

class Holding:

    def __init__(self, holding_id, stock, num_shares, purchase_date):
        self.holding_id = holding_id
        self.stock = stock
        self.num_shares = num_shares
        self.purchase_date = purchase_date
