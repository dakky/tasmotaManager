from mqtt.mqtt import Mqtt
from models.device import Device
from typing import List

def run():
    mqtt_instance = Mqtt()
    # get a list of devices
    devices: List[Device] = mqtt_instance.get_devices()

if __name__ == '__main__':
    run()