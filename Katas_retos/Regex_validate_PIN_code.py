#No use isdigit

def validate_pin(pin : str) -> bool:
    #validate length
    if not len(pin) in [4, 6]:
        return False
    
    for i in pin:
        if not i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    return True

if __name__=='__main__':
    pass