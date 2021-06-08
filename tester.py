class Tester:
    def __init__(self) -> None:
        self.res = ("FAIL", "PASS")
        self.examples = []

    def compare(self, lst1, lst2) -> bool:
        return str(lst1) == str(lst2)

    def test(self, method) -> bool:
        all_tests_result = True
        for parameters, reference in self.examples:
            result = Solution().addTwoNumbers(l1, l2)
            test_result = self.compare(reference, result)
            all_tests_result = min(all_tests_result, test_result)
            print(f"{self.res[test_result]}\taddTwoNumbers({l1}, {l2}) = {result} (reference: {reference})")
        return all_tests_result
