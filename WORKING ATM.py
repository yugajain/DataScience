Class Atm
    def __init__("self","cardnumber,pin")
        self.cardnumber = cardnumber
        self.pin = pin


     def check_balance(self):
          print(Your balance is 90000)  

     def withdrawl(self,amount):
          new_amount =  90000 - amount
          print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_ammount))   

def main():
    Card_number = input("enter your card number:_ ")
    pin_number = input("enter your pin number:- ")

    new_user = Atm(Card_number,pin_number)

    print("Hello how can we help you today ")
    print("1.Balance Enquiry          2.withdrawl")
    activity = int(input("enter activity number:- ") )

    if (activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input("enter the amount:_ "))
        new_user.withdrawl(amount)  
    else:
        print("enter a valid number ")     

if __name__ == "__main__":
    main()          