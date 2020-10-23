
from ingreso import Ingreso
from egreso import Egreso
#Variable Ingreso
ingresoObj=Ingreso()
egresObj=Egreso()
class Finanza:#Crear cartera madre
    def __init__(self):
        self.conceptoIngreso=None
        self.conceptoEgreso=None
        self.montoIngreso=0
        self.montoEgreso=0

    def sendConceptoI(self, concepto):#Manda el concepto de ingreso
        self.conceptoIngreso=ingresoObj.Concepto(concepto)

    def sendMontoI(self, monto):#Manda el monto de ingreso
        self.montoIngreso=ingresoObj.Monto(monto)

    def sendIncome(self, concepto, monto):#Guarda el registro coompleto de ingreso
        ingresoObj.addIncome(concepto, monto )

    def showIncome(self):#Muestra todos los ingresos realizados
        ingresoObj.Showlog()

    def sendConceptoE(self, concepto):#Manda el concepto de egreso
        self.conceptoEgreso=egresObj.ConceptoE(concepto)

    def sendMontoE(self, monto):#Manda el monto egresado
        self.montoEgreso=egresObj.Monto(monto)

    def sendOutcome(self, concepto, monto):#Guarda el registro completo de egreso
        egresObj.addOutcome(concepto, monto)

    def showOutcomes(self):#Muestra todos los egresos realizados
        egresObj.Showlog()

    def showAllTransactions(self):#Muestra ingresos y egresos realizados
        result1=[]
        result2=[]
        while not(ingresoObj.Showlog() is None):
            result1 = print(ingresoObj.Showlog)
        while not(egresObj.Showlog() is None):
            result2= print(egresObj.Showlog)   
        return result1+result2

    def getTotal(self):#Muestra el saldo total
        Total=(ingresoObj.getMonto()-egresObj.getMonto())
        return Total

while True:
    print(  "Bienvenida a su cartera personal\n"+ #Si no inicia el proyecto no puede procesar nada
            "1. Iniciar proyecto de finanzas personales con cuenta a $0.00\n"+
            "2. Registrar un ingreso o un egreso\n"+
            "3. Generar reporte de todos los ingresos\n"+
            "4. Generar reporte de todos los egresos\n"+
            "5. Generar reporte de todas las transacciones (ingresos y egreso)\n"+
            "6. Ver saldo total\n"+
            "0. Salir\n"
        )
    Entrada=int(input("Seleccione el número de la opción\n"))
    if Entrada==0:#Cierra app
        print("Gracias por usar el servicio. Tenga buen día.")
        break
    elif Entrada==1:#Activar cartera
        FinanzasObj= Finanza()
    elif Entrada==2:#Registrar Ingreso o Egreso
        Entrada2=int(input("Seleccione la opción\n 1.Ingreso\n 2.Egreso\n"))
        if Entrada2==1:#Ingreso
            Concepto=input("Concepto del ingreso:\n")
            Monto=float(input("Monto:\n"))
            FinanzasObj.sendConceptoI(Concepto)
            FinanzasObj.sendMontoI(Monto)
            FinanzasObj.sendIncome(Concepto, Monto)
            print("Transacción realiza con éxito\n"+"-"*100)
        elif Entrada2==2:#Egreso
            Concepto=input("Concepto del egreso:\n")
            Monto=float(input("Monto:\n"))
            FinanzasObj.sendConceptoE(Concepto)
            FinanzasObj.sendMontoE(Monto)
            FinanzasObj.sendOutcome(Concepto, Monto)
            print("Transacción realiza con éxito\n"+"-"*100)
    elif Entrada==3:#Generar reporte de ingresos
        print("Generando reporte de Ingresos")
        FinanzasObj.showIncome()
        print(" \n")
        print("-"*100)
    elif Entrada==4:#Generar reporte de egresos
        print("Generando reporte de Egresos\n")
        FinanzasObj.showOutcomes()
        print(" \n")
        print("-"*100)
    elif Entrada==5:#Generar transacciones totales
        print("Generando registro de todas las transacciones\n")
        FinanzasObj.showAllTransactions()
        print(" \n")
        print("-"*100)
    elif Entrada==6:#Obtener saldo total
        print("Su saldo actual es de: $"+ str(FinanzasObj.getTotal()))




