from os import system, name
from random import randint
from time import sleep

VACIO = "X"
SNAKE = "S"
OBJETIVO = "*"
GUARDIA = "!"

COLOR_GRIS = "\033[90m"
COLOR_AMARILLO = "\033[33m"
COLOR_ROJO = "\033[31m"
COLOR_VERDE = "\033[32m"
COLOR_POR_DEFECTO = "\033[0m"

ALTO = 11

class BinarySnake:
    def __init__(self, largo:int, alto:int, guardias:int):
        self.mapa = [[VACIO] * largo for _ in range(alto)]
        
        self.largo = largo
        self.alto = alto
        self.base = 2 if largo <= 20 else 8 if largo <= 100 else 16
        
        self.snakeX = 0
        self.snakeY = 0
        self.moverSnake(0,5)
        
        self.guardias = guardias
        for _ in range(guardias):
            self.spawnear(GUARDIA)
        
        self.spawnear(OBJETIVO)
        self.objetivo = randint(0,(20 if self.base == 2 else 100 if self.base == 8 else 500))
    
    def obtenerBaseInt(self):
        return self.base
    def obtenerBaseStr(self):
        return "Binario" if self.base == 2 else "Octal" if self.base == 8 else "Hexadecimal"
    def obtenerBasePrefix(self):
        return "0b" if self.base == 2 else "0o" if self.base == 8 else "0x"
    
    def obtenerObjetivo(self):
        return self.objetivo
    def obtenerObjetivoConvertido(self):
        return calcularBase(self.objetivo,self.base)
    
    def moverSnake(self,x:int,y:int):
        currX = self.snakeX
        currY = self.snakeY
        
        finalX = max([0,min([currX+x,self.largo-1])])
        finalY = max([0,min([currY+y,self.alto-1])])
        
        stepX = 0 if x == 0 else -1 if x < 0 else 1
        stepY = 0 if y == 0 else -1 if y < 0 else 1
        
        while currX != finalX:
            currX += stepX
            currCasilla = self.obtenerCasilla(currX,currY)
            self.actualizarSnake(currX,currY)
            if currCasilla in (GUARDIA, OBJETIVO):
                return 1 if currCasilla == GUARDIA else 2
        
        while currY != finalY:
            currY += stepY
            currCasilla = self.obtenerCasilla(currX,currY)
            self.actualizarSnake(currX,currY)
            if currCasilla in (GUARDIA, OBJETIVO):
                return 1 if currCasilla == GUARDIA else 2
            
        return 0
        
        
    def spawnear(self,c:str):
        aux = True
        while aux:
            x = randint(1,self.largo)-1
            y = randint(1,self.alto)-1
            if self.obtenerCasilla(x,y) == VACIO:
                self.actualizarCasilla(x,y,c)
                aux = False
        
    def obtenerCasilla(self,x:int,y:int):
        return self.mapa[y][x]
    
    def actualizarCasilla(self,x:int,y:int,c:str):
        self.mapa[y][x] = c
        
    def actualizarSnake(self,x:int,y:int):
        self.actualizarCasilla(self.snakeX,self.snakeY,VACIO) 
        self.snakeX = x
        self.snakeY = y
        self.actualizarCasilla(self.snakeX,self.snakeY,SNAKE) 
        
    
    def mostrarMapa(self,condition:int=0):
        print(f'[BASE{self.obtenerBaseInt()}][{self.largo}x{self.alto}]')
        for y in self.mapa:
            for x in y:
                if x == SNAKE:
                    if (condition == 0):                        # JUGANDO
                        print(f'{COLOR_POR_DEFECTO}',end="")
                    elif (condition == 1):                      # PERDISTE
                        print(f'{COLOR_ROJO}',end="")
                    else:                                       # OBJETIVO
                        print(f'{COLOR_AMARILLO}',end="")
                elif x == GUARDIA:
                    print(f'{COLOR_ROJO}',end="")
                elif x == OBJETIVO:
                    print(f'{COLOR_AMARILLO}',end="")
                else:
                    print(f'{COLOR_GRIS}',end="")
                print(x,end="")
            print(f'{COLOR_POR_DEFECTO}')

def calcularBase(num:int,base:int):
    res = str()
    while num > 0:
        res = baseDigito(num%base)+res
        num //= base
    return res if res else "0"

def baseDigito(dig:int):
    c = "0123456789ABCDEF"
    return c[dig] if 0 <= dig < 16 else "?"

def calcularDecimal(num:str,base:int):
    
    res = int()
    e = len(num)-1
    for dig in num:
        if dig not in "0123456789ABCDEF"[0:base]:
            return -1
        
        res+=decimalDigito(dig)*(base**e)
        e-=1
    return res

def decimalDigito(dig:str):
    digitos = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    return int(digitos.get(dig,dig))

def clear():
    system('cls' if name == 'nt' else 'clear')



# EMPIEZA EL JUEGO AQUI

clear()
print(f'{COLOR_VERDE}BINARY SNAKE{COLOR_POR_DEFECTO}')
sleep(1)

while True:
    try:
        largo = int(input("Ingresar largo del pasillo: "))
    except:
        print("Ingresa un numero...\n")
        continue
    if 0 < largo:
        break
    print("Ingresa un numero mayor a 0...\n")

max_ = largo*ALTO-2 # se resta 2 para no contar la casilla de Snake y el Objetivo
while True:
    try:
        cantidadGuardias = int(input(f'Ingresar cantidad de guardias [0-{max_}]: '))
    except:
        print("Ingresa un numero...\n")
        continue
    if 0 <= cantidadGuardias <= max_:
        break
    print("Ingresa un numero dentro del rango...\n")

BS = BinarySnake(largo=largo,alto=ALTO,guardias=cantidadGuardias)

while True:
    clear()
    
    BS.mostrarMapa()
    accion = input("Ingresa una acción:\nw: ↑\na: ←\ns: ↓\nd: →\n-1: Salir\nAcción: ").lower()
    
    if accion == "-1":
        clear()
        break
    if accion not in ["w","a","s","d"]:
        print("Ingresa una acción valida...")
        sleep(1)
        continue
    
    res = int()
    while True:
        distancia = calcularDecimal(input(f'Ingresa la distancia a recorrer en formato {BS.obtenerBaseStr()}: ').upper(),BS.base)
        if distancia == -1:
            print(f'Ingresa un numero valido en formato {BS.obtenerBaseStr()}...')
            sleep(1)
            continue
        
        direccion = {"w":(0,-distancia),"s":(0,distancia),"d":(distancia,0),"a":(-distancia,0)}
        res = BS.moverSnake(x=direccion[accion][0],y=direccion[accion][1])
        
        break
    clear()
    
    if res == 1: # GUARDIA
        BS.mostrarMapa(1)
        print(f'{COLOR_ROJO}Te atrapo un guardia. Perdiste!{COLOR_POR_DEFECTO} :(')
        break
    
    if res == 2: # OBJETIVO
        BS.mostrarMapa(2)
        print("Haz llegado al objetivo! :O")
        print(f'{COLOR_VERDE}',end="")
        print("Iniciado hackeo...")
        
        sleep(1)
        
        while True:
            try:
                num = int(input(f'{COLOR_ROJO}[{BS.obtenerBasePrefix()}{BS.obtenerObjetivoConvertido()}] → Necesita ser convertido de {BS.obtenerBaseStr()} a Decimal para continuar:{COLOR_POR_DEFECTO} '))
            except:
                print(f'{COLOR_ROJO}Ingresa un numero...')
                continue
            finally:
                break
        
        sleep(1)
        print(f'{COLOR_VERDE}...')
        sleep(2)
        
        if num != BS.obtenerObjetivo():
            print(f'{COLOR_ROJO}Decimal incorrecto, hackeo interrumpido. Perdiste!{COLOR_POR_DEFECTO} :(')
            break
        
        print(f'Hackeo completado. {COLOR_AMARILLO}Ganaste {COLOR_POR_DEFECTO}:D')
        break