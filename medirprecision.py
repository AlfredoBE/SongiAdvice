# Listas de palabras clave por unidad y año de enseñanza básica
palabras_clave_5_1 = ['hello', 'bye', 'thanks', 'look', 'and', 'face', 'mother','father']
palabras_clave_5_2 = ['garden','house','wall','big','run','there','picture','shower']
palabras_clave_5_3 = ['sorry','please','good','lunch','cofee','eat','bad','drink']
palabras_clave_5_4 = ['sunny','boots','shirt','hot','night','birthday','christmas','coat']

#***************************************************************************************************************************************
palabras_clave_6_1 = ['can','cough','welcome','well','fell','stomachache','want','what']
palabras_clave_6_2 = ['time','next','straight','right','driver','builder','shop','restaurant']
palabras_clave_6_3 = ['when','slept','ran','forest','wolf','quiet','yesterday','many']
palabras_clave_6_4 = ['nice','hotel','was','travel','city','vacations','beach','bus']

#***************************************************************************************************************************************
palabras_clave_7_1 = ['think','find','meet','nice','happy','peopke','friend','angry']
palabras_clave_7_2 = ['coffee','juice','milk','water','tea','rice','banana','apple']
palabras_clave_7_3 = ['football','tennis','dancing','playing','running','climbing','loser','winning']
palabras_clave_7_4 = ['first','finally','destroy','protect','trash','garbage','sea','forest']

#***************************************************************************************************************************************
palabras_clave_8_1 = ['many','much','like','love','hate','computer','internet','blog']
palabras_clave_8_2 = ['good','bad','tall','amazing','beautiful','popular','interesting','expensive']
palabras_clave_8_3 = ['bus','train','plane','bookshop','church','lake','market','underground']
palabras_clave_8_4 = ['tomorrow','month','disagree','dislike','disappear','computer','think','believe']

#***************************************************************************************************************************************
numeros = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
               'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one',
               'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight',
               'twenty-nine', 'thirty', 'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four', 'thirty-five',
               'thirty-six', 'thirty-seven', 'thirty-eight', 'thirty-nine', 'forty', 'forty-one', 'forty-two',
               'forty-three', 'forty-four', 'forty-five', 'forty-six', 'forty-seven', 'forty-eight', 'forty-nine', 'fifty']


def contar_palabras(cancion, palabras_clave, numeros):
    """
    Función para contar palabras clave en una letra de canción.
    
    Args:
    - cancion (str): La letra de la canción en formato de cadena.
    - palabras_clave (list): Lista de palabras clave a buscar en la letra.
    - numeros (list): Lista de números a considerar como una unidad.
    
    Returns:
    - tuple: Porcentaje de puntaje obtenido y número total de palabras únicas que suman puntos.
    """
    palabras_encontradas = []
    puntaje_total = 0
    palabras_unicas = set()  # Utilizamos un conjunto para contar palabras únicas
    
    # Convertimos la letra de la canción a minúsculas para hacer la búsqueda case insensitive
    cancion_minusculas = cancion.lower()
    
    # Buscar y contar palabras clave
    for palabra in palabras_clave:
        if cancion_minusculas.count(palabra.lower()) > 0:
            puntaje_total += 1
            palabras_encontradas.append(palabra)
            palabras_unicas.add(palabra.lower())  # Agregamos la palabra al conjunto
    
    # Buscar y contar números
    for numero in numeros:
        if cancion_minusculas.count(numero.lower()) > 0:
            puntaje_total += 1  # Contar solo como un punto, no múltiples veces
            palabras_encontradas.append(numero)
            palabras_unicas.add(numero.lower())  # Agregamos el número al conjunto
            break  # Solo necesita encontrar uno de los números para contar el conjunto completo
    
    # Calculamos el número de palabras únicas que suman puntos
    total_palabras_unicas = len(palabras_unicas)
    
    # Calculamos el porcentaje de puntaje obtenido
    puntaje_maximo = len(palabras_clave) + 1  # Sumamos 1 por el número
    porcentaje = (puntaje_total / puntaje_maximo) * 100
    
    # Imprimir las palabras clave encontradas
    print("Palabras clave encontradas:")
    for palabra in palabras_encontradas:
        print(palabra)
    
    return porcentaje, total_palabras_unicas

def obtener_palabras_clave(año, unidad):
    """
    Función para obtener las palabras clave según el año y unidad seleccionadas.
    
    Args:
    - año (str): Categoría seleccionada ('5', '6', '7', '8').
    - unidad (str): Unidad seleccionada ('1', '2', '3', '4').
    
    Returns:
    - tuple: Lista de palabras clave y lista de números correspondiente al año y unidad seleccionadas.
    """
    if año == '5':
        if unidad == '1':
            return (palabras_clave_5_1, numeros)
        elif unidad == '2':
            return (palabras_clave_5_2, [])
        elif unidad == '3':
            return (palabras_clave_5_3, numeros)
        elif unidad == '4':
            return (palabras_clave_5_4, numeros)
    
    elif año == '6':
        if unidad == '1':
            return (palabras_clave_6_1, numeros )
        elif unidad == '2':
            return (palabras_clave_6_2, numeros )
        elif unidad == '3':
            return (palabras_clave_6_3, numeros)
        elif unidad == '4':
            return (palabras_clave_6_4, numeros)
    
    elif año == '7':
        if unidad == '1':
            return (palabras_clave_7_1, [])
        elif unidad == '2':
            return (palabras_clave_7_2, [])
        elif unidad == '3':
            return (palabras_clave_7_3, [])
        elif unidad == '4':
            return (palabras_clave_7_4, [])
    
    elif año == '8':
        if unidad == '1':
            return (palabras_clave_8_1, [])
        elif unidad == '2':
            return (palabras_clave_8_2, [])
        elif unidad == '3':
            return (palabras_clave_8_3, [])
        elif unidad == '4':
            return (palabras_clave_8_4, [])
    
    return ([], [])

def main():
    # Solicitar la categoría al usuario
    print("Seleccione un año de enseñanza básica (5, 6, 7, 8):")
    año = input().strip()
    
    # Seleccionar las palabras clave según la categoría y la unidad elegida
    if año in ['5', '6', '7', '8']:
        print(f"Seleccione una unidad (1-4) para el año {año}:")
        unidad = input().strip()
        
        if unidad in ['1', '2', '3', '4']:
            palabras_clave, numeros = obtener_palabras_clave(año, unidad)
            
            if palabras_clave:
                # Solicitar el nombre del archivo al usuario
                print("Ingrese el nombre del archivo de texto:")
                nombre_archivo = input().strip()
                
                try:
                    # Abrir y leer el archivo
                    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                        # Leer todo el contenido del archivo
                        letra_cancion = archivo.read()
                    
                    # Calcular el porcentaje de puntaje obtenido y el número de palabras únicas que suman puntos
                    porcentaje, palabras_unicas = contar_palabras(letra_cancion, palabras_clave, numeros)
                    
                    print(f"Porcentaje de puntaje obtenido: {porcentaje:.2f}%")
                    print(f"Número total de palabras únicas que suman puntos: {palabras_unicas}")
                    return
                
                except FileNotFoundError:
                    print(f"No se encontró el archivo '{nombre_archivo}'. Por favor, verifique el nombre del archivo.")
                    return
                except IOError:
                    print(f"Error al leer el archivo '{nombre_archivo}'.")
                    return
        
    # Si se ingresa un año o unidad inválida
    print("Selección inválida. Por favor seleccione un año del 5 al 8 y una unidad del 1 al 4.")

if __name__ == "__main__":
    main()