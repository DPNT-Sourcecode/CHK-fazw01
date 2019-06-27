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

    def test_free_b(self):
        assert checkout_solution.checkout("BEE") == 80

    def test_compare_offers(self):
        assert checkout_solution.checkout("BBEE") == 110
        assert checkout_solution.checkout("EE") == 80

    def test_a_bundle(self):
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380