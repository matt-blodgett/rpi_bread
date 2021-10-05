import time

import RPi.GPIO as GPIO


def main():
    print('setup')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)

    for _ in range(10):
        print('led on')
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.25)

        print('led off')
        GPIO.output(12, GPIO.LOW)
        time.sleep(0.25)

    print('cleanup')
    GPIO.cleanup()


if __name__ == '__main__':
    main()
