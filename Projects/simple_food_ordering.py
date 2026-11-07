print("welcome to kfc momo")
print("in kfc momos,we have:- \n 1.paneer momo \n 2.chicken momo \n 3. mushroom momo.\n ")
print("type 0 if do not want to select that item.\n") 
ans='y'
while(ans=='y'): 
        print("price for paneer momo is: 60 rupees per plate")
        price1=60
        plate1=int(input("how many plates for this:-"))
        total_bill1=plate1*price1   

        print("price for chicken momo is: 70 rupees per plate")
        price2=70
        plate2=int(input("how many plates for this:-"))
        total_bill2=plate2*price2

        print("price for mushroom momo is: 50 rupees per plate")
        price3=50
        plate3=int(input("how many plates for this:-"))
        total_bill3=plate3*price3
        print("\n")          
        if plate1==0 and plate2!=0 and plate3!=0:       
            print("ordered items are:\n1.chicken momo-",plate2,"plate","\n2.mushroom momo-",plate3)
            print("the total bill is:",total_bill2+total_bill3,"$")
        elif plate1!=0 and plate2==0 and plate3!=0:
            print("ordered items are:\n1.chicken momo-",plate2,"plate","\n2.mushroom momo-",plate3)
            print("the total bill is:",total_bill2+total_bill3,"$")
        elif plate1!=0 and plate2!=0 and plate3==0:
            print("ordered items are:\n1.chicken momo-",plate2,"plate","\n2.mushroom momo-",plate3)
            print("the total bill is:",total_bill2+total_bill3,"$")
        elif plate1!=0 and plate2!=0 and plate3!=0:
            print("ordered items are:\n1.chicken momo-",plate2,"plate","\n2.mushroom momo-",plate3,"plate","\n3.paneer momo-",plate1,"plate",)
            print("the total bill is: ",total_bill2+total_bill3+total_bill1,"$")
        else:
            print("please order as per the menu.")
        
        ans=input("do you want to order again:?")
        if(ans=='n'):
                break;
            
print("Thank you for visting kfc,we wait for you always")