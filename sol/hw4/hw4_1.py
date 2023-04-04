import RPi.GPIO as GPIO
import time

class LED:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, True)

    def off(self):
        GPIO.output(self.pin, False)

    def blink(self, times, duration):
        for i in range(times):
            self.on()
            time.sleep(duration)
            self.off()
            time.sleep(duration)


# Define the menu
menu = {
    1: ("LED 18", 18),
    2: ("LED 23", 23),
    3: ("LED 24", 24)
}

commands = ["on", "off", "blink", "exit"]

# Show the menu
print("Select an LED to operate:")
for key, value in menu.items():
    print(f"{key}: {value[0]}")
while True:
    choice = input("Enter your choice :").lower()
    if choice.isdigit() and int(choice) in menu:
        c = int(choice)
        led = LED(menu[c][1])
        print("input a command in ", commands)
        command = input("Enter your command :").lower()
        if command == "on":
            led.on()
            print(menu[c][0], " is opened.")
        elif command == "off":
            led.off()
            print(menu[c][0], " is closed.")
        elif command == "blink":
            led.blink(5, 0.5)
        elif command == "exit":
            break
        else:
            print("Invalid command")
    else:
        print("Invalid choice. Please try again.")

GPIO.cleanup()
