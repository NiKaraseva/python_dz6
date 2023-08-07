import portfolio


stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8, "TSLA": 7}
prices_initial = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50, "TSLA": 253.86}
prices_current = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50, "TSLA": 503.86}


initial_value_res = portfolio.calculate_portfolio_value(stocks, prices_initial)
current_value_res = portfolio.calculate_portfolio_value(stocks, prices_current)
return_portfolio = portfolio.calculate_portfolio_return(initial_value_res, current_value_res)
most_stock_profitable = portfolio.get_most_profitable_stock(prices_current)


print(f"Начальная стоимость портфеля акций = {initial_value_res}")
print(f"Текущая стоимость портфеля акций = {current_value_res}")
print(f"Процентная доходность портфеля = {return_portfolio}%")
print(f"Наиболее прибыльная акция = {most_stock_profitable}")