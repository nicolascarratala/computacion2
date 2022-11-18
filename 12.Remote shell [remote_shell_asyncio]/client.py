import socket 
servidor="127.0.0.1"
direcciones = socket.getaddrinfo(servidor, 8888, socket.AF_UNSPEC, 1)

for direccion in direcciones:

    #Some info
    s = socket.socket(direccion[0], direccion[1])
    print("🛰 Conectando a :", direccion[4])
    s.connect((direccion[4]))

    #Infinite loop
    while(True):
        comandostr = str(input("🎛 Escriba comando: "))
        #Get Byte array of str
        comando = bytearray(comandostr, encoding='utf-8')
        #Send command
        s.send(comando)
        #Get response and print
        response = s.recv(1024).decode("utf-8")
        print(f"📡 Respuesta: {response}")
        #If write exit then break and close
        if(response == "bye"): break

    s.close()