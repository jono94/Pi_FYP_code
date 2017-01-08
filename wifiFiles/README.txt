These two files will allow you to connect to the uni wifi (atleast in EE)
The interfaces file should be in /etc/network/ and the wpa file in /etc/wpa_supplicant/
Note that when setting up the Pi as a wireless access point the interfaces file will have to be changed (the bottom section which is commented out should allow for use as access point and the uni wifi part should then be commneted out)
NOTE: you will need to add your student number and password to the wpa file where the placeholders exist
