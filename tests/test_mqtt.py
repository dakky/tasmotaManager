from unittest import mock
import pytest
from mqtt.mqtt import Mqtt
from models.device import Device

@pytest.fixture
def mqtt_client():
    client = Mqtt()
    yield client

def test_mqtt_message_handling(mqtt_client):
    # Create mock messages
    mock_messages = [
        {
            'payload': {
                'IP': '192.168.0.1',
                'NAME': 'Device 1',
                'Version': '1.0'
            }
        },
        {
            'payload': {
                'IP': '192.168.0.2',
                'NAME': 'Device 2',
                'Version': '2.0'
            }
        }
    ]

    # Patch the on_message method with a mock function
    with mock.patch.object(Mqtt, 'on_message') as mock_on_message:
        # Simulate receiving the mock messages
        for mock_message in mock_messages:
            mqtt_client.on_message(None, None, mock_message)

    # Verify the devices list has the expected content
    expected_devices = [
        Device('192.168.0.1', 'Device 1', '1.0'),
        Device('192.168.0.2', 'Device 2', '2.0')
    ]
    assert mqtt_client.devices == expected_devices
