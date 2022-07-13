# test_connect.py 
import paho.mqtt.client as mqtt 
import ssl
import time

# The callback function. It will be triggered when trying to connect to the MQTT broker
# client is the client instance connected this time
# userdata is users' information, usually empty. If it is needed, you can set it through user_data_set function.
# flags save the dictionary of broker response flag.
# rc is the response code.
# Generally, we only need to pay attention to whether the response code is 0.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected success')
    else:
        print('Connected fail with code {}'.format(rc))

def on_publish(client,userdata,result):             #create function for callback
    print("data published.\nClient{}\nUserdata:{}\nResult:{}".format(client,userdata,result))

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
client = mqtt.Client()
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.on_connect = on_connect 
client.on_publish = on_publish
client.username_pw_set('admin',password='Uedsoldier00*')
client.tls_insecure_set(True)
client.connect('192.168.0.12', 8883, 60) 
cnt = 0
while(True):
    client.publish('test','Hola '+str(cnt),qos=2)
    client.loop(0.2)
    cnt += 1
    time.sleep(5)

    