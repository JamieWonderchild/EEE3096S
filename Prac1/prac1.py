#!/usr/bin/python3
"""
Names: <Jamie Aronson>
Student Number: <ARNJAM004>
Prac: <Prac 1>
Date: <31/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO

# Logic that you write
def main():
    global count
    GPIO.setmode(GPIO.BCM)
    pinout_list = [13,19,26] #array of pins that will be used as outputs
    pinin_list = [2,3] #array of pins that will be used as inputs
    GPIO.setup(pinout_list, GPIO.OUT,initial=GPIO.LOW) #setting the modes of the various pins and an initial output state to low
    GPIO.setup(pinin_list, GPIO.IN)
    #here we detect a button being pushed with a bounce time of 300ms
    GPIO.add_event_detect(2, GPIO.RISING,callback=button_increase,bouncetime = 300)
    GPIO.add_event_detect(3, GPIO.RISING,callback=button_decrease,bouncetime = 300)    
    while True:
        pass
        
def button_decrease(channel):
    #function responsible for decreasing count
    global count
    if count == 0:#as the buttom is clicked, count is checked to see if it is at its minimum
        count = 7
    else:
        count = count -1
    display()
    
def button_increase(channel):
    #function to increase the counter
    global count
    if count == 7:#checks to see if count is at a maximum
        count = 0
    else:
        count = count +1
    display()
    
def display():
    global count
    x= format(count, '03b')#formats an integer into a 3 bit binary number with leading 0's
    #conditional statements to turn various pins high or low
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
