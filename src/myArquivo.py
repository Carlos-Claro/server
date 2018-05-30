import os
import string
from dominio import Dominio
import csv

class myArquivo(object):

    def __init__(self):
        self.pasta = "arquivos/"
        self.chave = []

    def get(self):
        arquivos = self.buscarArquivos()
        for a in arquivos:
            self.lerArquivo(a)
        return self.chave

    def buscarArquivos(self):
        self.arquivos = os.listdir(self.pasta)
        array = []
        if self.arquivos:
            for f in self.arquivos:
                array.append(f)
        return array

    def lerArquivo(self,f):
        with open(self.pasta + f,"r") as arquivo:
            csvreader = csv.reader(arquivo)
            # print(csvreader)
            numero = 0
            for row in csvreader:
                self.chave.append(Dominio(row))


if __name__ == "__main__":
    a = myArquivo()
    i = 0
    c = a.get()
    print(c)
    #
    # for b in a.get():
    #     for c in b:
    #         i = i+1
    #         print(i)
    #         print(c.get_dominio())

    # print(os.getcwd())
