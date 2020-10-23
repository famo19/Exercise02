class Egreso:
    def __init__(self):#Inicialización de variables
        self.concepto=None
        self.montoE=0
        self.ElogDict={}
        self.counter=0
        self.ElogList=[]

    def ConceptoE(self, concepto):#Guarda el concepto de la compra  
        self.concepto=concepto

    def Monto(self, montoE):#Guarda el monto depositado
        self.montoE+=montoE

    def getMonto(self):#Obtiene el monto
        return self.montoE

    def addOutcome(self, concepto, montoE):#agrega al diccionario la información
        self.counter+=1
        idC=self.counter
        self.ElogDict={"id":idC,"Concepto":concepto, "Monto":montoE, "Tipo":"Egreso"}
        self.ElogList.append(self.ElogDict)
        
    def Showlog(self):#despliega la información procesada
        Reporte= print(self.ElogList)
        return Reporte