from enum import Enum
from abc import abstractmethod

class YakitTuru(Enum):
    BENZIN=1
    DIZEL=2
    LPG=3
    ELEKTRIK=4

class VitesTuru(Enum):
    OTOMATIK=1
    YARI_OTOMATIK=2
    MANUEL=3

class Vasita():
    __arac_listesi=[]
    def __init__(self,marka,model,yil=None,yakit=None,vites=None):
        if marka.isalnum():
            self.marka=marka.upper()
        else:
            raise Exception("Marka verisi hatalı!")

        if isinstance(yakit,YakitTuru):
            self.yakit=yakit
        else:
            raise Exception("Yakıt türü hatalı!")

        self.model=model
        self.yil=None
        self.vites=VitesTuru.MANUEL

    @staticmethod
    def arac_ekle(vasita):
        '''
        ENCAPSULATING
        '''
        Vasita.__arac_listesi.append(vasita)

    @staticmethod
    def listeyi_goster():
        '''
        STATIC METHODS
        '''
        print([str(arac) for arac in Vasita.__arac_listesi])

    @abstractmethod
    def arac_tipi(self):
        '''
        POLYMORPHISM
        '''
        return ""

    def __str__(self):
        '''
        LABELING
        '''
        return "Marka:{},Model:{}".format(self.marka, self.model)

class KaraTasiti(object):
    '''
    MULTI INHERITENCE
    '''
    tekerlek_sayisi=None

class Otomobil(Vasita, KaraTasiti):
    def __init__(self,marka,model=None,yakit=None):
        super().__init__(marka,model,yakit=yakit)

    def arac_tipi(self):
        return "Otomobil"

class Motosiklet(Vasita, KaraTasiti):
    def __init__(self,marka,model,yakit=None):
        super().__init__(marka,model,yakit=yakit)
        self.__zamanlama=None
        self.silindir_sayisi=None

    def arac_tipi(self):
        return "Motosiklet"

    def __str__(self):
        '''
        OVERRIDING
        '''
        return "{}({})".format(self.marka,self.yil)

class SuratTeknesi(Vasita):
    def __init__(self):
        self.govde=None
        self.boy=0

    def arac_tipi(self):
        return "Sürat Teknesi"
