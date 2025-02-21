salary=int(input("input your salary for the month: "))
month=input(" input the name of the month you are storing the salary for: ")
savingsPercent=int(input("input the percentage for savings:"))
rentPercent=int(input("input the percentage for rent: "))
electPercent=int(input("input the percentage for electricity: "))

savingsAmount=(savingsPercent/100)*salary
rentAmount=(rentPercent/100)*salary
electAmount=(electPercent/100)*salary

print("The amount allocated to savings is: "+str(savingsAmount))
print("The amount allocated to rent is: "+str(rentAmount))
print("The amount allocated to electricity is: "+str(electAmount))

totalAmountCombined=savingsAmount+rentAmount+electAmount

print("The total amount Nabiha spends on savings, rent, and electricity combined is: "+str(totalAmountCombined))






