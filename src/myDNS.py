import os
import string
from myArquivo import myArquivo
from datetime import datetime

class MyDNS(object):

    def __init__(self):
        self.dominios = []


    def setArquivo(self):
        arquivo = myArquivo();
        self.dominios = arquivo.get()

    def setLocal(self):
        for dominio in self.dominios:
            self.criaLocalaconf(dominio)

    def setDireto(self):
        for dominio in self.dominios:
            self.criaDnsdireto(dominio)

    def criaLocalaconf(self,domain):
        # print(domain.get_dominio(),domain.get_ip(),domain.get_ipReverso(),datetime.today().strftime("%Y%m%d%H"),"{","}");
        with open("modelos/dns/named.conf.local","r") as matrizDns:
            dataDns = matrizDns.read().format(URL=domain.get_dominio(),IP=domain.get_ip(),IPA=domain.get_ipReverso(),DATA=datetime.today().strftime("%Y%m%d%H"),ABRE="{",FECHA="}")
            nomeArquivo = "../sites/dns/conf/named.conf.local"
            novoSite = open(nomeArquivo,"a")
            novoSite.write(dataDns)
            novoSite.close()
        with open("modelos/dns1/named.conf.local","r") as matriz:
            dataDns1 = matriz.read().format(URL=domain.get_dominio(),IP=domain.get_ip(),IPA=domain.get_ipReverso(),DATA=datetime.today().strftime("%Y%m%d%H"),ABRE="{",FECHA="}")
            nomeArquivo = "../sites/dns1/conf/named.conf.local"
            novoSite = open(nomeArquivo,"a")
            novoSite.write(dataDns1)
            novoSite.close()

    def criaDnsdireto(self,domain):
        with open("modelos/dns/admin.powempresas.com.direto","r") as matriz:
            data = matriz.read().format(URL=domain.get_dominio(),IP=domain.get_ip(),IPA=domain.get_ipReverso(),DATA=datetime.today().strftime("%Y%m%d%H"),ABRE="{",FECHA="}")
            nomeArquivo = "../sites/dns/dominios/" + domain.get_dominio() + ".direto"
            novoSite = open(nomeArquivo,"w")
            novoSite.write(data)
            novoSite.close()
        with open("modelos/dns/geral.reverso","r") as matriz:
            data = matriz.read().format(URL=domain.get_dominio(),IP=domain.get_ip(),IPA=domain.get_ipReverso(),DATA=datetime.today().strftime("%Y%m%d%H"),ABRE="{",FECHA="}")
            nomeArquivo = "../sites/dns/dominios/geral.reverso"
            novoSite = open(nomeArquivo,"a")
            novoSite.write(data)
            novoSite.close()
        with open("modelos/dns1/powempresas.com.direto","r") as matriz:
            data = matriz.read().format(URL=domain.get_dominio(),IP=domain.get_ip(),IPA=domain.get_ipReverso(),DATA=datetime.today().strftime("%Y%m%d%H"),ABRE="{",FECHA="}")
            nomeArquivo = "../sites/dns1/dominios/" + domain.get_dominio() + ".direto"
            novoSite = open(nomeArquivo,"w")
            novoSite.write(data)
            novoSite.close()
        with open("modelos/dns1/geral.reverso","r") as matriz:
            data = matriz.read().format(URL=domain.get_dominio(),IP=domain.get_ip(),IPA=domain.get_ipReverso(),DATA=datetime.today().strftime("%Y%m%d%H"),ABRE="{",FECHA="}")
            nomeArquivo = "../sites/dns1/dominios/geral.reverso"
            novoSite = open(nomeArquivo,"a")
            novoSite.write(data)
            novoSite.close()


if __name__ == "__main__":
    a = MyDNS()
    a.setArquivo()
    a.setLocal()
    a.setDireto()
