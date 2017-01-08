To start the state machine on the raspberry Pi:
python slamStateMachine.py
This will start the tcp server. After this the client on your computer can be started:
python src/quadClient.py
NOTE: this is from the ORBSLAM code and will start the client along withthe state machine that alows the live orb slam to be run:
Commands are run, pause, exit.
NOTE: ip, name and password will all have to be added to the sendImages.py file to tell the code where to send the images. File paths aswell.
