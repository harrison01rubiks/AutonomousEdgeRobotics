# **04 Desktop Setup**


## Prerequisites:

1. SD card is in the Raspberry Pi 5
1. Robot Pi is connected to monitor and keyboard
1. Power is connected and Pi desktop is running
1. Pi is connected to local wifi

<img src="https://github.com/stemoutreach/AutonomousEdgeRobotics/blob/main/Session-1/images/PiDesktop.jpg" width="500" > 

## Steps:

1. **Run Camera test**

    ~~~
    sudo python
    ~~~

1. **Jupyter Lab Connection**
  
   ~~~
   cd /home/pi/Desktop
   jupyter notebook --ip='*' --port=8888 
   ~~~

   First time login - create a password
   - Copy the token from the terminal window 
   - Open a browser and connect to http://XXX.XXX.XXX.XXX:8888
   - Use the token copied from the terminal window and paste it in the section **Setup a Password** then add your own password 
