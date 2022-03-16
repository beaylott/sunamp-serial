import serial
import time
import urllib3
import json

http = urllib3.PoolManager()

emoncms_url = "https://emoncms.org/input/post?node={NODE}&apikey={APIKEY}&fulljson={JSON}"

NODE = "sunamp"
APIKEY = "" #emoncms RW API key

sunamp_data_params_v1 = ['T1', 'T2', 'T3', 'T4', 'T5', 'relay1', 'relay2']

# This is connected to V1 sunamp - values read are byte aligned numbers corresponding to above params as inferred from technical documentation and correspondence with sunamp
sensor_id1 = "FTBWZFSS"

# This is connected to V2 sunamp - values read are in a JSON format with param names included
sensor_id2 = "FTBWZH3T"

with serial.Serial(f'/dev/serial/by-id/usb-FTDI_TTL232R-3V3_{sensor_id1}-if00-port0', 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1) as ser1:
    with serial.Serial(f'/dev/serial/by-id/usb-FTDI_TTL232R-3V3_{sensor_id2}-if00-port0', 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1) as ser2:
        while(True):
            if (ser1.inWaiting() > 0):
                data_str = ser1.readline().decode('ascii')
                JSON = json.dumps(
                    dict(zip(sunamp_data_params_v1, data_str.strip('\r').strip(' ').split(','))) | {"serial_id": sensor_id1})
                print(f'{sensor_id1}: {JSON}')
                if len(data_str) > 2:
                    r = http.request('GET', emoncms_url.format(
                        NODE=NODE+'-'+sensor_id1, APIKEY=APIKEY, JSON=JSON))
                    print(r.data)

            if (ser2.inWaiting() > 0):
                data_str = ser2.readline().decode('ascii')
                JSON = json.dumps(
                    dict([x.strip("\n").split(':') for x in data_str.replace(' ', '').split(',')]) | {"serial_id": sensor_id2})
                print(f'{sensor_id2}:{JSON}')
                if len(data_str) > 2:
                    r = http.request('GET', emoncms_url.format(
                        NODE=NODE+'-'+sensor_id2, APIKEY=APIKEY, JSON=JSON))
                    print(r.data)
            time.sleep(0.01)
