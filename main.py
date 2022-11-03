coffee_prices =[('cappucino', 1.5),
               ('expresso',1.2),
               ('mocha',1.9)]

#problem #1 retrieve the coffee names and price from the above tuple. Make sure it is in a readable format(hint: f strings


for coffee, prices in coffee_prices:
  print(f"coffee:{coffee} and price {prices}")
  

  

# highest_coffee= (max(coffee_prices))



#create a function that iterates through the tuple list above and returns the highest priced coffee only. You probably want to create a function that has arguments  
# def coffee():
#   print("highest coffee is: ")
  
# print(highest_coffee)


 def most_expensive_coffee(coffee_prices):
  # establish what the highest prices are
  # my most expensive coffee_prices
  
  highest_price = 0
  my_most_expensive_coffee= ""
  for coffee, price in coffee_prices:
    if price > highest_price:
      highest_price = price
      my_most_expensive_coffee=coffee
      
  else:
    pass
  return(my_most_expensive_coffee,highest_price)
print(most_expensive_coffee(coffee_prices))


  
  






   




