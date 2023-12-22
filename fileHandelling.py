num=int(input("Enter your Table Number: "))
multi=int(input("Enter numbers till you need a table: "))
for i in range (1,multi+1):
    table=num*i
    print(f"{num} * {i} = {table}")
    with open ("table.txt","a") as f:
        f.write(str(f"{num} * {i} = {table}"))
        f.write('\n')
f.close()