# Тестирование модуля:
#
# Напишите небольшую программу, которая импортирует модуль "portfolio.py"
# и демонстрирует использование всех трех функций.
# Создайте словари для акций и цен, запустите функции и выведите результаты.


__all__ = ['calculate_portfolio_value', 'calculate_portfolio_return', 'get_most_profitable_stock']


_initial_value = {}


# Расчет общей стоимости портфеля акций
def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    if len(_initial_value) == 0:
        for key, value in prices.items():
            _initial_value[key] = value
    sum_stocks = 0
    for key, value in stocks.items():
        sum_stocks += value * prices[key]
    return round(sum_stocks, 2)


# Расчет доходности портфеля
def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return round((current_value - initial_value) / initial_value * 100, 2)


# Определение наиболее прибыльной акции
def get_most_profitable_stock(prices: dict) -> str:
    res_dict = {key: value - _initial_value[key] for key, value in prices.items()}
    final_dict = max(res_dict.items(), key=lambda k_v: k_v[1])
    return final_dict[0]


if __name__ == "__main__":
    all_stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8, "TSLA": 7}
    prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50, "TSLA": 253.86}
    current_prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50, "TSLA": 503.86}
    res_initial_value = calculate_portfolio_value(all_stocks, prices)
    res_current_value = calculate_portfolio_value(all_stocks, current_prices)
    portfolio_return = calculate_portfolio_return(res_initial_value, res_current_value)
    profitable_stock = get_most_profitable_stock(all_stocks, current_prices)
    print(f"Общая стоимость портфеля акций = {res_initial_value}")
    print(f"Процентная доходность портфеля = {portfolio_return}%")
    print(f"Наиболее прибыльная акция = {profitable_stock}")
