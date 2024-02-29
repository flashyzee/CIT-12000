#Ask user for weight
weight = float(input("Enter the weight of the package: "))

#Finding the shipping fee
shipping_fee = weight

#Determining Shipping fees 
if weight <= 2:
    shipping_fee = weight * 1.10
elif weight > 2 or weight <= 6:
    shipping_fee = weight * 2.20
elif weight > 6 or weight <= 10:
    shipping_fee = weight * 3.70
else:
    shipping_fee = weight * 3.80

#Display the shipping fees
print(f"Your Shipping fee is ${shipping_fee}")