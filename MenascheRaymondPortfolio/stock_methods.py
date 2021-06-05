"""
   Author:             Raymond G. Menasche
   Date:               05/08/2021
   Version:            1.0
   Project Title:      Stock Problem with Objects and Files
   File:               stock_methods.py
   Type:               Class
"""
from datetime import datetime

class StockMethods:


    # Takes purchase price(float), current price(float) and quantity(int) to calculate gain or loss
    # Returns: float with gain/loss amount.
    def calculate_gain_loss(self, p_price, c_price, quantity):
        total = (c_price - p_price) * quantity
        return total

    # Takes purchase price(float) and current price(float) to calculate total percentage yield/loss
    # Returns: float with percentage amount. 
    def calculate_percentage_yield(self, p_price, c_price):
        total = (c_price * 100) / p_price
        return total - 100

    # Takes purchase price(float), current price(float), and date(string) to caluculate yearly yield/loss
    # Returns: float with percentage amount. 
    def calculate_yearly_earning_loss(self, p_price, c_price, date):
        date_difference = self.get_date_difference(datetime.now(), date)
        total = ((((c_price - p_price)/p_price)/ date_difference)) * 100
        return total

    # Takes two dates to calculate days between
    # Returns: int with number of days between.
    def get_date_difference(self, date1, date2):
        date_dif = str(date1 - date2)
        temp_list = date_dif.split(" ")
        return int(temp_list[0])

    # Takes a portfolio and displays it after perfroming methods.
    def display_results(self, portfolio):
        stock_dict = portfolio.holdings
        float_format = "{0:.2f}"
        output = f"Stock Ownership for { portfolio.owner.first_name } { portfolio.owner.last_name }\n"
        output += "Stock\tShare #\tEarnings/Loss\tYearlyEarning/Loss\n"
        for key, value in stock_dict.items():
            output += f"{ key }\t{ value.num_shares }\t"
            earn_loss = self.calculate_gain_loss(value.stock.purchase_price,
                                            value.stock.current_price,
                                            value.num_shares)
            output += f"${ float_format.format(earn_loss) }\t\t"
            yearly_percentage = self.calculate_yearly_earning_loss(value.stock.purchase_price,
                                                              value.stock.current_price,
                                                              value.purchase_date)
            output += f"{ float_format.format(yearly_percentage * 100) }%\n"
        return output
