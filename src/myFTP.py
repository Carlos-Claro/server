import os
import string
from dominio import Dominio
from ftplib import FTP
class myFTP(object):

    def __init__(self):
        self.ftp = '201.22.56.213'
        self.user = 'programacao'
        self.password = ''
        self.ftp = FTP(self.ftp)
        self.ftp.login(user = self.user, passwd = self.password)
        # self.ftp.retrlines('LIST')
        self.ftp.cwd('Documentos/clientes')
        self.ftp.retrlines('LIST')
        self.ftp.close()


if __name__ == "__main__":
    a = myFTP()
