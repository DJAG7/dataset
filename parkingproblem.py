#Taking input of the number of cars and bikes
cars=int(input("Number of Cars"))
bikes=int(input("Number of Bikes"))

#Calculating Collection
cars_cost= 20
bikes_cost= 10
total_cost=(cars*cars_cost)+(bikes*bikes_cost)

#Result, Checking if it was a good day or a bad day

if (total_cost>10000):
    print("Its a good Day. Parking funds generated for the day is "+ str(total_cost))

else: 
    print("It is a bad Day. Parking funds generated for the day is "+ str(total_cost))