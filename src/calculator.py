from models import LoanInput


class LoanCalculator:

    def __init__(self, loan: LoanInput):

        self.loan = loan

        self.loan_amount = (
            loan.house_price * loan.ltv / 100
        )

    @property
    def total_months(self):

        return self.loan.years * 12

    @property
    def special_months(self):

        return self.loan.special_years * 12

    @staticmethod
    def monthly_rate(rate):

        return rate / 100 / 12