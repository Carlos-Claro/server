import os
import string
from myArquivo import myArquivo

class MyApache(object):

    def __init__(self):
        self.dominios = []

    def setArquivo(self):
        arquivo = myArquivo();
        self.dominios = arquivo.get()

    def setApache(self):
        for linha in self.dominios:
            self.criaApacheConf(linha)

    def criaApacheConf(self,domain):
        with open("modelos/site.conf","r") as matriz:
            data = matriz.read().format(URL=domain.get_dominio(),DIR="/var/www/html/portais_novo/", APACHE_LOG_DIR="{APACHE_LOG_DIR}")
            nomeArquivo = domain.get_dominio() + ".conf"
            localArquivo = "../sites/apache/" + nomeArquivo
            print(localArquivo)
            novoSite = open(localArquivo,"w")
            novoSite.write(data)
            novoSite.close()
            # os.system("echo 4 | sudo -S mv " + localArquivo + " /etc/apache2/sites-available/")
            # os.system("echo 4 | sudo -S ln -s /etc/apache2/sites-available/" + nomeArquivo + " /etc/apache2/sites-enabled/" + nomeArquivo)

    # def moveRestart(self):
    #     os.system("echo 4 | sudo -S /etc/init.d/apache2 restart")



if __name__ == "__main__":
    a = MyApache()
    a.setArquivo()
    a.setApache()
