# without using strategy pattern
class GoogleCreditCardProcessor:
    def register_user(self, user):
        # Logic to register user with Google
        pass

    def process_payment(self, user, amount):
        # Logic to process credit card payment
        pass

class GooglePayPalProcessor:
    def register_user(self, user):
        # Logic to register user with Google
        pass

    def process_payment(self, user, amount):
        # Logic to process PayPal payment
        pass

class GoogleBitcoinProcessor:
    def register_user(self, user):
        # Logic to register user with Google
        pass

    def process_payment(self, user, amount):
        # Logic to process Bitcoin payment
        pass

# ... and so on for Microsoft and GitHub registration methods
############################################################
# Registration using Strategies
from abc import ABC, abstractmethod

class RegistrationStrategy(ABC):
    @abstractmethod
    def register(self, user):
        pass

class GoogleRegistrationStrategy(RegistrationStrategy):
    def register(self, user):
        # Logic to register user with Google
        pass

class MicrosoftRegistrationStrategy(RegistrationStrategy):
    def register(self, user):
        # Logic to register user with Microsoft
        pass

class GitHubRegistrationStrategy(RegistrationStrategy):
    def register(self, user):
        # Logic to register user with GitHub
        pass

# PaymentProcessor now also handles registration

class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy, registration_strategy: RegistrationStrategy):
        self._payment_strategy = payment_strategy
        self._registration_strategy = registration_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def set_registration_strategy(self, registration_strategy: RegistrationStrategy):
        self._registration_strategy = registration_strategy

    def process_payment(self, user, amount):
        return self._payment_strategy.process_payment(user, amount)

    def register_user(self, user):
        return self._registration_strategy.register(user)

# Client code
processor = PaymentProcessor(CreditCardPaymentStrategy(), GoogleRegistrationStrategy())
processor.register_user(user)
processor.process_payment(user, amount)

processor.set_payment_strategy(PayPalPaymentStrategy())
processor.set_registration_strategy(MicrosoftRegistrationStrategy())
processor.register_user(user)
processor.process_payment(user, amount)


