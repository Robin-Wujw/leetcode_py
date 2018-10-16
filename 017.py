from  functools import reduce

class Solution(object):
    def letterCombinations(self,digits):
        """

        :type digits:  str
        :return:       List{str}
        """
        keyMap = {
            "0": " ",
            "1": "*",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        results = []
        for digit in digits:
            if len(results) == 0 :
                for letter in keyMap[digit]:
                    results.append(letter)
            else:
                tempResults = []
                for result in results:
                    for letter in keyMap[digit]:
                        tempResults.append(result + letter)
                results = tempResults
        return results