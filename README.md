# Utoqa Development Control Software for Testing
This repo contains development control software for testing at AE.

There is one primary file that is used to control the fridge:

```bash
sudo python control.py [commands]
```

There are 3 options that can be used:

1. Control doors
2. Control LEDs
3. Send defacto serial string

## Controlling doors
To control the doors, the command is as follows:

```bash
sudo python control.py open [DOOR]
```

So, to open the bottom right door, you would type into a terminal window:

```bash
sudo python control.py open RD
```

To close the same door, you type:

```bash
sudo python control.py close RD
```

The door codes can be found on the spreadsheet from Fabio.

## Controlling LED lights
To control the LED lights, the same procedure is taken, with different arguments:

```bash
sudo python control.py led [DOOR] [R] [G] [B]
```

So, to change the bottom right drawer lights to red, you would type:
 ```bash
 sudo python control.py led RD 255 0 0
 ```
 
 The door codes are the same as on the spreadsheet given by Fabio.
 
 ## Using your own command
 If you need to test out a new or different command, simply do:
 ```bash
 sudo python control.py protocol [COMMAND]
 ```
 
 So, to open the bottom right door, type:
 
 ```bash
 sudo python control.py protocol Q:#RD:MTR:OP
 ```
 
 
