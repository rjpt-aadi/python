print("*********Aditya Kumar*********")

# Get user input for the number to check
num = int(input("What is your favorite number? "))
prime = True

# Check the number is prime or not
for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print(f"{num} is Prime")
else:
    print(f"{num} is not Prime")
