# Free shipping eligibility
# Amazon prime customers OR purchases over $25
# under 18, you need parent consent to purchase

def free_shipping(age, cost, prime, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("Free shipping applied!")

    else:
        print("Ineligible for free shipping")

p = False
cos = 18
a = 12
con = False

free_shipping (a, cos, p, con)

