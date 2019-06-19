from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_invalid_sku(self):
        assert checkout_solution.checkout(1) == -1

    def test_no_bundle(self):
        assert checkout_solution.checkout("ABC") == 100

    def test_bundle(self):
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("AAABBC") == 195
        
    def test_empty_string(self):
        assert checkout_solution.checkout("") == 0