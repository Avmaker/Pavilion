import board
import time
import displayio
import terminalio
import digitalio
from adafruit_display_text import label
import adafruit_ili9341
import adafruit_scd4x
from adafruit_lc709203f import LC709203F, PackSize
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import pwmio
from adafruit_motor import servo
import neopixel

#FOR NEOPIXEL
pixel = neopixel.NeoPixel(board.A4, 5)
pixel.brightness = 0.3


relay = digitalio.DigitalInOut(board.A3)
relay.direction = digitalio.Direction.OUTPUT

# create a PWMOut object on Pin A1.
pwm = pwmio.PWMOut(board.A1, frequency=35)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

kit = MotorKit(i2c=board.I2C())

displayio.release_displays()

spi = board.SPI()
tft_cs = board.D9
tft_dc = board.D10

i2c = board.I2C()

battery_monitor = LC709203F(board.I2C())

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D6)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

scd4x = adafruit_scd4x.SCD4X(i2c)
print("Serial number:", [hex(i) for i in scd4x.serial_number])

scd4x.start_periodic_measurement()
print("Waiting for first measurement....")

while True:
    if scd4x.data_ready:
        print("CO2: %d ppm" % scd4x.CO2)
        print("Temperature: %0.1f *C" % scd4x.temperature)
        print("Humidity: %0.1f %%" % scd4x.relative_humidity)
        print("Battery Percent: {:.2f} %".format(battery_monitor.cell_percent))
        print()


# Make the display context
        splash = displayio.Group()
        display.show(splash)

 # Draw a label
        text = "PAVILION ENVIRONMENT"
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, scale =2, x=50, y=10)
        splash.append(text_area)

        text = "CO2: {:.1f} ppm ".format(scd4x.CO2)
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF,scale =2, x=20, y=50)
        splash.append(text_area)

        text = "Temperature: {:.1f} C".format(scd4x.temperature)
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, scale =2, x=20, y=100)
        splash.append(text_area)

        text = "Humidity: {:.1f} %".format(scd4x.relative_humidity)
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, scale =2, x=20, y=150)
        splash.append(text_area)

        text = "Battery %: {:.2f} %".format(battery_monitor.cell_percent)
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, scale =2, x=20, y=200)
        splash.append(text_area)

        display.show(splash)

        time.sleep(5)

        # Co2 is less than 1000 COLOUR GREEN
        if scd4x.CO2 <1000:
            pixel.fill((0, 255, 0))
            time.sleep(0.5)

        # Co2 is less than 2000 COLOUR AMBER
        elif scd4x.CO2 <= 2000:
            pixel.fill((25, 0, 51))
            time.sleep(0.5)

        # Co2 is greater than 5000 COLOUR RED
        elif scd4x.CO2 <= 5000 :
            for i in range(4):
                pixel.fill((255, 0, 0))
                time.sleep(0.2)
                pixel.fill((0, 0, 0))
                time.sleep(0.2)
                pixel.fill((255, 0, 0))




        # Triggers an action if the Co2 Level is greater than 100
        if scd4x.CO2 >1000:
            relay.value = True
            time.sleep(1)

            for j in range(1):

                for i in range(25):
            #left stepeper 1
                    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                    time.sleep(0.5)

                for i in range(27):
            #right stepper 1
                    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                    time.sleep(0.5)

                for i in range(15):
            #left stepper 2
                    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                    time.sleep(0.5)

                for i in range(15):
            #right stepper 2
                    kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                    time.sleep(0.5)

            kit.stepper2.release()

            my_servo.throttle = -1.0
            time.sleep(1.5)

            my_servo.throttle = 0.0
            time.sleep(1.5)

            my_servo.throttle = 0.9
            time.sleep(1.5)

            my_servo.throttle = 0.0
            time.sleep(2.0)

        else:
            relay.value = False





