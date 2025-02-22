salary=int(input("input your salary for the month: "))
month=input(" input the name of the month you are storing the salary for: ")
savingsPercent=int(input("input the percentage for savings:"))
rentPercent=int(input("input the percentage for rent: "))
electPercent=int(input("input the percentage for electricity: "))

savingsAmount=(savingsPercent/100)*salary
rentAmount=(rentPercent/100)*salary
electAmount=(electPercent/100)*salary

print("The amount allocated to savings is: ",savingsAmount)
print("The amount allocated to rent is: "+str(rentAmount))
print("The amount allocated to electricity is: "+str(electAmount))

totalAmountCombined=savingsAmount+rentAmount+electAmount

print("The total amount Nabiha spends on savings, rent, and electricity combined is: "+str(totalAmountCombined))

remainderOfSalary=salary-totalAmountCombined
print("The remainder amount of Nabiha's salary after the expenses is: "+str(remainderOfSalary))

yearlyCostForElectAndRent=(rentAmount+electAmount)*12
print("The yearly cost for rent and electricity is: "+str(yearlyCostForElectAndRent))

monthlySalarypoweredByTwo=salary**2
print("Nabiha's total salary for the month raised to the power of 2 is: "+str(monthlySalarypoweredByTwo))

additionalSavingAmount=int(input("enter an additional random amount: "))
if additionalSavingAmount!=0 and savingsAmount!=0:
    remainderFromAdditionalSavings = additionalSavingAmount%savingsAmount
print("amount left is: "+str(remainderFromAdditionalSavings))    


