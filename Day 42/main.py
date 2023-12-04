class Solution(object):
    @staticmethod
    def letterCombinations(digits):
        phone_numbers = {2 : {0 :"a", 1 :"b", 2 :"c"},
                     3 : {0 :"d", 1 :"e", 2 :"f"},
                     4 : {0 :"g", 1 :"h", 2 :"i"},
                     5 : {0 :"j", 1 :"k", 2 :"l"},
                     6 : {0 :"m", 1 :"n", 2 :"o"},
                     7 : {0 :"p", 1 :"q", 2 :"r", 3 : "s"},
                     8 : {0 :"t", 1 :"u", 2 :"v"},
                     9 : {0 :"w", 1 :"x", 2 :"y", 3 :"z"} }              
        all_combinations=[]
        if digits=="":
            True
        elif (int(digits)//10==0):
            for i in range(len(phone_numbers[int(digits)])):
                all_combinations.append(phone_numbers[int(digits)][i])
        else:
            num1 = int(digits)//10
            num2 = int(digits)%10
            for i in range(len(phone_numbers[num1])):
                letter_1=phone_numbers[num1][i]
                for j in range(len(phone_numbers[num2])):
                    letter_2=phone_numbers[num2][j]
                    combination = letter_1 + letter_2
                    all_combinations.append(combination)
        return all_combinations   