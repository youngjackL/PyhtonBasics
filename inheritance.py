class Mpesa :
    def __init__(self, account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number =phone_number
    def send_money(self,amount ,recipient):
        if self.account_balance >= amount :
            self.account_balance -= amount
            print(f"{amount} Kes has been sent to {recipient} successfully")
        else:
            print("insufficient Amount to send Money")
class PersonalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,idno):
        super().__init__(account_balance,phone_number)
        self.idno = idno
    def buyairtime (self,amount):
        self.account_balance -= amount
        print(f"{amount} Kes airtime bought successfully")
class BusinessMpesa(Mpesa):
    def __init__(self,account_balance,phone_number, business_id):
        super().__init__(account_balance,phone_number)
        self.business_id =business_id
    def recive_payment(self,amount):
        self.account_balance += amount
        print(f"{amount} Kes recived from a customer")
personal=PersonalMpesa(2000,"0712345678","3277583")
personal.send_money(3000,712345678)
personal.buyairtime(150)

personal=BusinessMpesa(2000,"0787654321","499023")
personal.send_money(5000,787654321)
personal.recive_payment(600)
