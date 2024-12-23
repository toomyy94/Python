import socket
import sys
import csv
import json
import random
import time


# requisitos funcionais:

# 1. Se for iniciado com um número de argumentos inferior a 3, este deverá imprimir
# a ajuda no seguinte formato: python3 client.py interval num [country or id]

# 2. Se for iniciado com um qualquer argumento inválido (tipo errado, valor incorreto
# ou não encontrado), deverá ser apresentada uma mensagem de erro respetiva aoargumento que gera o erro.

# 3. Se for indicado um texto no terceiro argumento, o teste deverá ser realizado para
# um qualquer servidor aleatório daquele país.

# 4. Se for indicado um valor inteiro no terceiro argumento, o teste deverá ser realizado
# para o servidor com esse identificador.

# 5. O primeiro argumento deverá consistir num valor inteiro positivo, especificando o
# tempo que decorre entre dois testes realizados.

# 6. O segundo argumento deverá consistir num valor inteiro positivo, especificando o
# número de testes a serem realizados.

# 7. Caso não seja possível contactar um servidor específico, o programa deve apresentar
# uma mensagem significativa e iniciar um novo teste após o tempoEspera especificado.
# Neste caso, a largura de banda registada deverá será de 0 e a latência será de -1.

# 8. O ficheiro report.csv deverá possuir a seguinte estrutura: contador, id do
# servidor, data e hora no formato ISO, latência, largura de banda, check.

# 9. O campo check deverá conter a síntese calculada sobre a concatenhação de todos
# os campos anteriores, pela ordem apresentada, e sem qualquer separador.

# 10. O cliente deverá realizar uma descarga entre 10MB e 100MB, ou até que passem 10 segundos.

# 11. A taxa de largura de banda deve ser calculada pelo número de octetos recebidos
# sobre o tempo decorrido, após ter sido obtido 1MB.

# 12. A latência deve ser calculada pelo tempo médio de 10 transações PING/PONG.

# 13. O cliente deverá ler um ficheiro denominado key.priv, contendo uma chave privada RSA.

# 14. Ao terminar o cliente deverá escrever um ficheiro report.sig com uma assinatura do relatório por esta chave.


if len(sys.argv) < 4:
    print("Executar no terminal as: py teste2.py interval num [country or id]")
    sys.exit(0)

nServers = 0

if sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
    if int(sys.argv[1]) < 0:
        print("tempoEspera: %d necessita ser positivo" % sys.argv[1])
        sys.exit(0)
    if int(sys.argv[2]) < 0:
        print("nTestes: %d necessita ser positivo" % sys.argv[2])
        sys.exit(0)
else:
    print("tempoEspera e/ou nTestes necessitam de ser numeros")
    sys.exit(0)

tempoEspera = int(sys.argv[1])
nTestes = int(sys.argv[2])

with open('servers.json') as ficheiro:
    servers = json.load(ficheiro)

host = ""

if sys.argv[3].isnumeric(): #id
    countryOrID = int(sys.argv[3])
    for umServer in servers['servers']:
        if umServer['id'] == countryOrID:
            incrementaFor = incrementaFor + 1
            print("Pais escolhido: " + str(umServer['country']) + "(" + str(umServer['id']) + ") - " + str(umServer['name']))
            host = umServer['host']
            break
    else:
        print("Server nao encontrado")
        sys.exit(0)
else:  # Letras (pais)
    countryOrID = sys.argv[3]
    for umServer in servers['servers']:
        if umServer['country'] == countryOrID: #country
            nServers += 1 #contar numero de servidores do pais

    if nServers >= 1:
        randomServer = random.randint(0, nServers - 1)  # random server do pais
        incrementaFor = 0
        for umServer in servers['servers']:
            if umServer['country'] == countryOrID:
                if incrementaFor == randomServer:
                    host = umServer['host']
                    break
                incrementaFor +=1
        print("Pais escolhido: " + str(umServer['country']) + "(" + str(umServer['id']) + ") - " + str(umServer['name']))
    else:
        print("Pais nao encontrado")
        sys.exit(0)

url = host.split(":")[0]
port = host.split(":")[1]
serverTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("A ligar a: " + url)
try:
    serverTCP.connect((url, int(port)))
except socket.error as exc:
    print("Falha na coneção ao servidor, verificar ligação à Internet: %s" % exc)
    sys.exit(0)

print("HI")
serverTCP.send(b"HI\n")
print(serverTCP.recv(2048).decode("utf-8"))

if serverTCP == 0:
    print("Servidor em baixo")
else:
    pingToCsv = 0
    pingTotal = 0
    tsPongAnterior = 0
    incrementaFor = 0
    print("Playing PING PONG, retriving latencys...")
    for i in range(11):

        tsPing = int(time.time() / 1000) #milisegundos
        str_data = "PING " + str(tsPing) + "\n"
        b_data = str_data.encode("utf-8")
        serverTCP.send(b_data)

        b_data = serverTCP.recv(2048)
        str_data = b_data.decode("utf-8")
        data_to_split = str_data.split(" ")

        tsPong = int(data_to_split[1])

        umPing = tsPong - tsPongAnterior
        tsPongAnterior = tsPong
        incrementaFor += 1

        if incrementaFor > 1:
            pingTotal = pingTotal + umPing

    pingToCsv = pingTotal / 10

    print("Ping acabado!: " + str(pingToCsv) + "s\n")

    countTestes = 0
    bytesToMB = 1000000
    microToSecond = 1000000  # para obeter tempo em segundos

    for x in range(nTestes):
        print("A começar download #" + str(countTestes+1) + "...")

        randomMbytesToDownload = random.randint(10, 100)

        randomMBtoBytes = randomMbytesToDownload * bytesToMB

        print("a sacar: (DOWNLOAD " + str(randomMBtoBytes) + ")bytes")
        str_data = ("DOWNLOAD " + str(randomMBtoBytes) + "\n")
        b_data = str_data.encode("utf-8")
        serverTCP.send(b_data)
        downloadStartTime = int(time.time())

        totalBytes = 0
        tempoFinalpMedia = 0

        while 1:
            resp = serverTCP.recv(4098)
            totalBytes += len(resp)

            if totalBytes == randomMBtoBytes:
                print("sai por acabar o download")
                downloadFinalTime = int(time.time())
                tempoFinalpMedia = (downloadFinalTime - downloadStartTime)
                break;

            if not resp or time.time() - downloadStartTime >= 10:
                print("sai por passar 10segundos")
                downloadFinalTime = int(time.time())
                tempoFinalpMedia = int((downloadFinalTime - downloadStartTime))
                break;

        print("Saquei " + str((totalBytes * 8) / bytesToMB) + "Mb") #Megabit
        print("em " + str(tempoFinalpMedia) + "s")
        speed = ((totalBytes * 8) / tempoFinalpMedia) / bytesToMB #bytes->bits->Mb->Mb/s

        print("Speed: %d Mb/s\n" % speed)

        countTestes += 1
        if(countTestes < nTestes):
            print("esperando " + str(tempoEspera) + "s pelo proximo teste")
        time.sleep(tempoEspera)

    # fazer media dos 3 speeds
    # obter speedFinalToCsv

    print("Fechando ligacao: QUIT\n")
    str_data = "QUIT\n".encode("utf-8")
    serverTCP.send(str_data)
    serverTCP.close()

#fazer csv
list1 = ["contador", "id", "date", "ping", "speed", "check"]

with open("report.csv", "a", newline='') as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(list1)

    count = 0
    list1 = [str(count), str(umServer['id']), str("dataXXX"), str(pingToCsv), str(speed), str(str(count+umServer['id'])+str("dataXXX")+str(pingToCsv)+str(speed))]

    #for
    wr.writerow(list1)

print("report.csv criado!\nProgram closing...\n")

