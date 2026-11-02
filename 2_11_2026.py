import random 

secret_num=random.randint (1,100) 
def fuc():    
    print("----start guess number game-------")
    attmept=0
    for attmept in range(5):
        count= 4-attmept

        num=int(input("enter your 1 to 100 num : "))
        attmept+=1
        if num<secret_num:
            print(f"too low! try again,attmept remaining : {count}")
        elif num>secret_num:
            print(f"too high! try again,attmept remaining : {count} ")    
        
        elif num==secret_num:
            print(f"thank you! your num is correct, secret_num:{secret_num} , attmept: {attmept+1} ") 
            break 
    else:
        
            print(f"game over! your attempt is end, attmept: {attmept} , secret_num:{secret_num}")
fuc()      
while True:
   
    choice=input("Do you want to play again? (yes/no):")

    if choice=="yes":
        fuc()
    else:
        print("thank you!  ")
        break



