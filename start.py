import main
import pakiet # import całego pakietu, ale sterowany przez __all_
from pakiet import fun # import z konkretnego pliku
import pakiet.fun as pk # jako alies
main.print_hi("Radek")

# pakiet.powitanie()

fun.powitanie()
fun.info()

#import pakiet, fun as pk # jako alies
pk.powitanie()
pk.info()

# sterowanie widocznością elementów pakietu
#__all__ = ['info']
pakiet.info()
pakiet.pożegnanie()