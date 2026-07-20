


def validar_codigo(codigo, recorridos):
    if not codigo or str(codigo).strip() == "":
        return False
    if codigo.strip().upper() in [k.upper() for k in recorridos.keys()]:
        return False
    return True

def validar_texto(texto):
    if not texto or str(texto).strip() =="":
        return False
    return True

def validar_distancia(distancia):
    try:
        valor = int(distancia)
        return valor > 0
    except ValueError:
        return False
    
def validar_tipo_bus(tipo):
    return str(tipo).strip().lower() in ['normal', 'semi-cama', 'cama']

def validar_servicio(servicio):
    return str(servicio).strip().lower() in ['dia', 'noche']

def validar_tiene_wifi(wifi_input):
    return str(wifi_input).strip().lower() in ['s', 'n']

def validar_precio(precio):
    try:
        valor = int(precio)
        return valor > 0
    except ValueError:
        return False
    
def validar_asientos(asientos):
    try:
        valor = int(asientos)
        return valor >= 0
    except ValueError:
        return False



def leer_opcion():
    while True:
        try:
            opcion_str = input("Seleccione una opcion: ")
            opcion = int(opcion_str)
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida (1-6).")
        except ValueError:
            print("Debe selecionar una opción valida.")

def asientos_origen(origen_buscar, recorridos, venta):
    total_asientos = 0 
    encontrado = False

    origen_buscar_clean = origen_buscar.strip().lower()

    for codigo, datos in recorridos.items():
        if datos[0].lower() == origen_buscar_clean:
            encontrado = True
            if codigo in venta:
                total_asientos += venta[codigo][1]

    if encontrado:
        print(f"\nTotal de aientos para salor desde '{origen_buscar}': { total_asientos}")
    else:
        print(f"\nNo se encontraron recorridos con el origen: {origen_buscar}")

def busqueda_precio(p_min, p_max, recorridos, venta):
    resultados = []

    for codigo, datos_venta in venta.items():
        precio = datos_venta[0]
        asientos = datos_venta[1]

        if p_min <= precio <= p_max and asientos > 0:
            origen = recorridos[codigo][0]
            destino = recorridos[codigo][1]
            resultados.append(f"{origen}-{destino}-{codigo}")

    if resultados:
        resultados.sort()
        print("\nRecorridos encontrados (origen-Destino-Codigo): ")
        for res in resultados:
            print(f"- {res}")
    else:
        print("\nNo hay recorridos en ese rango de precios.")

def buscar_codigo(codigo, venta):
    return codigo.strip().upper() in [k.upper() for k in venta.keys()]

def actualizar_precio(codigo, nuevo_precio, venta):
    codigo_upper = codigo.strip().upper()
    for k in venta.keys():
        if k.upper() == codigo_upper:
            venta[k][0] = nuevo_precio
            return True
    return False

def agregar_recorridos(codigo, origen, destino, distancia, tipo_bus, servicio, tiene_wifi, precio, asientos, recorridos, venta):
    if codigo in recorridos:
        return False

    wifi_bool = True if tiene_wifi.lower() == 's' else False


recorridos[codigo] = [
 origen.strip(),
 destino.strip(),
 int(distancia),
 tipo_bus.strip().lower(),
 servicio.strip().lower(),
 wifi_bool
]

venta[codigo] = [int(precio), int(asientos)]
return True

def eliminar_recorrido(codigo, recorridos, venta):
    codigo.upper = codigo.strip().upper()
    clave_encontrada = None

    for k in recorridos.keys():
        if k.upper() == codigo.upper:
            clave_encontrada = K 
            break

if clave_encontrada:
    del recorridos[clave_encontrada]
    if clave_encontrada in venta:
        del venta[clave_encontrada]
    return True
return False



def main():
    recorridos = {
'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'día', True],
'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'día', False],
'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'día', True],
'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
'R006': ['Santiago', 'Rancagua', 90, 'normal', 'día', True],
}
    
venta = {
'R001': [7990, 20],
'R002': [25990, 0],
'R003': [1990, 35],
'R004': [12990, 8],
'R005': [18990, 3],
'R006': [4990, 12],
}    

ejecuntando = True

while ejecutando:
  print("\n========== MENÚ PRINCIPAL ==========")
  print("1. Asientos por ciudad de origen")
  print ("2. Búsqueda de recorridos por rango de precio")
  print ("3. Actualizar precio de recorrido")
  print ("4. Agregar recorrido")
  print ("5. Eliminar recorrido")
  print ("6. Salir")
  print ("=====================================")

opcion = leer_opcion()

if opcion == 1:
    print("\n--- Opcion 1: Asientos por ciudad de origen ---")
    origen = input("Ingrese la ciudad de origen: ")
    asientos_origen(origen, recorridos, venta)

elif opcion == 2:
    print("\n--- Opcion 2: Busqueda por rango de precio ---")
    while True:
        try:
            p_min = int(input("Ingrese precio minimo: "))
            p_max = int(input("ingrese precio maximo: "))
            if p_min >= 0 and p_max > p_min:
                break
            else:
                print("El precio minimo debe ser >= 0 y al maximo debe ser mayor o igual al minimo")


    busqueda_precio(p_min, p_max, recorridos, venta)

elif opcion == 3:
    print("\n---  Opcion 3: Actualizar precio del recorrido ---")
    while True:
        codigo = input("Ingrese el codigo del recorrido a modificar: ")
        if buscar_codigo(codigo, venta):
            while True:
                np_str = input("Ingrese el nuevo precio: ")
                try:
                    nuevo_precio = int(np_str)
                    if nuevo_precio > 0:
                        break
                    print("El precio debe ser un entero mayor a cero")
                except ValueError:
                    print("Precio invalido.")

    if actualizar_precio(codigo, nuevo_precio, venta):
        print("Precio actualizado")
    break
else:
    print("El codigo no existe")
    resp = input("¿Desea actualizar otro precio (S/N)?: ").strip().lower
    if resp != 's':
        break

    elif opcion == 4:
         print("\n--- Opcion 4: Agregar recorrido ---")
         codigo = input("Codigo de recorrido: ")
         if not validar_codigo(codigo, recorridos):
            print("Error: El origen no puede estar vacio. No se registra el recorrido.")
            continue


          
                            

    


    
          