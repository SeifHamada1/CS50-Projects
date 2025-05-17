from tracker import get_valid_amount, get_valid_date

def test_get_valid_amount():
    assert get_valid_amount("10") == 10
    assert get_valid_amount("0") == None
    assert get_valid_amount("-5") == None
    assert get_valid_amount("abc") == None

def test_get_valid_date():
    assert get_valid_date("2025-05-17") == "2025-05-17"
    assert get_valid_date("") == __import__("datetime").datetime.today().strftime("%Y-%m-%d")
    assert get_valid_date("invalid-date") == None

def test_sort_transactions_by_date():
    transactions = [
        {"type": "expense", "category": "food", "amount": "20", "date": "2025-05-15"},
        {"type": "income", "category": "income", "amount": "100", "date": "2025-05-10"},
        {"type": "expense", "category": "rent", "amount": "500", "date": "2025-05-20"},
    ]

    # Sort transactions by date ascending
    transactions.sort(key=lambda x: x['date'])

    assert transactions[0]['date'] == "2025-05-10"
    assert transactions[1]['date'] == "2025-05-15"
    assert transactions[2]['date'] == "2025-05-20"

test_sort_transactions_by_date()


