
These two files will allow you to connect to the uni wifi (atleast in EE).

The interfaces file should be in /etc/network/ and the wpa file in /etc/wpa_supplicant/

Note: When setting up the Pi as a wireless access point the interfaces file will have to be changed
      by altering which wlan0 section is commented out.

NOTE: You will need to add your student number and password to the wpa file where the placeholders exist
      to allow authentification
