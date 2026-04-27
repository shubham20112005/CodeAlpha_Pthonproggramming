def Investment():
    return stock[stock_name] * stock_quantity

stock = {"Apple inc": 180,"Microsoft":190,"Amazon":150,"tesla":200}
Total_investment = 0
file = open("stockdata.txt","w")
while True:
    stock_name = input("Enter stock name(use close to exit) ")
    if stock_name == "close":
        file.write(f"your total stock price = {Total_investment}\n")
        break
    stock_quantity = int(input("Enter stock quantity  "))
    Total_investment = Investment() + Total_investment
    file.write(f"{stock_name} = {stock[stock_name]}\n")
    
file.close()