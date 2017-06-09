
def ejercicio2():
    contrasena = raw_input("password: ")
    numero = len(contrasena)
    if numero > 8:
	if contrasena.isalpha():
	    return "La password debe contener numeros y caracteres no alfanumericos"
	else:
	    if contrasena.isdigit():
		return "La password debe contener letras y caracteres no alfanumericos"
	    else:
		if contrasena.isalnum():
		    return "La password debe contener al menos un caracter no alfanumerico"
		else:
		    if contrasena.islower():
			return "La password debe contener al menos una mayuscula"
		    else:
			if contrasena.isupper():
			    return "La password debe contener al menos una minuscula"
			else:
			    if contrasena.find(' ') > 0:
				return "La password no puede contener espacios"
			    else:
				return "Password valida"
    else:
	return "La password debe contener mas de 8 caracteres"


