# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 05:37:33 2024

@author: Leon-Onetype
"""

import pygame
import pywinusb.hid as hid

# Taille de la fenetre
WIN_WIDTH   =  900
WIN_HEIGHT  = 720

# Les couleurs
BACKGROUND_COLOR   = (255, 255, 255)
WHITE_COLOR        = (255, 255, 255)
BLACK_COLOR        = (0,   0,   0)
GREEN_COLOR        = (0,   255, 0)
BLUE_COLOR         = (0,   0,   180)
RED_COLOR          = (255, 50,   50)

# Les positions et les dimentions des object sur l'écran
MOUSE_DEST         = (25, 470)
IMG_MOUSE_SIZE     = (108, 209)

KEYBOARD_DEST      = (10, 0)
IMG_KEYBOARD_SIZE  = (864, 324)

JOYSTICK_FRONT_DEST= (400, 475)
JOYSTICK_BACK_DEST=  (400 , 360)
IMG_JOYSTICK_FRONT_SIZE  = (320, 250)
IMG_JOYSTICK_BACK_SIZE  = (320, 111)

FPS = 30


class Device():
    """
    
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
              
def remove_duplicate(iterable):
    """
    
    Returns a new iterable  with non duplicated values
    """
    
    new_iterable = [iterable[0]]
    
    for element in iterable:
        if element not in new_iterable:
            new_iterable.append(element)
    
    return new_iterable

def parse_devices():
    """
    Detect new connected devices and devices deconnected

    Returns
    -------
     booleans values that determinate if keyboards, mouses and joysticks is connected or not

    """
        
    # On recupère la liste des devices connectés
    tmp_devices = hid.HidDeviceFilter().get_devices()
    
    # On converti ces devices en instances de la notre class Device
    tmp_devices = [Device(hid_device.product_name, hid_device.product_id, hid_device.vendor_name, hid_device.vendor_id, hid_device.serial_number)\
                  for hid_device in tmp_devices]
    
    tmp_devices = remove_duplicate(tmp_devices)
    
    return tmp_devices

def display_text(text, pos, screen, color = WHITE_COLOR, font_size=12, center= False):
    """
    Display text on the Surface object passed as parameter
    """
    # text setting
    font_obj = pygame.font.Font('freesansbold.ttf', font_size)
    text_surface = font_obj.render(text, True, BLACK_COLOR, color)
    text_rect = text_surface.get_rect()
    position = pos
    if center == True:
        position = pos[0] - text_rect.width/2,  pos[1] - text_rect.height/2
    text_rect = pygame.Rect(*position, text_rect.width, text_rect.height)
    screen.blit(text_surface, position)

def display_device_informations(device, pos, screen, decalage):
    pos = pos[0], pos[1] + decalage
    display_text(f"- Name : {device.product_name[:50]}", pos, screen)
    pos = pos[0], pos[1] + decalage
    display_text(f"- id : {device.product_id}", pos, screen)
    pos = pos[0], pos[1] + decalage
    display_text(f"- Serial number : {device.serial_number }", pos, screen)
    pos = pos[0], pos[1] + decalage
    display_text(f"- Vendor name : {device.vendor_name}", pos, screen)
    pos = pos[0], pos[1] + decalage
    display_text(f"- Vendor id : {device.vendor_id}", pos, screen)
    
def display_devices_informations(devices, screen):
    """

    Parameters
    ----------
    devices : list
        list of devices(instances of the Device Classe).
    screen : 

    Returns
    -------
    keyboard_connected : bool
        His value will be True if a keyboard is connected False if not.
    mouse_connected : bool
        His value will be True if a mouse is connected False if not..
    joystick_connected : bool
        His value will be True if a joystick is connected False if not..

    """
    # Affichage des informations sur les devices détectés
    pos = None
    keyboard_connected = False
    mouse_connected = False
    joystick_connected = False
    num_keyboard = 0
    num_mouse = 0
    num_joystick = 0
    
    # Si on trouve au moins un périphérique
    if devices:
        
        # Le décalage en ordonnées ou en abscices quand on va afficher les informations sur le périphérique
        decalage=15
        
        for i, device in enumerate(devices):
            
            # Gestion selon le type de périphérique
            
            # Le cas d'une clavier
            if "keyboard" in device.product_name.lower(): 
                pos = KEYBOARD_DEST[0] + num_keyboard*25 , IMG_KEYBOARD_SIZE[1] + 10 
                display_text(">> New keyboard connected! ", pos, screen, color=GREEN_COLOR)
                display_device_informations(device, pos, screen, decalage)
                keyboard_connected = True
                num_keyboard += 1
            
            # Le cas d'une souris
            elif "mouse" in device.product_name.lower(): 
                pos = MOUSE_DEST[0] + IMG_MOUSE_SIZE[0], MOUSE_DEST[1] + num_mouse*decalage
                display_text(">> New mouse connected! ", pos, screen, color=GREEN_COLOR)
                display_device_informations(device, pos, screen, decalage)
                mouse_connected = True
                num_mouse += 1
                
            # Le  d'une manette de jeu
            elif "joystick" in device.product_name.lower(): 
                pos = JOYSTICK_BACK_DEST[0] + IMG_JOYSTICK_BACK_SIZE[0], JOYSTICK_BACK_DEST[1] + num_joystick*decalage
                display_text(">> New joystick connected! ", pos, screen, color=GREEN_COLOR)
                display_device_informations(device, pos, screen, decalage)
                joystick_connected = True
                num_joystick += 1
                
            else:
                pass
    
    # Dans le cas contraire.
    if keyboard_connected == False:
        pos = KEYBOARD_DEST[0] + IMG_KEYBOARD_SIZE[0]/2, KEYBOARD_DEST[1] + IMG_KEYBOARD_SIZE[1]/2
        display_text(">> No keyboad connected", pos, screen, RED_COLOR, center=True)
        
    if mouse_connected == False:
        pos = MOUSE_DEST[0] + IMG_MOUSE_SIZE[0]/2, MOUSE_DEST[1] + IMG_MOUSE_SIZE[1]/2
        display_text(">> No mouse connected", pos, screen, RED_COLOR, center=True)
        
    if joystick_connected == False:
        pos = JOYSTICK_BACK_DEST[0] + IMG_JOYSTICK_BACK_SIZE[0]/2, JOYSTICK_BACK_DEST[1]\
                            + (IMG_JOYSTICK_FRONT_SIZE[1] + IMG_JOYSTICK_BACK_SIZE[1])/2
        display_text(">> No joystick connected", pos, screen, RED_COLOR, center=True)
    
    # Actualisation de la surface
    pygame.display.update()
        
    return keyboard_connected,  mouse_connected, joystick_connected     

def on_key_press(event, screen):
    """
    
    function to call when a key is pressed
    Parameters
    ----------
    event : pygame.event.Event
    screen : pygame.surface.Surface

    Returns
    -------
    None.

    """
    image_key = None
    
    try:
        texte = "clavier_images/" + '_'.join(pygame.key.name(event.key).lower().split(' ')) + ".png"
        image_key = pygame.image.load(texte).convert_alpha()
    except FileNotFoundError: 
        # On regarde d'abord si c'est une touche particulière
        particuliers =  {':':"deux_points", '\\':"antislash",'[/]':"slash", '[*]':"etoile", '?':"", '<':"inf_sup", '>':"inf_sup"  }
        if pygame.key.name(event.key) in particuliers.keys():
             texte = "clavier_images/" + particuliers[pygame.key.name(event.key)] + ".png"   
             image_key = pygame.image.load(texte).convert_alpha()
        
        # Sinon, on ne fais rien
        else:
            image_key = pygame.image.load("clavier_images/connected.png").convert_alpha()
        
    screen.blit(image_key, KEYBOARD_DEST)
    
    pygame.display.update()
      
def on_click(event, screen):
    """
    
    function to call when a key is pressed
    Parameters
    ----------
    event : pygame.event.Event
    screen : pygame.surface.Surface

    Returns
    -------
    None.

    """
    
    path = "souris_images/connected.png"

    if event.button == 1:
        path = "souris_images/Button.left.png"
    elif event.button == 2:
        path = "souris_images/Button.middle.png"
    elif event.button == 3:
        path = "souris_images/Button.right.png"

    image_key = pygame.image.load(path).convert_alpha()
    screen.blit(image_key, MOUSE_DEST)
    pygame.display.update()
    
def on_joystick_pres(event, screen):
   
    button = event.button
    
    try:
        image = pygame.image.load(f"joystick_images/{button}.png").convert_alpha()
        if button in [4, 5, 6, 7]:
            screen.blit(image, JOYSTICK_BACK_DEST)
        else: 
            screen.blit(image, JOYSTICK_FRONT_DEST)
    except:
        pass
    
    pygame.display.update()

def on_joystick_motion(event, screen):
    axis = event.axis
    value = event.value
    path = "joystick_images/connected_front.png"
    
    if axis == 0:
        if value <= -1.0:
            path = "joystick_images/l3_gauche.png"
        elif value >=1.0:
            path = "joystick_images/l3_droite.png"
            
    elif axis == 1:
        if value <= -1.0:
            path = "joystick_images/l3_haut.png"
        elif value >=1.0:
            path = "joystick_images/l3_bas.png"
            
    elif axis == 2:
        if value <= -1.0:
            path = "joystick_images/r3_gauche.png"
        elif value >=1.0:
            path = "joystick_images/r3_droite.png"
            
    elif axis == 3:
        if value <= -1.0:
            path = "joystick_images/r3_haut.png"
        elif value >=1.0:
            path = "joystick_images/r3_bas.png"
        
    image = pygame.image.load(path).convert_alpha()
    screen.blit(image, JOYSTICK_FRONT_DEST)
    

def main():
    # Initialisation du module pygame
    pygame.init()
    
    # Création de la fénètre et définition du titre
    screen = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Hid detection")
    screen.fill(BACKGROUND_COLOR) 
    # Icone
    icon = pygame.image.load('icone.png')
    pygame.display.set_icon(icon)
    
    # affichage des images de base
    clavier = pygame.image.load("clavier_images/deconnected.png").convert_alpha()
    screen.blit(clavier, KEYBOARD_DEST)

    image = pygame.image.load("souris_images/deconnected.png").convert_alpha()
    screen.blit(image, MOUSE_DEST)
    
    image_front = pygame.image.load("joystick_images/deconnected_front.png").convert_alpha()
    image_back = pygame.image.load("joystick_images/deconnected_back.png").convert_alpha()
    screen.blit(image_front, JOYSTICK_FRONT_DEST)
    # On la met juste à coté de l'image front
    screen.blit(image_back, JOYSTICK_BACK_DEST)
    
    pygame.display.update()
    
    # Quelques variables
    connected_devices = []
    clock = pygame.time.Clock()  # pour la gestion du temps dans la boucle principale
    running = True
    keyboard_connected = False
    mouse_connected = False
    joystick_connected = False
    path_1 = ""
    path_2 = ""
    
    # Boucle principale
    while running:
        
        event = pygame.event.poll()
        
        # On éfface l'écran
        screen.fill(BACKGROUND_COLOR)
        
        # Ecriture sur l'ecran
        # Gestion du clavier
        if keyboard_connected:
            path_1 = "clavier_images/connected.png"
        else:
            path_1 = "clavier_images/deconnected.png"
            
        clavier = pygame.image.load(path_1).convert_alpha()
        screen.blit(clavier, KEYBOARD_DEST)
        
        # Gestion de la souris
        if mouse_connected:
            path_1 = "souris_images/connected.png"
        else:
            path_1 = "souris_images/deconnected.png"
        image = pygame.image.load(path_1).convert_alpha()
        screen.blit(image, MOUSE_DEST)
        
        # Gestion du joystick
        if joystick_connected:
            # Initialisation du joystick
            # Le joystick à besion d'etre initialiser avec la sdl. On le met dans un try afin de prévenir le cas ou il n'y
            # aurais aucun joystick connecté car ci c'est le cas l'initialisation renverait une erreur.
            try:
                joystick = pygame.joystick.Joystick(0)
                joystick.init()
                path_1 = "joystick_images/connected_front.png"
                path_2 = "joystick_images/connected_back.png"
            except:
                path_1 = "joystick_images/deconnected_front.png"
                path_2 = "joystick_images/deconnected_back.png"
        else:
            path_1 = "joystick_images/deconnected_front.png"
            path_2 = "joystick_images/deconnected_back.png"
        image_front = pygame.image.load(path_1).convert_alpha()
        image_back = pygame.image.load(path_2).convert_alpha()
        screen.blit(image_front, JOYSTICK_FRONT_DEST)
        screen.blit(image_back, JOYSTICK_BACK_DEST)
    
        # Recherche et affichage des informations sur les devices
        connected_devices = parse_devices()
        keyboard_connected,mouse_connected, joystick_connected = display_devices_informations(connected_devices, screen)
        
        # Gérer les événements pygame
        if event.type == pygame.KEYDOWN:
            on_key_press(event, screen)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_click(event, screen)
            
        # Gestion des événements de joystick
        elif event.type == pygame.JOYAXISMOTION:
            # Mouvement de l'axe du joystick
            on_joystick_motion(event, screen)

        elif event.type == pygame.JOYBUTTONDOWN:
            # Appui sur un bouton du joystick
            on_joystick_pres(event, screen)
        
        elif event.type == pygame.QUIT:
           running = False
        
        # on met à jour l'écran
        pygame.display.update()
             
        clock.tick(FPS)
    
    pygame.quit()            
                
if __name__ == "__main__":
    main()