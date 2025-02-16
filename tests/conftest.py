import pytest

@pytest.fixture
def account_number_fixture():
    return '12345678905555555555'


@pytest.fixture
def cart_number_fixture():
    return '1234567890666666'


@pytest.fixture
def mask_account_cart_fixture():
    return 'Visa Classic 6831982476737658'

@pytest.fixture
def get_date_fixture():
    return '2024-03-11T02:26:18.671407'
