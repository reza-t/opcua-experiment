import time

from opcua import Client, ua

client = Client("opc.tcp://127.0.0.1:4841")
client.set_user("test")
client.set_password("test2")
client.security_policy = ua.SecurityPolicy
try:
    client.connect()
    print("Client Connected")
    while True:
        nodid = "ns=2;i=2"
        temp = client.get_node(nodid)

        temperature = temp.get_value()

        print("temperature", temperature)

        hum = client.get_node("ns=2;i=3")
        humidity = hum.get_value()
        print("humidity", humidity)

        loc = client.get_node("ns=2;i=4")
        location = loc.get_value()
        print("location", location)
        # out = < string -> variant>
        time.sleep(2)
finally:
    client.disconnect()
    print("Client disconnect")
