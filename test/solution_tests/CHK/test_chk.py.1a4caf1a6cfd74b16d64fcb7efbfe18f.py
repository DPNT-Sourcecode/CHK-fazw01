from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_invalid_sku(self):
        assert checkout_solution.checkout(1) == -1
