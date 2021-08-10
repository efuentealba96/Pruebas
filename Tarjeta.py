class Card:
    def __init__(self,id,expiration,name,bank,balance):
        self.id = id
        self.expiration = expiration
        self.name = name
        self.bank = bank
        self.balance = balance
        self.activation = False
        self.password = None
        return

    def Active_Card(self):
        while True:
            password = input("Enter your password: ")
            try:
                self.password = str(password)
                print("The card is activated")
                self.activation = True
                return self.activation

            except:
                print("Erro in the activation")

    def Buy(self):
        while True:
            amount = input("Ingresar el monto a pagar: ")
            try:
                if(self.activation!=False):
                    pay = int(amount)
                    if(pay < self.balance):
                        print("Payment efectuted")
                        self.balance = self.balance-pay
                        print("New balance: %d" % self.balance)
                    else:
                        print("Max amount exceeded")    
                else:
                    print("Your card is not active, now you can perform the activation")
                    self.Active_Card()
            except:
                print("Check your input")
    
    def show_balance(self):
        print("Your balance is: ",self.balance)


card1 = Card(1,"07/27","Eliacer Fuentealba","Banco estado",1000)
card1.Buy()