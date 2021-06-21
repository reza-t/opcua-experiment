from time import sleep
import random
from opcua import Server, ua


server = Server()
server.set_endpoint("opc.tcp://127.0.0.1:4841")
server.set_security_policy([
    ua.SecurityPolicyType.NoSecurity
])

name = "OPCUA_ROOM-SERVER"
address_space = server.register_namespace(name)

node = server.get_objects_node()

param = node.add_object(address_space, "Parameters")

temp = param.add_variable(address_space, "Temperature", 0.0)
humidity = param.add_variable(address_space, "Temperature", 0.0)
loc = param.add_variable(address_space, "Location", "Kiel")

temp.set_writable()
humidity.set_writable()
loc.set_writable()

temperature = 20.0
try:
    print("Start Server")
    server.start()
    print("Server Online")
    while True:
        temperature = random.uniform(-1, 1)
        temp.set_value(temperature)
        humidity.set_value(random.uniform(0, 100))

        print(temp.get_value(), humidity.get_value(), loc.get_value())

        sleep(2)
finally:
    server.stop()
    print("Server Offline")
