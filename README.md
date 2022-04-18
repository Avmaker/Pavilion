# The Air Quality Pop-Up Pavilion
<img src= "Images/PavilionCover.JPG" width=800>

### Table of Contents

- [Description](#description)
- [Assembling the Pavilion](#assembling-the-pavilion)
- [Wiring the Pavilion](#wiring-the-pavilion)
- [Coding the Pavilion](#coding-the-pavilion)
- [Visualising data with Adafruit IO](#visualising-data-with-adafruit-io)
- [Tuturials used](#tutorial-used)
- [Components](#components)
- [Author Info](#author-info)

## Description
Since the pandemic, social distancing along with the need for additional space and appropriate ventilation has become hugely important. Because of this, I want to also explore the concept of a POP-UP Pavilion - A pavilion that could be installed in different locations to provide space & healthy indoor air quality solutions where needed. There is a range of settings that could benefit from this, including classrooms, maker spaces & eating areas in the hospitality sector, to name just a few. I want to develop and refine a scaled-down fully working model of this pavilion concept and ultimately create a workshop based on it that will enable me to deliver hands-on sessions to other young people - giving them the opportunity to explore how spaces can monitor & react to internal air quality in order to improve the experience of the users.

The pavilion uses an internal sensor to monitor & then trigger various reactions to the co2 levels from inside. The reactions include opening & closing motorised shutter walls, an automatic sliding skylight, a ventilation fan & colour coded co2 level warning lights. I have used stepper motors & servos to generate the movement, and an Adafruit ESP 32-S2 as the brain stacked with a TFT screen to display the air quality data from the wall of the pavilion. The data is also visualised via IoT on Adafruit IO

## Assembling the Pavilion

cf pdf file in Assembling Instruction folde
and Youtube assembly link video tutorial: 
> XXX

[Back To The Top](#the-air-quality-pop-up-pavilion)

## Wiring the Pavilion

> The Motors
<img src= "Images/wiringmotors.png" width=800>

>The Electronic Components
<img src= "Images/Wiringcomponents.png" width=800>

## Coding the Pavilion

I coded the pavilion using Circuit Python to code the stepper motors, the servos, the Neopixels, the fan, the Co2 sensor and the TFT screen

cf pdf file in Assembling Instruction folder
and Youtube assembly link video tutorial: 
> XXX

## Visualising data with Adafruit IO
I also used CircuitPython to code the visualisation of the date on Adafruit IO.

## Components 
**What you will need**
- Adafruit ESP32-S2 Feather with BME280 Sensor
- Adafruit Stepper Motor Featherwing
- Adafruit TFT FeatherWing - 2.4" 320x240. Touchscreen For All Feathers
- Adafruit SCD 40 - True CO2, Temperature and Humidity Sensor
- Mini Stepper Motor - 200 Steps - 20x30mm NEMA-8 Size (2 off)
- Micro 360 Degree Continuous Rotation Servo FS90R
- Linear actuator
- 5V DC, Axial Fan, 40 x 40 x 10mm, 7CFM
- Relay - 5V
- Kitronik ZIP Stick - 5 ZIP LED
- 4mm Economy Birch Laser Plywood - 600mm x 400mm
- sheet Clear Perspex Sheet (Cast) 4mm x 600mm x 400mm Lipo Battery - 3.7 v; 500mAh
- AA Battery pack; 3x 1.5V
- Jumper wires
- USB C to B Cable
- M3 button head screws
- M3 hex nuts

[Back To The Top](#the-air-quality-pop-up-pavilion)

## Tutorials used

Adafruit ESP32-32 Feather:
- https://learn.adafruit.com/adafruit-esp32-s2-feather

Stepper motor Featherwing:

- https://learn.adafruit.com/adafruit-stepper-dc-motor-featherwing

- https://thepihut.com/products/mini-stepper-motor-200-steps-20x30mm-nema-8-size

Co2 sensor Adafruit SCD40:

- https://learn.adafruit.com/adafruit-scd-40-and-scd-41?view=all

Adafruit IO set up

- https://learn.adafruit.com/welcome-to-adafruit-io/getting-started-with-adafruit-io

- https://learn.adafruit.com/adafruit-io-basics-feeds

- https://learn.adafruit.com/adafruit-io-basics-dashboards

## Author Info

- Twitter - [@girlsintocoding](https://twitter.com/girlsintocoding)
- Website - [Girls Into Coding](https://girlsintocoding.com)

[Back To The Top](#the-air-quality-pop-up-pavilion)
