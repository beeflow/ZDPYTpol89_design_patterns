from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid {amount} using a Credit Card")


class PayPalPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid {amount} using PayPal.")


class BlikPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid {amount} using BLIK.")


class Cash(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid {amount} using CASH.")



class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount: float):
        self.payment_method.pay(amount)


def main() -> None:
    # Przychodzę do kasy i pada pytanie, jak chcę zapłacić

    # Odpowiadam - karta kredytowa
    credit_card = CreditCardPayment()

    # kasjerka przyjmuje kartę
    processor = PaymentProcessor(credit_card)

    # i pobiera płatność
    processor.process_payment(100.0)

    blik = BlikPayment()
    processor = PaymentProcessor(blik)
    processor.process_payment(230.0)

    cash = Cash()
    processor = PaymentProcessor(cash)
    processor.process_payment(50.0)


if __name__ == '__main__':
    main()
