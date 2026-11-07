questions=[
    ["which language was used to create facebook?","python","js","php","none",4],
    ["which language is famous?","python","js","php","none",1],
    ["which language is very old?","python","js","php","none",3],
    ["which language  use pointers?","python","js","php","none",2],
    ["which language is dynamicaly types?","python","js","php","none",1]
]
levels=[1000,5000,10000,20000,230493]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"question for rs{levels[i]}")
    print(f"{question[0]}")
    print(f"a.{question[1]}     b.{question[2]} ")     
    print(f"c.{question[3]}     d.{question[4]} ") 
    reply=int(input("enter your ans(1-4) or 0 to quit:"))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"correct answer , you have won rs {levels[i]}")
        print("\n")
        if i==1:
            money=10000
        elif i==3:
            money=10000
        else:
            money=230493
    else:
        print("wrong answer")
        break
print("your take home money is:",money)

'''
question for rs1000
which language was used to create facebook?
a.python     b.js 
c.php     d.none 
enter your ans(1-4):4
correct answer , you have won rs 1000


question for rs5000
which language is famous?
a.python     b.js 
c.php     d.none 
enter your ans(1-4):1
correct answer , you have won rs 5000


question for rs10000
which language is very old?
a.python     b.js 
c.php     d.none 
enter your ans(1-4):3
correct answer , you have won rs 10000


question for rs20000
which language  use pointers?
a.python     b.js 
c.php     d.none 
enter your ans(1-4):2
correct answer , you have won rs 20000


question for rs230493
which language is dynamicaly types?
a.python     b.js 
c.php     d.none 
enter your ans(1-4):1
correct answer , you have won rs 230493


your take home money is: 230493
'''