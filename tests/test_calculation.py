from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficentFunds
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (10, 5, 15),
    (123, 23, 146)
])
def test_add(num1:int, num2:int, expected:int):
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(12, 4) == 8

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(12, 4) == 3




def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 30, 20),
    (90, 35, 55),
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficentFunds):
        bank_account.withdraw(200)
    