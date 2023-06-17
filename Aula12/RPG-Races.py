class Personagem:
    __forc = 0
    __dest = 0
    __const = 0
    __sab = 0
    __inte = 0
    __caris = 0

    @property
    def forca(self) -> int:
        return self.__forc
    @forca.setter
    def forca(self,forca:int) -> None:
        self.__forc = int(forca)
    
    @property
    def const(self) -> int:
        return self.__const
    @const.setter
    def const(self,const:int) -> None:
        self.__const = int(const)

    def __init__(self,forc,dest,const,sab,inte,caris):
        self.__forc = forc
        self.__dest = dest
        self.__const = const
        self.__sab = sab
        self.__inte = inte
        self.__caris = caris


class Raca(Personagem):
    raca = " "

    def Race(self,raca):
        self.raca = raca
        if "Dwarf" in raca:
            self.const += 2
            if raca == "Hill Dwarf":
                self.__sab += 1
            elif raca == "Mountain Dwarf":
                self.forca = self.forca + 2
        elif "Elf" in raca == True:
            self.__dest += 2
            if raca == "High Elf":
                self.__inte += 1
            elif raca == "Wood Elf":
                self.__sab += 1
            elif raca == "Dark Elf":
                self.__caris += 1


Davi = Raca(12,4,5,6,4,1)
Davi.Race("Mountain Dwarf")
print(Davi.raca)
print(Davi.forca)