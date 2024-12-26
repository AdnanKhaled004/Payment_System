# 1. Single Responsibility Principle (SRP)
class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of {amount}.")




# 2. Open/Closed Principle (OCP)
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}.")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}.")




# 3. Liskov Substitution Principle (LSP)
def make_payment(payment_method: PaymentProcessor, amount: float):
    payment_method.process_payment(amount)




# 4. Interface Segregation Principle (ISP)
class Payment:
    def process_payment(self, amount: float):
        pass

class CreditCard(Payment):
    def process_payment(self, amount: float):
        print(f"Credit card payment: {amount}.")

class PayPal(Payment):
    def process_payment(self, amount: float):
        print(f"PayPal payment: {amount}.")



# 5. Dependency Inversion Principle (DIP)
class Order:
    def __init__(self, payment_method: Payment):
        self.payment_method = payment_method

    def place_order(self, amount: float):
        self.payment_method.process_payment(amount)



if __name__ == "__main__":
    credit_card = CreditCard()
    paypal = PayPal()

    order1 = Order(credit_card)
    order2 = Order(paypal)

    order1.place_order(100.0)
    order2.place_order(200.0)
