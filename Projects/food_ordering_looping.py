print("welcome to kfc momo")
print("enter your choice for momos \n 1.paneer momo \n 2.chicken momo \n 3. mushroom momo.\n ")
price1=60
price2=70
price3=50
total_bill1=total_bill2=total_bill3=0
n=int(input("enter the number of customers you want to order for:"))
print("there are three options and if you want to skip any order enter 0 in  thet place.")
for i in range(n):
        choice1=choice2=choice3=0
        a=input("for order type yes otherwise no:- ")
        if a=="yes":
            choice1,choice2,choice3=input("enter your choice:").split()
            if choice1=='1' or choice2=='2' or choice3=='3':
                if choice1=='1':
                    print("price for paneer momo is: 60 rupees per plate")
                    plate1=int(input("how many plates for this:-"))
                    total_bill1+=plate1*price1   
                if choice2=='2':
                    print("price for chicken momo is: 70 rupees per plate")
                    plate2=int(input("how many plates for this:-"))
                    total_bill2+=plate2*price2
                if choice3=='3':
                    print("price for mushroom momo is: 50 rupees per plate")
                    plate3=int(input("how many plates for this:-"))
                    total_bill3+=plate3*price3
                    
                print("After order ",i+1,"the orders and the total bill is shown  below:")
                if choice1=='1' and choice2=='2' and choice3=='0':
                    print("your order is paneer momo of price ",price1,"and plates of ",plate1,"\nyour order is chicken momo of price ",price2,"and plates of ",plate2)
                    print("your total bill is=",total_bill1+total_bill2+total_bill3)
                elif choice3=='3' and choice2=='2' and choice1=='0':
                    print("your order is chicken momo of price ",price2,"and plates of ",plate2,"\nyour order is mushroom momo of price ",price3,"and plates of ",plate3)
                    print("your total bill is=",total_bill3+total_bill2+total_bill1)
                elif choice1=='1' and choice3=='3' and choice2=='0':
                    print("your order is paneer momo of price ",price1,"and plates of ",plate1,"\nyour order is mushroom momo of price ",price3,"and plates of ",plate3)
                    print("your total bill is=",total_bill1+total_bill3+total_bill2)
                elif choice1=='1' and choice3=='3' and choice2=='2':
                        print("your order is paneer momo of price ",price1,"and plates of ",plate1,
                            "\nyour order is mushroom momo of price ",price3,"and plates of ",plate3,
                             "\nyour order is chicken momo of price ",price2,"and plates of ",plate2)
                        print("your total bill is=",total_bill1+total_bill3+total_bill2) 
                elif choice1=='1':
                        print("your order is paneer momo of price ",price1,"and plates of ",plate1)
                        print("your total bill is=",total_bill1)
                elif choice2=='2':
                        print("your order is chicken momo of price ",price2,"and plates of ",plate2)
                        print("your total bill is=",total_bill2)
                elif choice3=='3':
                        print("your order is mushroom momo of price ",price3,"and plates of ",plate3)
                        print("your total bill is=",total_bill3)
                else:
                    print("not in above opyion.please check again.")
        else:
            break

print("Thank you for visting kfc,we wait for you always")