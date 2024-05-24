from datetime import date

today = date.today()

D = today.day
MM = today.month
YYY = today.year

print(f"The current date is {D}/{MM}/{YYY}")
filename = f"C_CALC_{YYY}_{D}_{MM}"
print(f"The file name will be\n{filename}")
