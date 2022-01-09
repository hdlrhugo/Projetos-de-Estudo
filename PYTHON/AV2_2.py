#include<stdio.h>
#Hugo de Lima
# Questão 2
def qtd_segundos(segundos):
    minutos, segundo = divmod(segundos, 60)
    hora, minuto = divmod(minutos, 60)
    hora = Hora(hora, minuto, segundo)
    return hora



class Hora:
    def _init_(self, hora=0, minuto=0, segundo=0):
     self.hora = hora
     self.minuto = minuto
     self.segundo = segundo


def get_hora(self):
    return self.hora

def get_minutos(self):
    minutos = self.hora * 60 + self.minuto
    return minutos

def get_segundos(self):
    segundos = self.get_minutos() * 60 + self.segundo
    return segundos


def add_horas(self, segundos):
    segundos += self.get_segundos()



def _str_(self):
    return '%.2d:%.2d:%.2d' % (self.hora, self.minuto, self.segundo)

def print_hora(self):
    print(str(self))
# HORA DA VERDADE
def main():
    inicio = Hora(0, 0, 0)
    inicio.print_hora()
    fim1 = inicio.add_horas(300)
    fim1.print_hora()
    fim2 = inicio.add_horas(366)
    fim2.print_hora()
    print(inicio, fim1, fim2)
    if __name__== '_main_':
        main()

