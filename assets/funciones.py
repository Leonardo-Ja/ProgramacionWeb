def contar_empleado(arrayEmployees):
    for empleadoBuscado in arrayEmployees:
        contado = 0
        for employee in arrayEmployees: 
            if empleadoBuscado == employee:
                contado = contado + 1
        print('El nombre ' + empleadoBuscado + ' se encontro ' + str(contado) + ' veces')
    