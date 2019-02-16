#Answer to Stressful Subject - https://py.checkio.org/en/mission/stressful-subject/

import re

def is_stressful(subj):
    subj = re.sub(r"\b[!.-]\b","",subj)
    return subj.isupper() or any(re.findall("h+e+l+p+|u+r+g+e+n+t+|a+s+a+p+|!!!$",subj.lower()))
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')