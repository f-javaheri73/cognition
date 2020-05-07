1"""days = [31,28,31,30,31,30,31,31,30,31,30,31]



def julian_date(d,m,y):
    """ this function take day, month and year, and return days passed from the beginning"""
   
    if y%400==0 or (y%4 ==0 and y%100 != 0):
        days[1]=29
        days_passed = 0
        for items in days[:m-1]:
            


            days_passed += items 
            

            

    days_passed +=d
    print(days_passed)"""
            
            
            
2"""def  func():
    x = int(input('yek adad vared konid:'))
    for i in range(x,-1,-1):
     print(i)"""


3"""def func():
    num1 = int(input('adad vared konid:'))
    num2 = int(input('adad vared konid:'))
    if num1% num2 == 0:
        print('bakhsh pazir ast')
    else:
        print('bakhsh pazir nist')"""
    
4"""def func():
    num = int(input('adad vared konid:'))
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                print(num,"adad aval nist")
                print(i,"zarbdar", num//i,"mishavad",num)
                break
            else:
                print(num,"adade aval hast")

        else:
            print(num,"adae aval nist")"""
    
