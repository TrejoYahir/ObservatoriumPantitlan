lista_oid = [
            '1.3.6.1.2.1.4.20.1.1', #Direccion ip
            '1.3.6.1.2.1.1.5.0', #Nombre de la pc
            '1.3.6.1.2.1.1.1.0', #Datos del sistema
            '1.3.6.1.2.1.2.1.0',#No interfaces de red
            '1.3.6.1.2.1.1.3.0', #Tiempo de actividad desde el ultimo reinicio
            '1.3.6.1.2.1.1.6.0', #Ubicacion fisica
            '1.3.6.1.2.1.1.4.0', #Información de contacto del admon
            '1.3.6.1.2.1.2.2.1.10.3', #No. total de octetos recibidos (este no)
            '1.3.6.1.2.1.2.2.1.16.3'] #No. total de octetos enviados (este no)
monitoreosSNMP = [['trafico',
                   '1.3.6.1.2.1.2.2.1.10.3',
                   '1.3.6.1.2.1.2.2.1.16.3',
                   "Tráfico de interfaz"],
                  ['segmentostcp',
                   '1.3.6.1.2.1.6.10.0',
                   '1.3.6.1.2.1.6.11.0',
                   "Segmentos TCP"],
                  ['datagramaUDP',
                   '1.3.6.1.2.1.7.1.0',
                   '1.3.6.1.2.1.7.4.0',
                   "Datagramas UDP"],
                  ['paquetesSNMP',
                   '1.3.6.1.2.1.11.1.0',
                   '1.3.6.1.2.1.11.2.0',
                   "Paquetes SNMP"],
                  ['entradasicp',
                   '1.3.6.1.2.1.5.1.0',
                   '1.3.6.1.2.1.5.14.0',
                   "Entradas ICP"]]