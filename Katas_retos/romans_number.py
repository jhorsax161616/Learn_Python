"""TODO: create a RomanNumerals helper object"""

class RomanNumerals:
    
    def __init__(self):
        self.romans = ["I", "V", "X", "L", "C", "D", "M"]
        self.values = [1, 5, 10, 50, 100, 500, 1000]
        
        
    def to_roman(self, date):
        number = []
        #esto funcionara para las decenas en adelante, ceros a la derecha
        for i in range(7):
            if self.values[i] == date:
                number.append(self.romans[i])
            elif self.values[i] > date:
                if self.values[i] * 2 == date:
                    number.append(self.romans[i - 1] * 2)
                elif self.values[i] * 3 == date:
                    number.append(self.romans[i - 1] * 3)
                else:
                    number.append(self.romans[i - 1] + self.romans[i])
        
        return number
                
    def from_roman(self, date):
        pass

object1 = RomanNumerals()
print(object1.to_roman(100)) #, 'M', '1000 should == "M")
#object2 = RomanNumerals.to_roman(1990) #, 'MCMXC', '1990 should == "MCMXC")

#object3 = RomanNumerals.from_roman('XXI') #, 21, 'XXI should == 21')
#object4 = RomanNumerals.from_roman('MMVIII') #, 2008, 'MMVIII should == 2008')
