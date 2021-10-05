import time
import threading

import RPi.GPIO as GPIO


class App:

    def __init__(self):
        self._animation_cancelled = True
        self._animation_speed = 1
        self._animation_speed_max = 5

    def start(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        # leds
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)

        # buttons
        def _on_button_released(channel):
            # print(f'ButtonReleased: id="{channel}"')
            animation_speed = self._animation_speed
            animation_speed += 1
            if animation_speed > self._animation_speed_max:
                animation_speed = 1
            self._animation_speed = animation_speed
            print(f'animation speed = {self._animation_speed}')

        GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(19, GPIO.RISING, callback=_on_button_released)

        # switch
        def _on_switch_toggled(channel):
            # print(f'SwitchToggled: id="{channel}"')
            self._animation_cancelled = not self._animation_cancelled
            print(f'animation running = {not self._animation_cancelled}')
            if not self._animation_cancelled:
                self._start_animation()

        GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(40, GPIO.RISING, callback=_on_switch_toggled)

        # initialize
        self._animation_cancelled = not bool(GPIO.input(40))
        if not self._animation_cancelled:
            self._start_animation()

        message = input('Press enter to quit\n\n')
        self._animation_cancelled = True
        GPIO.cleanup()

    def _start_animation(self):
        thread = threading.Thread(target=self._animate, daemon=True)
        thread.start()

    def _animate(self):
        while not self._animation_cancelled:
            speed_factor = self._animation_speed_max + 1 - self._animation_speed
            sleep_seconds = 0.1 * speed_factor

            GPIO.output(8, GPIO.HIGH)
            time.sleep(sleep_seconds)

            GPIO.output(10, GPIO.HIGH)
            time.sleep(sleep_seconds)

            GPIO.output(12, GPIO.HIGH)
            time.sleep(sleep_seconds)

            GPIO.output(8, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            time.sleep(sleep_seconds)


def main():
    app = App()
    try:
        app.start()
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
