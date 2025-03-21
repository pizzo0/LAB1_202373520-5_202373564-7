import os
import random
import time

VACIO = "▢"
SNAKE = "◉"
OBJETIVO = "✦"
GUARDIA = "▪"

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
        self.objetivo = random.randint(0,(20 if self.base == 2 else 100 if self.base == 8 else 500))
    
    def obtenerBaseInt(self):
        return self.base
    def obtenerBaseStr(self):
        return "Binario" if self.base == 2 else "Octal" if self.base == 8 else "Hexadecimal"
    
    def obtenerObjetivo(self):
        return self.objetivo
    def obtenerObjetivoConvertido(self):
        return calcularBase(self.objetivo,self.base)

    
    def moverSnake(self,x:int,y:int):
        x = x + self.snakeX
        y = y + self.snakeY
        
        if x < 0 or x >= self.largo or y < 0 or y >= self.alto:
            return 3
        
        casilla = self.obtenerCasilla(x,y)
        if casilla == GUARDIA:
            return 1
        if casilla == OBJETIVO:
            return 2
        
        self.actualizarCasilla(self.snakeX,self.snakeY,VACIO) 
        
        self.snakeX = x
        self.snakeY = y
        self.actualizarCasilla(self.snakeX,self.snakeY,SNAKE) 
        
        return 0
        
    def spawnear(self,c:str):
        aux = True
        while aux:
            x = random.randint(1,self.largo)-1
            y = random.randint(1,self.alto)-1
            if self.obtenerCasilla(x,y) == VACIO:
                self.actualizarCasilla(x,y,c)
                aux = False
        
    def obtenerCasilla(self,x:int,y:int):
        return self.mapa[y][x]
    
    def actualizarCasilla(self,x:int,y:int,c:str):
        self.mapa[y][x] = c
    
    def mostrarMapa(self):
        for y in self.mapa:
            for x in y:
                print(x,end="")
            print()

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
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

largo = int(input("Ingresar largo del pasillo: "))
cantidadGuardias = int(input("Ingresar cantidad de guardias: "))

BS = BinarySnake(largo=largo,alto=ALTO,guardias=cantidadGuardias)

movimiento = 0
while True:
    clear()
    
    movimiento += 1
    print(f'[{BS.largo}x{BS.alto}] - Movimiento {movimiento}')
    
    BS.mostrarMapa()
    accion = input("Ingresa una acción:\nw: ↑\na: ←\ns: ↓\nd: →\n-1: Salir\nAcción: ")
    
    if accion == "-1":
        clear()
        break
    if accion not in "wasd":
        print("Ingresa una acción valida...")
        time.sleep(1)
        continue
    
    res = int()
    while True:
        distancia = calcularDecimal(input(f'Ingresa la distancia a recorrer en formato {BS.obtenerBaseStr()}: '),BS.base)
        if distancia == -1:
            print(f'Ingresa un numero valido en formato {BS.obtenerBaseStr()}...')
            time.sleep(1)
            continue
        
        direccion = {"w":(0,-distancia),"s":(0,distancia),"d":(distancia,0),"a":(-distancia,0)}
        res = BS.moverSnake(x=direccion[accion][0],y=direccion[accion][1])
        
        if res == 3: #FUERA DE RANGO
            print(f'Ingresa una distancia sin salirte del mapa...')
            time.sleep(1)
            continue
        
        break
    
    clear()
    
    if res == 1:
        print("Te atrapo un guardia. Perdiste! :(")
        break
    if res == 2:
        print("Haz llegado al objetivo! :O")
        while True:
            print("Iniciado hackeo")
            
            time.sleep(1)
            print("...")
            time.sleep(1)
            
            num = int(input(f'[{BS.obtenerObjetivoConvertido()}] → Necesita ser convertido a Decimal para continuar: '))
            
            time.sleep(1)
            print("...")
            time.sleep(1)
            
            if num != BS.obtenerObjetivo():
                print("Decimal incorrecto, hackeo interrumpido. Perdiste :(")
                break
            
            print("Hackeo completado. Ganaste :D")
            break
        break