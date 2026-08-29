'''
'''

import re
pattern = r"\b^[1267890][\d]{3}-?[\d]{3}[012356789]-?[\d]{3}[012356789]-?[\d]{3}[012356789]\b"

card_data = input("ENTER THE CREDIT CARD NUMBER: ")

match_1 = re.match(pattern, card_data)
if match_1:
    print("ITS VALID CARD")
else:
    print("INVALID CARD!!!")
