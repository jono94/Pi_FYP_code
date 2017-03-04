FILES THAT MUST BE CHANGED:
 - sendImages.py
     - need to update ip, user, password of the computer you are sending the images to.
     - change the file path to which the images are placed on the receiving computer

SETUP OF SLAM CODE ON LOCAL PC:
This will tell you how to set up the ORG SLAM code with the new c file to read images that are live.
In Examples/Monocular you will fing QuadCode.cc which you will need to overwrite mono_tum.cc with this (when you want to run that code) as mono_tum.cc is the file that gets built (alternatively you can do it the 'proper way' which I never got around to and change the make file to just compile this aswell...)
You will also have to change some file paths in QuadCode.cc to tell it where the images get put and also which image resolution config to use (the resolution can be changed in the Pi code in the captureImages.py file)
I believe this should be everything you need to do once you have been able to run the example datasets given.

The slamStateMachine file contains the state machine and server code. This allows the pi to take commands from your computer about when to take and send images. This state machine will run ./runCaptureSend.sh which will start the two python files sendImages.py and captureImages.py in seperate processes. These will run till they are killed by a file which gets written by the state machine on an exit command. (Yes this code can be improved a lot. The way processes are interacting is not nice at the moment).

To start the server and state machine on the pi run:
python slamStateMachine.py

Next you can start the client on your computer (which also runs in a local state machine) which will connect to the server:
python src/quadClient.py

From there you can enter 'run', 'pause', 'exit' on your pc to change the state of the state machine both on the pi and your computer.
(There is a bug where if you try to exit without going into the 'run' state then the SLAM process will not exit. If this happens you can kill the process through htop)
