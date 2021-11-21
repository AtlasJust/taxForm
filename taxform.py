"""
Program: taxform.py
Author: George 10/27/2021
Program used to compute a person's income tax.
"""

# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs
grossIncome = float(input("Please enter the gross income: "))
numDependents = int(input("Please enter the number of dependents: "))      

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
         (DEPENDENT_DEDUCTION * numDependents)
incomeTax = round(taxableIncome * TAX_RATE, 2)

# Display the income tax
print("The income tax is $" + str(incomeTax))
