
pattern="GAA"

def PatternToNumber(pattern):
    if pattern == '':
        return 0
    return 4 * PatternToNumber(pattern[0:-1])+ SymbolToNumber(pattern[-1:])                
    
def SymbolToNumber (symbol):
       if symbol == "A":
                    return 0
       if symbol == "C":
                    return 1
       if symbol == "G":
                    return 2
       if symbol == "T":
                    return 3

print(PatternToNumber(pattern))                
