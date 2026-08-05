from dataclasses import dataclass


@dataclass
class LoanInput:
    house_price: int
    ltv: float
    years: int

    special_rate: float
    special_years: int

    normal_rate: float

    repayment: str


@dataclass
class Payment:

    month: int

    payment: float

    principal: float

    interest: float

    balance: float

    annual_rate: float