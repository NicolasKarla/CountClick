from pynput import mouse

# Variable to store the click count
click_count = 0

# Function executed whenever a click occurs
def OnClick(x, y, button, pressed):
    global click_count
    if button == mouse.Button.left and pressed:
        click_count += 1
        print(f"Left click detected. Total clicks: {click_count}")

# Start the listener for mouse clicks
mouse.Listener(on_click=OnClick).start()

# Keep the program running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program terminated. Total clicks recorded:", click_count)
