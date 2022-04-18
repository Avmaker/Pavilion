#adapted existing adafuit iot code to this project
import time
import board
import digitalio
from adafruit_lc709203f import LC709203F, PackSize
import socketpool
import adafruit_requests
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError
import adafruit_scd4x
import wifi
import ssl
import alarm

try:
    from secrets import secrets
except ImportError:
    print("WiFi and Adafruit IO credentials are kept in secrets.py, please add them there!")
    raise

# Duration of sleep in seconds. Default is 600 seconds (10 minutes).
# Feather will sleep for this duration between sensor readings / sending data to AdafruitIO
sleep_duration = 10

# Update to match the mAh of your battery for more accurate readings.
# Can be MAH100, MAH200, MAH400, MAH500, MAH1000, MAH2000, MAH3000.
# Choose the closest match. Include "PackSize." before it, as shown.
battery_pack_size = PackSize.MAH500

# Setup the little red LED
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()


# Pull the I2C power pin low
i2c_power = digitalio.DigitalInOut(board.I2C_POWER_INVERTED)
i2c_power.switch_to_output()
i2c_power.value = False

# Create sensor objects, using the board's default I2C bus.
i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
battery_monitor = LC709203F(board.I2C())


scd4x.start_periodic_measurement()
print("Waiting for first measurement....")

while True:
    if scd4x.data_ready:
        #print("CO2: %d ppm" % scd4x.CO2)
        #print("Temperature: %0.0f *C" % scd4x.temperature)
        #print("Humidity: %0.0f %%" % scd4x.relative_humidity)
        #print("Battery Percent: {:.0f} %".format(battery_monitor.cell_percent))
        #print()

    # Collect the sensor data values and format the data
        CO2 ="{:0} ppm ".format(scd4x.CO2)
        temperature = "{:.0f}".format(scd4x.temperature)
        humidity = "{:.0f}".format(scd4x.relative_humidity)
        battery_percent = "{:.0f}".format(battery_monitor.cell_percent)

    def go_to_sleep(sleep_period):
# Create a an alarm that will trigger sleep_period number of seconds from now.
        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + sleep_period)
# Exit and deep sleep until the alarm wakes us.
        alarm.exit_and_deep_sleep_until_alarms(time_alarm)

# Fetch the feed of the provided name. If the feed does not exist, create it.
    def setup_feed(feed_name):
        try:
# Get the feed of provided feed_name from Adafruit IO
            return io.get_feed(feed_name)
        except AdafruitIO_RequestError:
# If no feed of that name exists, create it
            return io.create_new_feed(feed_name)

# Send the data. Requires a feed name and a value to send.
    def send_io_data(feed, value):
        return io.send_data(feed["key"], value)

# Wi-Fi connections can have issues! This ensures the code will continue to run.
    try:
    # Connect to Wi-Fi
        wifi.radio.connect(secrets["ssid"], secrets["password"])
        print("Connected to {}!".format(secrets["ssid"]))
        print("IP:", wifi.radio.ipv4_address)

        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())

# Wi-Fi connectivity fails with error messages, not specific errors, so this except is broad.
    except Exception as e:  # pylint: disable=broad-except
        print(e)
        go_to_sleep(5)

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
    aio_username = secrets["aio_username"]
    aio_key = secrets["aio_key"]

# Initialize an Adafruit IO HTTP API object
    io = IO_HTTP(aio_username, aio_key, requests)

# Turn on the LED to indicate data is being sent.
    led.value = True
# Print data values to the serial console. Not necessary for Adafruit IO.
    print("CO2: %d ppm" % scd4x.CO2)
    print("Temperature: %0.0f*C" % scd4x.temperature)
    print("Humidity: %0.0f %%" % scd4x.relative_humidity)
    print("Battery Percent: {:.0f} %".format(battery_monitor.cell_percent))
    print()

# Adafruit IO sending can run into issues if the network fails!
# This ensures the code will continue to run.
    try:
        print("Sending data to AdafruitIO...")
        # Send data to Adafruit IO
        send_io_data(setup_feed("c"), scd4x.CO2)
        send_io_data(setup_feed("t"), scd4x.temperature)
        send_io_data(setup_feed("h"), scd4x.relative_humidity)
        send_io_data(setup_feed("b"), battery_monitor.cell_percent)
        print("Data sent!")
        # Turn off the LED to indicate data sending is complete.
        led.value = False



# Adafruit IO can fail with multiple errors depending on the situation, so this except is broad.
    except Exception as e:  # pylint: disable=broad-except
        print(e)
    go_to_sleep(5)

go_to_sleep(sleep_duration)
