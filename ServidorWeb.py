import socket

tcpsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcpsocket.bind(("0.0.0.0",8000))
tcpsocket.listen(2)
print("Esperando conexiones..")
(client,(ip,sock))=tcpsocket.accept()
print("conexión recibida de :",ip)
print("comenzando la salida del echo ...")
data='basura'

while len(data):
    data=client.recv(2048)
    print("Envio cliente :",data)
    client.send(data)
print("Cerrando la conexión")
client.close();

