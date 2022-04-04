#Setting a protected variable
class safeGuard:
    def __init__(self):
        self._shielded = ""

#Testing calling the variable by assigning a string to the object from the class
txt = safeGuard()
txt._shielded = "Slap me, I'm American"
print(txt._shielded)

#Setting a private variable
class buyersRemorse:
    def __init__(oops):
        oops.__boughtNFT = 0

    #Setting the parameters to change the value so that the original variable remains untouched
    def howMuch(oops, amount):
        oops.__boughtNFT = amount

    #Prints the value of the private variable
    def showAmount(oops):
        print(oops.__boughtNFT)

#Testing the value of the private variable
nft = buyersRemorse()
nft.showAmount()
nft.howMuch(50000)
nft.showAmount()

if __name__ == '__main__':
    pass
