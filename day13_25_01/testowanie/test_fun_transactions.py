from day13_25_01.testowanie import fun_transactions as ft


def test_filter_transactions_income():
    expected_list = [
        {'amount': 1000, 'currency': 'USD', 'id': 1, 'type': 'income'},
        {'amount': 500, 'currency': 'USD', 'id': 3, 'type': 'income'},
        {'amount': 700, 'currency': 'USD', 'id': 5, 'type': 'income'},
        {'amount': 100, 'currency': 'EUR', 'id': 7, 'type': 'income'}
    ]
    assert ft.filter_transactions(ft.transactions, "income") == expected_list


# napisać test dla map_transactions()









def test_process_transactions_expense_eur():
    assert ft.process_transactions(ft.transactions, "expense", "EUR") == 400