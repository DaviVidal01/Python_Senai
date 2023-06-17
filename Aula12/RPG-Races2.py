class Personagem:
    __nome = ""
    __raca = ""
    __for = 0
    __dest = 0
    __const = 0
    __sab = 0
    __inte = 0
    __caris = 0

# Características---------------
    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self,nome:str) -> None:
        self.__nome = str(nome)
    
    @property
    def raca(self) -> str:
        return self.__raca
    @raca.setter
    def raca(self,raca:str) -> None:
        self.__raca = str(raca)
    
# Status---------------
    @property
    def forca(self) -> int:
        return self.__forc
    @forca.setter
    def forca(self,forca:int) -> None:
        self.__forc = int(forca)
    
    @property
    def dest(self) -> int:
        return self.__dest
    @dest.setter
    def dest(self,dest:int) -> None:
        self.__dest = int(dest)
    
    @property
    def const(self) -> int:
        return self.__const
    @const.setter
    def const(self,const:int) -> None:
        self.__const = int(const)
    
    @property
    def sab(self) -> int:
        return self.__sab
    @sab.setter
    def sab(self,sab:int) -> None:
        self.__sab = int(sab)
    
    @property
    def inte(self) -> int:
        return self.__inte
    @inte.setter
    def inte(self,inte:int) -> None:
        self.__inte = int(inte)
    
    @property
    def caris(self) -> int:
        return self.__caris
    @caris.setter
    def caris(self,caris:int) -> None:
        self.__caris = int(caris)

#-------------------------------{ INIT }--------------------

    def __init__(self,nome,raca,forca,dest,const,sab,inte,caris):
        self.__nome = nome
        self.__raca = raca
        self.__for = forca
        self.__dest = dest
        self.__const = const
        self.__sab = sab
        self.__inte = inte
        self.__caris = caris
#---------------------------------


Davi = Personagem("Davi","Dwarf Mountain",12,20,10,15,5,10)
print(Davi.raca)