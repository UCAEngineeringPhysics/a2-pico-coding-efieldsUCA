# fade_in_fade_out_Edward_Fields.py
# Edward Fields
# Robotics 1 // Dr.Zhang

from machine import Pin, PWM
from utime import sleep_ms

# SETUP
LED_PIN = 16
led_pwm = PWM(Pin(LED_PIN))
led_pwm.freq(1000)

FADE_IN_TIME_MS = 2000
FADE_OUT_TIME_MS = 1000
MAX_DUTY = 65535
STEPS = 100 

# LOOP
try:
    while True:
        # Fade In (2 seconds)
        delay_per_step_in = FADE_IN_TIME_MS // STEPS
        for i in range(STEPS):
            # Calculate brightness based on how far we are in the loop
            brightness = (i * MAX_DUTY) // STEPS
            led_pwm.duty_u16(brightness)
            sleep_ms(delay_per_step_in)

        # Fade Out (1 second)
        delay_per_step_out = FADE_OUT_TIME_MS // STEPS
        for i in range(STEPS):
            # Go in reverse to calculate brightness
            brightness = MAX_DUTY - (i * MAX_DUTY) // STEPS
            led_pwm.duty_u16(brightness)
            sleep_ms(delay_per_step_out)
            
except KeyboardInterrupt:
    led_pwm.duty_u16(0)
    print("\nFinished.")
