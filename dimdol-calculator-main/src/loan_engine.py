from dataclasses import dataclass
from typing import List


@dataclass
class PaymentRow:
    month: int
    annual_rate: float
    payment: float
    principal: float
    interest: float
    balance: float
    accumulated_principal: float
    accumulated_interest: float


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

        self.total_months = years * 12

        self.special_months = special_years * 12

        self.special_rate = special_rate / 100

        self.normal_rate = normal_rate / 100

    def _monthly_rate(self, annual_rate):

        return annual_rate / 12

    def _annuity_payment(self, balance, annual_rate, months):

        r = self._monthly_rate(annual_rate)

        if r == 0:
            return balance / months

        return balance * r / (1 - (1 + r) ** (-months))

    def summary(self, rows: List[PaymentRow]):

        total_payment = sum(r.payment for r in rows)

        total_interest = sum(r.interest for r in rows)

        total_principal = sum(r.principal for r in rows)

        return {

            "total_payment": total_payment,

            "total_interest": total_interest,

            "total_principal": total_principal,

            "last_balance": rows[-1].balance,

        }
