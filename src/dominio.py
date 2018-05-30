
class Dominio(object):
    def __init__(self,dominio):
        self.dominio = dominio[0].strip().lower()
        self.ip = "201.16.246.176"
        self.ipReverso = "201.16.246.18"
        if( dominio[1] ):
            self.ip = dominio[1]
        if(dominio[2]):
            self.ipReverso = dominio[2]


    def __repr__(self):
        return "dominio:%s ip:%s ipReverso:%s" % (self.dominio, self.ip, self.ipReverso)

    def get_dominio(self):
        return self.dominio

    def get_ip(self):
        return self.ip

    def get_ipReverso(self):
        return self.ipReverso
