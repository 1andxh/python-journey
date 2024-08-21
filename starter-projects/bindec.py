# convert number from binary to decimal
# conver to binary from decimal

class NumberConversion:
    def bin_to_dec(self,binary):
        self.binary = list(str(binary))
        self.dummy = list()
        self.power = 0
        for i in self.binary[::-1]:
            self.dummy.append(int(i)*pow(2,self.power))
            self.power += 1
        return sum(self.dummy)
    

    def dec_to_bin(self,decimal):
        self.dummy = list()
        while(decimal):
            if decimal % 2 == 0:
                self.dummy.append(0)
                decimal = int(decimal/2)
            else:
                self.dummy.append(1)
                decimal = int((decimal - 1)/2)

        return "".join(map(str,self.dummy[::-1]))
    

x = NumberConversion()
choice = ""
while choice != 'q':
    print("\n---Number Conversion System---")
    print("1. Decimal to Binary\n2. Binary to Decimal\n3.Press 'q' to quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        try:
            dec = int(input("enter a decimal number: "))
            print("-"*15)
            print(f"{dec} in binary is {x.dec_to_bin(dec)}")
        except ValueError:
            print("Enter a numbrer")

    

    elif choice == '2':
        try:
            binary = int(input("Enter a binary number: "))
            print("-"*15)
            print(f"{binary} in Deciaml is {x.bin_to_dec(binary)}")

        except:
            print("enter a valid choice: ")