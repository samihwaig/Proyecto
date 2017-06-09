

def ejercicio():
    usuario = raw_input("Nombre de usuario: ")
    numero1 = len(usuario)
    if numero1 >= 6:
        if numero1 <= 12:
            if usuario.isalnum():
                print "'Nombre de usuario valido'"
    		contrasena = raw_input("password: ")
   	 	numero = len(contrasena)
    		if numero >= 8:
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
        	    return "La password debe contener al menos 8 caracteres"    
            else:
                return "El nombre de usuario puede contener solo letras y numeros"
        else:
            return "El nombre de usuario no puede contener mas de 12 caracteres"
    else:
        return "El nombre de usuario debe contener al menos 6 caracteres"


