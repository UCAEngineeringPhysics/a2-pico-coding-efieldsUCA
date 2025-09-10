# switch_mode_Edward_Fields.py
# Edward Fields
# Robotics 1 // Dr. Zhang

from machine import Pin, PWM
from utime import sleep_ms

# SETUP
LED_PIN = 16
BUTTON_PIN = 15
MAX_DUTY = 50000

led_pwm = PWM(Pin(LED_PIN))
led_pwm.freq(1000)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Mode Controls
mode = 1 # fading mode
last_button_state = 1

# Variables
FADE_TIME_MS = 2000
LOOP_DELAY_MS = 10
fade_steps = FADE_TIME_MS // LOOP_DELAY_MS
fade_step_size = MAX_DUTY // fade_steps
current_duty = 0
fade_direction = 1

# LOOP
try:
    print(f"Starting in Mode {mode} (Endlessly Fading) . Press button to switch.")
    while True:
        current_button_state = button.value()
        if current_button_state == 0 and last_button_state == 1: # Button was just pressed
            if mode == 1:
                mode = 2
            else:
                mode = 1
            print(f"Switched to Mode {mode}")
        last_button_state = current_button_state
        
        # --- Mode Logic ---
        if mode == 1:
            current_duty += fade_step_size * fade_direction
            
            # Reverse direction at the top and bottom
            if current_duty >= MAX_DUTY:
                current_duty = MAX_DUTY
                fade_direction = -1
            elif current_duty <= 0:
                current_duty = 0
                fade_direction = 1
            
            led_pwm.duty_u16(current_duty)
            
        else: # Mode 2
            led_pwm.duty_u16(MAX_DUTY)
        
        # A short, consistent delay keeps the loop running smoothly
        sleep_ms(LOOP_DELAY_MS)

except KeyboardInterrupt:
    led_pwm.duty_u16(0)
    print("\nFinished.")