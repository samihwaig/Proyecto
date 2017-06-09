

def ejercicio(intento=1):
    usuario = raw_input("Nombre de usuario: ")
    numero = len(usuario)
    if numero > 6:
        if numero < 12:
            if usuario.isalnum():
                return "Nombre de usuario valido"
            else:
		return "El nombre de usuario puede contener solo letras y numeros"
	else:
            return "El nombre de usuario no puede contener mas de 12 caracteres"
    else:
	return "El nombre de usuario debe contener al menos 6 caracteres"

