# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 08:57:37 2024

@author: Leon-Onetype
"""


import pywinusb.hid as hid
from pynput import mouse
import keyboard  
import sys



class Device():
    """
    653876999
    Device class
    
    """
    def __init__(self, product_name, product_id, vendor_name, vendor_id, serial_number ):
        self.product_name = product_name.strip()
        self.product_id = int(product_id)
        self.vendor_name = vendor_name.strip()
        self.vendor_id = int(vendor_id)
        self.serial_number = serial_number
        
    def __eq__(self, other_device):
        
        # On a supposer que que deux devices sont égaux s'ils ont le meme id
        return  self.product_id == other_device.product_id

    
    def display(self):
        """
        Display the caracteristiqueS of a device such as vendor name, vendor id, product name ....

        Returns
        -------
        None.

        """

        print("-------------------------------------------------------------------")
        print("New HID device connected :" )
        print(f" \t- Device name : {self.product_name}")
        print(f" \t- Device id : {self.product_id}")
        print(f" \t- Serial number : {self.serial_number }")
        print(f" \t- Vendor name : {self.vendor_name}")
        print(f" \t- Vendor id : {self.vendor_id}")
        print("-------------------------------------------------------------------\n")


def remove_duplicate(iterable):
    
    new_iterable = [iterable[0]]
    
    for element in iterable:
        if element not in new_iterable:
            new_iterable.append(element)
    
    return new_iterable


def parse_devices(devices_saved):
    """
    Detect new connected devices and devices deconnected

    Parameters
    ----------
    devices_saved : list
        list of recent connected devices.

    Returns
    -------
    list of connected devices.

    """
        
    # On recupère la liste des devices connectés
    tmp_devices = hid.HidDeviceFilter().get_devices()
    
    # On converti ces devices en instances de la notre class Device
    tmp_devices = [Device(hid_device.product_name, hid_device.product_id, hid_device.vendor_name, hid_device.vendor_id, hid_device.serial_number)\
                  for hid_device in tmp_devices]
    
    tmp_devices = remove_duplicate(tmp_devices)

    # Recupération des devices qui ont été déconnectés
    deconnected_devices = [device for device in devices_saved if device not in tmp_devices]
    
    # Recupération des devices connectés
    connected_devices = [device for device in tmp_devices if device  not in  devices_saved]
    
    # Affichage des informations sur les devices détectés
    if connected_devices:
        print("\n>> HID devices found :")
        for device in connected_devices:
            device.display()
            # On actualise la liste des devices détectés
            devices_saved.append(device)
            
        print(">> Waiting for devices ... \n")
    
        
    # On notifi s'il y en a les devices déconnectés 
    if deconnected_devices:
        print("\n>> Deconnected device : ")
        for device in deconnected_devices:
            print("-------------------------------------------------------------------") 
            print(f" \t - Device {device.product_name}({device.product_id}) was deconnected")
            print("-------------------------------------------------------------------\n")
            # suppression du device dans la liste des devices connectés
            devices_saved.remove(device)

# Fonction de rappel pour gérer les événements de touches enfoncées
def on_key_press(event):
    print(f">> The key {event.name} was pressed.")

# Fonction de rappel pour gérer les événements de click       
def on_click(x, y, button, pressed):
    """

    Parameters
    ----------
    x : int
        x position of the mouse.
    y : int
        y position if the mouse.
    button : mouse.Button
        .
    pressed : bool()
        True if the button is pressed False if not.

    Returns
    -------
    None.

    """
    
    if pressed:
        print(f">> Click detected at the position ({x}, {y}) with button: {button}")

    
       
# The main function
def main():
    
    # liste qui va sauvegarder les devices détectés. 
    devices_saved = []
    
    # Créer une instance du listener pour la souris
    listener = mouse.Listener(on_click=on_click)
    
    # Démarrer le listener en arrière-plan
    listener.start()
    
    # Enregistrement de la fonction de rappel pour les événements de touches enfoncées
    keyboard.on_press(on_key_press)
    
    # Boucle principale
    continuer = True
    while (continuer):
        try:
            # Recherche et affichage des informations sur les devices
            parse_devices(devices_saved),

        except KeyboardInterrupt: 
              continuer = False
             
                      
    # On arrete d'ecouter les mouvements de la souris et du clavier
    listener.stop()
    sys.exit()
    
             
if __name__ == "__main__":
        main()
