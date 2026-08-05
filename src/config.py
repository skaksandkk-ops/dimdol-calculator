"""
기본 설정
"""

from dataclasses import dataclass


@dataclass
class LoanConfig:
    # 집값
    house_price: int = 400000000

    # LTV(%)
    ltv: float = 80

    # 대출기간(년)
    years: int = 30

    # 특례금리
    special_rate: float = 2.5

    # 특례기간(년)
    special_years: int = 5

    # 특례 종료 후 금리
    normal_rate: float = 3.5

    # 상환방식
    repayment_type: str = "원리금"

    @property
    def loan_amount(self):
        return int(self.house_price * self.ltv / 100)
