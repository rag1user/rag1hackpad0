# SinnerPad
It's a four key macropad... nothing too special for my first YSWS project. I didn't add anything because I wasn't too sure what to add. 

## Features
- Four key macros meant for my digital art (i.e undo, redo, copy, paste)
- Two layer assembly
- A ring for a keychain so I can put it on my backpack (or hackpack... heh... get it)
- Uh... cool sounds? I dunno LOL
- I made this in a day
- What else do you want me to say

## CAD
The entire macropad is held together with four M3 screws. The PCB itself is going to be placed inside the slot and then probably glued.

It has two separate pieces that will be 3d printed.

<img width="526" height="435" alt="image" src="https://github.com/user-attachments/assets/8a827669-ca85-42c2-9bb9-e195dfe7d782" />
Made in OnShape


## PCB
Here is my PCB, made in KiCAD.

Schematic:

<img width="904" height="638" alt="image" src="https://github.com/user-attachments/assets/225da1f9-5ef2-4bb1-b54d-8dab875dd9dc" />

PCB:

<img width="796" height="588" alt="image" src="https://github.com/user-attachments/assets/b4647599-3ab0-4172-99ea-077f1a3fc203" />

I used Cherry MX Basics

## Firmware Overview
This hackpad uses KMK firmware for everything. I decided to use KMK because I have no idea how to read the QMK documentation tbh (sobbing)
- The four keys apply in this order:
- Undo (CTRL + Z)
- Redo (CTRL + Y)
- Copy (CTRL + C)
- Paste (CTRL + V)

I will definite reiterate on this design later on (or make a new macropad, because now I know how to actually do it)

## Bill of Materials
- 4x LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm
- 4x Cherry_MX switches
- 4x PBT Keycaps
- 4x M3 6mm Screws
- 4x M3 6mm Nuts
- 1x XIAO RP2040
- 1x Case (2 3D printed parts)

