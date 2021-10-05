import time

import RPi.GPIO as GPIO


def loop():
    print('setup')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    try:
        while True:
            if GPIO.input(10) == GPIO.HIGH:
                print('Button was pushed!')
    except KeyboardInterrupt:
        print()
        print('exiting')
        print('cleanup')
        GPIO.cleanup()
        exit(-1)


def event():
    def button_callback1(channel):
        print(f'ButtonReleased - 1')

    def button_callback2(channel):
        print(f'ButtonReleased - 2')

    print('setup')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(8, GPIO.RISING, callback=button_callback1)

    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback2)

    message = input('Press enter to quit\n\n')

    print('cleanup')
    GPIO.cleanup()


def main():
    event()


if __name__ == '__main__':
    main()
