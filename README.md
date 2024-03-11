# HID Detection
Python application
Application for detecting connected HID devices on a PC.

## Program Use ##
The application can be launched by compiling and executing the hid_detection_console.py file for console mode or the hid_detection_gui.py file for graphical mode.

For graphical mode:

Detectable devices include mice, external keyboards, and joysticks.
The images representing the devices will be grayed out with a message indicating that the devices are not yet connected or have been disconnected.
Information about a device, such as its name, ID, vendor, and vendor ID, will be displayed next to the image representing the device once it is connected.
Each key press on the keyboard, joystick, or mouse button click will highlight the corresponding key or button on the image representing the device.
For console mode:

All types of devices are detectable.
When a new device is connected, a message will be displayed in the console indicating information about the newly connected device.
For device actions (especially for keyboards, mice, and joysticks), a message will be displayed indicating which key or button has been pressed.
The program can be stopped by pressing the Ctrl and C keys simultaneously.

## Notes on Building the Project ##
To develop this application, the following libraries were used:
Libraries:
pygame
pywinusb
pynput (for console mode)
keyboard (for console mode)
Please ensure that these libraries are installed if you don't have them already. You can install them using the following commands:

- pip install pygame
- pip install pywinusb
- pip install pynput
- pip install keyboard
Make sure to have the necessary dependencies installed in order to build and run the application successfully.
