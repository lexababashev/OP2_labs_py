import random
import time
from ASeries import ASeries
from GSeries import GSeries


n = int(input("Enter 'n': "))
m = int(input("Enter 'm': "))
print()
random.seed(time.time())
gSeries = GSeries()
aSeries = ASeries()

max = 0

max_sum = 0

for i in range(n):
    first_member = random.randint(1, 11)
    step = random.randint(1, 11)

    if(i % 2 == 0):
        gSeries.set_first(first_member)
        gSeries.set_parameter(step)

        print(f"{i + 1}) first number is  {first_member}  step is {step}")
        print(f" n number is {gSeries.calculate_n(n)} and sum is {gSeries.calculate_sum(m)}\n")

        if(max < gSeries.calculate_n(n)):
            max = gSeries.calculate_n(n)

            max_sum = gSeries.calculate_sum(m)

    else:
        print(f"{i + 1}) first number is  {first_member} step is {step}")
        print(f"n number is {aSeries.calculate_n(n)} and sum is {aSeries.calculate_sum(m)}\n")

        aSeries.set_first(first_member)
        aSeries.set_parameter(step)
        if(max < aSeries.calculate_n(n)):
            max = aSeries.calculate_n(n)

            max_sum = aSeries.calculate_sum(m)

print(f"\nMax n number is: {max} with sum of first m numbers is {max_sum}\n\n")

