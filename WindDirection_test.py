import time
from WindDirection import WindDirectionDevice
from DeviceManager import DeviceManager

def test_direction():
    dm = DeviceManager()
    dm.add("wind_direction", WindDirectionDevice(529516, 0))
    dm.waitUntilAllReady()
    while True:
        print(dm.get_event())
        time.sleep(1)

test_direction()