import time
import random
import paho.mqtt.client as mqtt_client
from typing import List
from models.device import Device
from config.config import config


class Mqtt:

    def __init__(self):
        self.broker = config['mqtt']['broker'].get()
        self.port = config['mqtt']['port'].get()
        self.topic = config['mqtt']['topic'].get()
        # Generate a Client ID with the publish prefix.
        self.client_id = f'publish-{random.randint(0, 1000)}'
        self.devices: List[Device] = []
        self.mqtt_client = None

    def _get_device_data(self) -> None:
        def on_message(client, userdata, msg):
            # parse the message into a Device object and add it to the list of devices
            device = Device(
                msg.payload['IP'], msg.payload['NAME'], msg.payload['Version'])
            self.devices.append(device)

        # Create a MQTT client
        self.mqtt_client = mqtt_client.Client()

        # Set up the message callback
        self.mqtt_client.on_message = on_message

        # Connect to the MQTT broker
        try:
            self.mqtt_client.connect(self.broker, self.port, 60)
        except Exception as e:
            print(f"Error connecting to MQTT broker: {e}")
            return

        # Subscribe to the topic(s) you're interested in
        self.mqtt_client.subscribe(self.topic)

        # Enable the timeout
        timeout = 1.0  # Timeout value in seconds

        # Start the MQTT loop and specify the timeout
        self.mqtt_client.loop(timeout)

        # Wait for messages for the specified timeout duration
        start_time = time.time()
        while time.time() - start_time < timeout:
            # Continue doing other tasks if needed
            pass

        # Disconnect from the MQTT broker
        self.mqtt_client.disconnect()

    # getters and setter
    def get_devices(self) -> List[Device]:
        self._get_device_data()
        return self.devices
