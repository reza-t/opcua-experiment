from opcua import Client, ua

client = Client("opc.tcp://127.0.0.1:12345")
client.connect()

client.get_namespace_array()
objects = client.get_objects_node()
# objects.get_children()
bulb = objects.get_children()[2]
tempsens = objects.get_children()[1]
# bulb.get_children()
# bulb.get_children()[0].get_browse_name()
state = bulb.get_children()[0]
# state.get_value()
state.set_value(True)
tempsens.get_children()
for i in tempsens.get_children():
    print(i.get_value())

temp = client.get_node('ns=2;s="TS1_Temperature"')
print(temp.get_browse_name())
print(temp.get_value())
client.close_session()
