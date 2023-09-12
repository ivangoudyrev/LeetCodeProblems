class Solution:
    def romanToInt(self, s: str) -> int:

        arabic_num = 0

        special_nums_dict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        nums_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        s1 = s

        for num in special_nums_dict:     
            result=s1.find(num)    
            if result>=0:
                s1 = s1.replace(num,"",1)
                arabic_num += special_nums_dict[num]

        while len(s1)>0:
            for num in nums_dict:
                result=s1.find(num)
                if result>=0:
                    s1 = s1.replace(num,"", 1)
                    arabic_num += nums_dict[num]
            
        return arabic_num