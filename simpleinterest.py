print("Simple Interest")
principal= float(input("Provide Principal"))
rate_of_interest= float(input("Provide rate of Interest in %"))
time= int(input("Provide the duration of the loan in years"))
si = principal*rate_of_interest*time/100
print(si)