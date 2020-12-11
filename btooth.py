import bluetooth
from gpiozero import LED

led = LED(21)   # Initializing pin 40 for led

host = ""
port = 1        # Raspberry Pi uses port 1 for Bluetooth Communication

# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')

try:
        server.bind((host, port))
        print("Bluetooth Binding Completed")
except:
        print("Bluetooth Binding Failed")

server.listen(1) # One connection at a time
# Server accepts the clients request and assigns a mac address.
client, address = server.accept()
print("Connected To", address)
print("Client:", client)
try:
        while True:
                # Receivng the data.
                data = client.recv(1024) # 1024 is the buffer size.
                x = data.decode()
                print(x)

                if x == "1":
                        led.on()
                        send_data = "Light On "
                elif x == "0":
                        led.off()
                        send_data = "Light Off "
                else:
                        send_data = "Type 1 or 0 "
                # Sending the data.
                client.send(send_data)
except:
        # Making all the output pins LOW
        led.close()
        # Closing the client and server connection
        client.close()
        server.close()
