# HID-detection
Application de détection des HID connecté à un pc

## Program Use ##
L'application peut etre lancé en compilant et en exécutant le fichier hid_detection_console.py pour le mode en console ou le fichier hid_detection_gui.py pour le mode graphique

Pour le model graphique:
1. Les périphériques détectables sont les souris, les claviers exertenes et les joysticks 
2. Les images representant les périphériques sont grisées avec un message dessus pour dire que les périphériques ne sont pas encore connectés ou ont été déconnectées. 
3. Les informations consernant un périphéque(comme son nom, son id, son vendeur, l'id de son vendeur) serons affichées près de l'image representant le périphérique une fois que ce dernier sera connecté
4. A chaque touche du clavier, du joystick enfoncée et à chaque clic sur un boutton de la souris la touche ou le boutton sera mis en évidence sur l'image representant le périphérique.

Pour le mode console:
1. Tout type de périphérique est détectable
2. A chaque nouveau périphérique connecté un méssage sera affiché dans la console indiquant les informations sur le nouveau périphérique connecté
3. A chaque action éffectué sur le périphique(en particlier pour les claviers, souris et joysticks) un message sera affiché indiquant quelle touche à été enfoncé ou quel boutton à été enfoncé.
4. Le programme s'arrete en appuyant successivement sur les touches ctrl et c

## Notes on Building Project ##
Pour le developpement de l'application j'ai utilisé:
1. Les librairies:
	-pygame
	-pywinusb.
	-pynput (pour le mode console)
	-keyboard (pour le mode console)
Donc il faudra les installer si vous ne les avez pas.
Commande d'installation:
-pip install pygame
-pip install pywinusb
-pip install pynput
-pip install keyboard


