#vcc to pin 1
#data  to pin 36
#gnd to pin 6

import Adafruit_DHT

# Set the sensor type and the GPIO pin number
sensor = Adafruit_DHT.DHT22
pin = 16  # GPIO pin where the DATA pin of the DHT11 is connected

try:
    while True:
        # Read humidity and temperature from the DHT11
        humidity, temperature = Adafruit_DHT.read(sensor, pin)

        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature:.1f}      C, Humidity: {humidity:.>
        else:
            print("Failed to retrieve data from the sensor")
except KeyboardInterrupt:
    print("Exiting program")
