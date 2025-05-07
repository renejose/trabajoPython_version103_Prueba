nota = round(float(input("ingrese nota de estudiante")),2)
calificacion = 0
print("la nota es: ",nota)
	if 0 <=  nota <= 20 :
	    print("ingreso a evaluación")
	    if 18 <= nota <= 20:
	        calificacion = "Excelente"
	    elif 15 <= nota <= 17:
	        calificacion = "Buena"
	    elif 11 <= nota <= 14:
	        calificacion = "Regular"
	    else:
	        calificacion = "Necesita recuperación"
	else:
	    print("la nota está fuera de rango")