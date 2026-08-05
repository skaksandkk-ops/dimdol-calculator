from dataclasses import dataclass
from typing import List


@dataclass
class PaymentRow:
    month: int
    payment: float
    principal: float
    interest: float
    balance: float
    rate: float


class LoanEngine:

    def __init__(
        self,
        loan_amount: int,
        years: int,
        special_rate: float,
        special_years: int,
        normal_rate: float,
    ):

        self.loan_amount = loan_amount
        self.years = years

        self.special_rate = special_rate / 100
        self.normal_rate = normal_rate / 100

        self.special_years = special_years

        self.total_months = years * 12
        self.special_months = special_years * 12

    def monthly_rate(self, annual_rate):

        return annual_rate / 12

    def annuity_payment(self, balance, annual_rate, months):

        r = self.monthly_rate(annual_rate)

        if r == 0:
            return balance / months

        return balance * r / (1 - (1 + r) ** (-months))

    def equal_principal_payment(self):

        raise NotImplementedError

    def equal_payment(self):

        raise NotImplementedError
