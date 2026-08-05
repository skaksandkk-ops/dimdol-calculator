from models import LoanInput

DEFAULT_INPUT = LoanInput(
    house_price=400000000,
    ltv=80,
    years=30,
    special_rate=2.5,
    special_years=5,
    normal_rate=3.5,
    repayment="원리금",
)