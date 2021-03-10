class Solution:
    def intToRoman(self, num: int) -> str:
        roman_to_int = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            20: "XX",
            30: "XXX",
            40: "XL",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: "XC",
            100: "C",
            200: "CC",
            300: "CCC",
            400: "CD",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: "CM",
            1000: "M",
            2000: "MM",
            3000: "MMM",
        }

        result = ""
        indx = 1
        str_num = str(num)
        for value in str_num:
            if value == '0':
                indx += 1
                continue
            cur_val = value
            zeros = len(str_num) - indx
            for index in range(zeros):
                cur_val += "0"
            result += roman_to_int[int(cur_val)]
            indx += 1
        return result
