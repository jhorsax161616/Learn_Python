#Hola 3 -> HolaHolaHola

def make_repeater_of(n: int):
    def repeater(string: str) -> str:
        assert type(string) == str, "Solo se debe recibir cadenas"
        return string * n
    return repeater

def make_division_by(n: float):
    assert n != 0, "No se acepta factor de divisor 0!!!"
    def division(number: float) -> float:
        return number/n
    return division

def run() -> None:
    repeat3 = make_repeater_of(3)
    repeat4 = make_repeater_of(4)
    repeat8 = make_repeater_of(8)

    print(repeat3("Hola"))
    print(repeat4("Power"))
    print(repeat8("Sa"))

    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    division_by_18 = make_division_by(18)

    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))
   
if __name__ == '__main__':
    run()