import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Setup the GPIO mode
GPIO.setmode(GPIO.BCM)

# Setup the LED pin
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Setup the DHT sensor
DHT_SENSOR = Adafruit_DHT.DHT11  # Use DHT11 sensor (can also use DHT22)
DHT_PIN = 4  # GPIO pin connected to DHT sensor

# Temperature threshold (in Celsius)
TEMP_THRESHOLD = 25.0

try:
    while True:
        # Read the temperature and humidity from the sensor
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature}C  Humidity: {humidity}%')
            
            # Check if the temperature is below the threshold
            if temperature < TEMP_THRESHOLD:
                print("Temperature is below threshold. LED OFF.")
                GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED
            else:
                GPIO.output(LED_PIN, GPIO.LOW)  # Keep LED OFF if not threshold
            
        else:
            print('Failed to get reading. Try again!')
        
        time.sleep(2)  # Wait for 2 seconds before reading again

except KeyboardInterrupt:
    print("Exiting Program")

finally:
    GPIO.cleanup()  # Cleanup GPIO pins when done



dht above threshold:
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Setup the GPIO mode
GPIO.setmode(GPIO.BCM)

# Setup the LED pin
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Setup the DHT sensor
DHT_SENSOR = Adafruit_DHT.DHT11  # Use DHT11 sensor (can also use DHT22)
DHT_PIN = 4  # GPIO pin connected to DHT sensor

# Temperature threshold (in Celsius)
TEMP_THRESHOLD = 25.0

try:
    while True:
        # Read the temperature and humidity from the sensor
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature}C  Humidity: {humidity}%')
            
            # Check if the temperature is above the threshold
            if temperature > TEMP_THRESHOLD:
                print("Temperature is above threshold. LED ON.")
                GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
            else:
                GPIO.output(LED_PIN, GPIO.LOW)  # Keep LED OFF if below threshold
            
        else:
            print('Failed to get reading. Try again!')
        
        time.sleep(2)  # Wait for 2 seconds before reading again

except KeyboardInterrupt:
    print("Exiting Program")

finally:
    GPIO.cleanup()  # Cleanup GPIO pins when done
