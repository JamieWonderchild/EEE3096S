#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <names>
Student Number: <studnum>
Prac: <Prac Num>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO

# Logic that you write
def main():
    global count
    GPIO.setmode(GPIO.BCM)
    pinout_list = [13,19,26]
    pinin_list = [2,3]
    GPIO.setup(pinout_list, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(pinin_list, GPIO.IN)
    GPIO.add_event_detect(2, GPIO.RISING,callback=button_increase,bouncetime = 300)
    GPIO.add_event_detect(3, GPIO.RISING,callback=button_decrease,bouncetime = 300)    
    while True:
        pass
        
def button_decrease(channel):
    global count
    if count == 0:
        count = 7
    else:
        count = count -1
    display()
    
def button_increase(channel):
    global count
    if count == 7:
        count = 0
    else:
        count = count +1
    display()
    
def display():
    global count
    print(count)
    x= format(count, '03b')
    if x[2:3] == '1':
        GPIO.output(26, GPIO.HIGH)
    else:
        GPIO.output(26, GPIO.LOW)
    if x[1:2] == '1':
        GPIO.output(19, GPIO.HIGH)
    else:
        GPIO.output(19, GPIO.LOW)
    if x[0:1] == '1':
        GPIO.output(13, GPIO.HIGH)
    else:
        GPIO.output(13, GPIO.LOW)    
    
        
    


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    count = 0
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
