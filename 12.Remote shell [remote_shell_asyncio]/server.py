import asyncio
import time
import subprocess
import argparse


#Handle commands on remote shell
async def handle_commands(reader, writer):
    # List all tasks (only test)
    """ for t in asyncio.all_tasks():
        print(f"Tarea: {t}") """

    #Get extra info (peername)
    addr = writer.get_extra_info('peername')
    
    # Conected client
    print(f"👨‍💻 Cliente {addr!r} conectado ✅")

    while(True):
        
        #Await to read 100 bytes
        data = await reader.read(100)
        #Decode read data and get commands
        command = data.decode()

        if(command == "exit"):
            print(command)
            writer.write(bytearray("bye", encoding='utf-8'))
            await writer.drain()
            break

        #Print command and client peername
        print(f"👨‍💻 Cliente {addr!r} envía 🛰")
        print(f"🎛 Comando :  {command!r}")

        #This runs commands on your server whith Popen
        proceso = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        #Get output and error from popen
        out,err = proceso.communicate()

        #Format output and error as a unified message
        response = out + err

        #Write response on client terminal
        writer.write(response)
        
        #Drain
        await writer.drain()

    #Close task
    writer.close()

    #Print closed task (only test)
    """ for t in asyncio.all_tasks():
    print(f"---> Cerrando Tarea: {t}") """


#Main Function async
async def main():

    # Args defintion and description
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument("--host", type=str, help="string")
    parser.add_argument("--port", type=int, help="int")

    # Get args
    args = parser.parse_args()

    #If you dont have args start server on 127.0.0.1:8888
    try:
        #Start server on host and port
        server = await asyncio.start_server(
        handle_commands, args.host, args.port)
    except ValueError:
        #Start server on host and port default
        print("❌ No se proposionaron argumentos ❌. Modo default ⛺")
        server = await asyncio.start_server(
        handle_commands, '127.0.0.1', 8888)

    #Get socket name
    addr = server.sockets[0].getsockname()
    print(f'🚀 Sirviendo en {addr} 🛸')


    # List all task of the asyncio and start acepting connections
    async with server:
        #print(f"--->Tareas:\n{asyncio.all_tasks()}")
        await server.serve_forever()

# RUN
asyncio.run(main())


