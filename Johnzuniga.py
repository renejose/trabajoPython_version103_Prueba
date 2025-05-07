print("------------------------ hacer algoritmo----------------")
totpacientes = 0
cBajoPeso = 0
cPesoNormal = 0
cSobrePeso = 0
cObesidad = 0

def calcularimc(x,y,cBajoPeso,cPesoNormal,cSobrePeso,cObesidad):
    imc = x / (y ** 2)
    if imc < 18.5:
        cBajoPeso = cBajoPeso + 1
    elif 18.5 <= imc < 24.9:
        cPesoNormal = cPesoNormal + 1
    elif 25 <= imc < 29.9:
        cSobrePeso = cSobrePeso + 1
    else:
        cObesidad = cObesidad + 1

print("hola a todos")        


while totpacientes<5:
    totpacientes = totpacientes + 1 
    print("---------------")
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    calcularimc(peso,altura,cBajoPeso,cPesoNormal,cSobrePeso,cObesidad)
    
print("Pacientes Bajo de Peso : ",cBajoPeso)
print("Pacientes Peso Normal : ",cPesoNormal)
print("Pacientes Con SobrePeso : ",cSobrePeso)
print("Pacientes Con Obesidad : ",cObesidad)
print("------------------------ Fin del programa----------------")