class Ingreso:
    def __init__(self):#Inicialización de variables 
        self.concepto=None
        self.montoI=0
        self.IlogDict={}
        self.idCounter=0
        self.IlogList=[]

    def Concepto(self,concepto):#Guarda el concepto de la compra
        self.concepto=concepto      

    def Monto(self, montoI):#Guarda el monto depositado
        self.montoI+=montoI

    def getMonto(self):#Obtiene el monto
        return self.montoI
        
    def addIncome(self, concepto, montoI):#agrega al diccionario la información   
        self.idCounter+=1#contador
        idC=self.idCounter#id para contar las transacciones     
        self.IlogDict={"id":idC,"Concepto":concepto,"Monto":montoI, "Tipo":"Ingreso"}#diccionario
        self.IlogList.append(self.IlogDict)#se agrega el registro a la lista
        

    def Showlog(self):#despliega la información procesada
        Reporte=print(self.IlogList)
        return Reporte


