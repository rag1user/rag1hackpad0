# Rag's macropad with 4 switches and 2 LEDs and additional LED controller/strip

This is my first blueprint project. I started out with a just modest change (to add a Neopixel_txt) on top of the instructions provided, but revised it based on feedback
Here is what I have in revision2:
1. The macropad has 4 keys similar to most other starter macropad projects
2. In addition, the macropad also has a SW coded switch (Surface mount SH-7010) that can be used to do additional controlls such as scrolling, volume up/down, screen brigntness up/down
3. I also added a low-end SHT1x temperature and humidity sensor out of curiosity (I want to play with more sensor projects in future and can't resist putting one right away although it makes little sense to have a sensor in a macropad/ hackpad)

The 4 keys will function as:

key1: gives a help message on what keys2,3,4 do

key2: performs \<ALT\>\<tab\> with delay b/w switching

key2: performs \<CTL\>\<tab\> with delay b/w switching

key2: performs \<WIN\>\<tab\> with delay b/w switching

Rotary key will be used for scrolling, volume controll and screen brigntness control functions (activated by  keys2-4) (Firmware for this is pending update)

LED1: Lights up when board is ready for use (keeps blinking or turned off on error)

LED2: Blinks whenever a key is pressed

SHT1x sensor: Provides temperature and humidity measurement (no display; will have to extract this via RP2040)

# Finished product (minus switches):
<img width="890" height="653" alt="image" src="https://github.com/user-attachments/assets/b16feeb9-c675-4e62-9e25-6d9580252f78" />

# PCB layout
<img width="921" height="958" alt="image" src="https://github.com/user-attachments/assets/d3ae596d-8f6f-4ee3-af2c-8414e7ac42c9" />

# Schematic
<img width="1218" height="832" alt="image" src="https://github.com/user-attachments/assets/7daf9c94-02c8-4ee0-8c8d-5ddb2233330d" />



