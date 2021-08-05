class Test:
    def __init__(self, method, exapmples=[]) -> None:
        self.res = ("FAIL", "PASS")
        self.method = method
        self.examples = exapmples

    def __str__(self):
        return f'examples: {self.examples}'

    def compare(self, res1, res2) -> bool:
        return str(res1) == str(res2)

    def paramsToStr(self, parameters) -> str:
        result = ''
        for p in parameters:
            separator = ', ' if result else ''
            result = f'{result}{separator}{p}'
        return result

    def run(self, detail=True) -> bool:
        all_tests_result = True
        for parameters, reference in self.examples:
            result = self.method(*parameters)
            test_result = self.compare(reference, result)
            all_tests_result = min(all_tests_result, test_result)
            if detail:
                print(f"{self.res[test_result]}\t{self.method.__name__}({self.paramsToStr(parameters)}) = {result} (reference: {reference})")
        print(f'{self.method.__name__} test result: {self.res[all_tests_result]}')
        return all_tests_result

import easy.twoSum
import medium.AddTwoNumbers
import medium.lengthOfLongestSubstring

tests = [
    Test(easy.twoSum.twoSum, easy.twoSum.examples()),
    Test(medium.AddTwoNumbers.addTwoNumbers, medium.AddTwoNumbers.examples()),
    Test(medium.lengthOfLongestSubstring.lengthOfLongestSubstring, medium.lengthOfLongestSubstring.examples())
]

for t in tests:
    t.run(False)

