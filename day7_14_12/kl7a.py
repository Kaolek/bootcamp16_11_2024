from pprint import pprint


class Printer:
    def print_message(self, message):
        print(f"Drukowanie wiadomości {message}")


class Scanner:
    def scan_dodument(self):
        print("Skanowanie dokumentu")
        return "Zawartość dokumentu"


printer = Printer()
printer.print_message("Radek")  # Drukowanie wiadomości Radek

scanner = Scanner()
print(scanner.scan_dodument())


# Skanowanie dokumentu
# Zawartość dokumentu

# klasa Mixin
class MultifunctionDevice(Printer, Scanner):

    def photocopy(self):
        content = self.scan_dodument()
        self.print_message(content)


device = MultifunctionDevice()
device.photocopy()

message = device.scan_dodument()
print(message)

device.print_message(message)

pprint(MultifunctionDevice.__mro__)
