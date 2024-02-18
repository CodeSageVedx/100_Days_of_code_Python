#String to Integer
class Solution:
    def myAtoi(self, s: str) -> int:
        intFound, signFound = False, False
        answer = ""
        for i in s:
            # If number is not found
            if intFound is False:
                if i == "+" or i == "-":
                    # If already we encountered sign, loop will end.
                    if signFound is True:
                        answer = "0"
                        break
                    # Otherwise i becomes our sign and we ignore this sign
                    else:
                        answer += i
                        signFound = True
                        continue
                else:
                    # If we find number
                    if 48 <= ord(i) <= 57:
                        intFound = True
                        answer += i
                        continue
                    else:
                        # If whitespace is leading, we ignore
                        if i == " " and signFound is False:
                            continue
                        else:
                            answer = "0"
                            break
            else:
                if not 48 <= ord(i) <= 57:
                    break
                else:
                    answer += i
        if len(answer) == 0:
            answer = "0"
        if len(answer) == 1 and answer == "-" or answer == "+":
            answer = "0"
        answer = min(int(answer), 2 ** 31 - 1)
        answer = max(int(answer), -2 ** 31)
        return int(answer)
####        