class FechaHora:
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self, dia=1, mes=1, año=2020, hora=0, minutos=0, segundos=0):
        self.__dia = dia
        self.__mes = mes
        self.__año = año
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        return 'Fecha:{}/{}/{}\n\tHora: {}:{}:{}'.format(self.__dia, self.__mes, self.__año, self.__hora,
                                                         self.__minutos, self.__segundos)

    def getHORA(self):
        return '{}:{}:{}'.format(self.__hora, self.__minutos, self.__segundos)
    def getHora(self):
        return self.__hora

    def getMin(self):
        return self.__minutos

    def getSeg(self):
        return self.__segundos

    def getDIA(self):
        return self.__dia

    def getMES(self):
        return self.__mes

    def getANIO(self):
        return self.__año

        # def __add__(self, otraHora):
        #    return FechaHora(self.__hora + otraHora.getHora(), self.__minutos + otraHora.getMin(), self.__segundos + otraHora.getSeg())

    def __add__(self, otraFecha):
        #print("Estoy en la clase HORA en el add")
        print("SELF", type(self))
        print("OTRO", type(otraFecha))

        aux = self
        h = self.getHora() + otraFecha.getHora()
        m = self.getMin() + otraFecha.getMin()
        s = self.getSeg() + otraFecha.getSeg()

        aux = FechaHora(otraFecha.getDIA(), otraFecha.getMES(), otraFecha.getANIO(), h, m, s)
        return aux

    def __sub__(self, otraFecha):
        #print("Estoy en la clase HORA en el add")
        print("SELF", type(self))
        print("OTRO", type(otraFecha))

        aux = self
        h = self.getHora() - otraFecha.getHora()
        m = self.getMin() - otraFecha.getMin()
        s = self.getSeg() - otraFecha.getSeg()

        aux = FechaHora(otraFecha.getDIA(), otraFecha.getMES(), otraFecha.getANIO(), h, m, s)
        return aux


    def __gt__(self, otraFecha):
        #print("Estoy en la clase HORA en el add")
        print("SELF", type(self))
        print("OTRO", type(otraFecha))

        aux = self
        h = self.getHora() > otraFecha.getHora()
        m = self.getMin() > otraFecha.getMin()
        s = self.getSeg() > otraFecha.getSeg()
        print("Resultados de comparaciones:")

        aux = FechaHora(otraFecha.getDIA(), otraFecha.getMES(), otraFecha.getANIO(), h, m, s)


        return aux


    def ponerEnHora(self, hora=0, minuto=0, segundo=0):
        self.__hora = hora
        self.__minutos = minuto
        self.__segundos = segundo

    def Mostrar(self):
        s=' ' + repr(self.__dia) + '/' + repr(self.__mes) + '/' + repr(self.__año) + ' '+repr(self.__hora)+':'+repr(self.__minutos)+':'+repr(self.__segundos)
        #repr muestra lo imprimible
        print(s)

    def AdelantarHora(self, hora=0, minuto=0, seg=0):
        self.__hora+=int(hora)
        self.__minutos+=int(minuto)
        self.__segundos+=int(seg)
        if self.__segundos>59:
            self.__segundos = self.__segundos-60
            self.__minutos+=1
        if self.__minutos>59:
            self.__minutos = self.__minutos-60
            self.__hora+=1
        if self.__hora>=24:
            self.__hora = self.__hora-24
            self.__dia=self.__dia+1
        if (self.__mes==11 or self.__mes==4 or self.__mes==6 or self.__mes==9):
            if self.__dia>30:
                self.__dia-=30
                self.__mes+=1

            else:
                if (self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or self.__mes==12):
                    if self.__dia>31:
                        if self.__mes==12:
                            self.__año+=1
                            self.__mes=1
                        else:
                            self.__mes+=1
                            self.__dia-=31

                    else:
                        if bisiesto (self.__año):
                            if self.__dia>29:
                                self.__dia-=29
                        else:
                            if self.__dia>28:
                                self.__dia-=28
                        self.__mes+=1











#d=int(input("Ingrese Dia: "))
#mes=int(input("Ingrese Mes: "))
#a=int(input("Ingrese Año: "))
#h=int(input("Ingrese Hora: "))
#m=int(input("Ingrese Minutos: "))
#s=int(input("Ingrese Segundos: "))
#gere=FechaHora(d,mes,a,h,m,s)







