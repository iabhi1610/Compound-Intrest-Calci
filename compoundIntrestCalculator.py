print("For how many years you will be saving? ")
years = int(input('Enter years: '))

print("Please! feed for principle amount")
principle = float(input('Enter principal: '))

print("How much amount you wanna spend monthly?")
monthly_amount = float(input('Enter the amount: '))

print("At what intrest you want to do this investment?")
intrest = float(input('Enter the intrest rate in decimal form(e.g. 10% = 0.1): '))

final_amount = 0
monthly_amount = monthly_amount * 12 #conversion into months

for i in range(0, years):
    if final_amount == 0:
        final_amount = principle
    final_amount = (final_amount + monthly_amount) * (1 + intrest)

print("Your  investment after {} years will be: ".format(years) + str(final_amount))
    
