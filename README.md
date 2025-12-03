# Rag's macropad with 4 switches and 2 LEDs and additional LED controller/strip

This is my first blueprint project with a modest change on top of the instructions provided
I added a Neopixel_txt LED controller that can connect to additional LEDs or an LED strip for some fancy lighting. I also tried to hook up a buzzer but gave up in the interest of time

The 4 keys will function as:

key1: gives a help message on what keys2,3,4 do

key2: performs <ALT><tab> with delay b/w switching

key2: performs <CTL><tab> with delay b/w switching

key2: performs <WIN><tab> with delay b/w switching

LEDs will function as below (firmware yet to be implemented.. so, expect some surprises!) 

LED1: Lights up when board is ready for use (keeps blinking or turned off on error)

LED2: Blinks whenever a key is pressed

LED3 and above: Fancy lighting (patterns based on last key pressed) 

<img width="842" height="982" alt="rag1 macropad pcb image" src="https://github.com/user-attachments/assets/0668af9b-d83b-4c2c-a2a6-3cf5fa8e48ae" />

Here is the schematic. I played around a bit with placement to help routing easier, although kicad didnt make good use of it!! 
[myproj1 schematic drawing.pdf](https://github.com/user-attachments/files/23893459/myproj1.schematic.drawing.pdf)


<img width="1406" height="787" alt="macropad pcb - empty" src="https://github.com/user-attachments/assets/e6d528e6-6513-4f59-a913-f287180f5b4d" />
<img width="1537" height="695" alt="macropad lid" src="https://github.com/user-attachments/assets/5feaca9d-6b1f-48dd-a970-d4f1c5545bdc" />
<img width="878" height="831" alt="macropad with pcb" src="https://github.com/user-attachments/assets/a0d7f55c-518c-4111-ad1b-6eead0bf25a9" />
<img width="621" height="478" alt="image" src="https://github.com/user-attachments/assets/9c44d321-632b-455f-8fee-3c5559d41945" />
