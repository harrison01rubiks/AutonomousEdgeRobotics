# **200 Robot Pi Image**

1. **Create a fresh Raspberry Pi OS**
  Use Raspberry Pi Imager to create a fresh Raspberry Pi OS (64-bit) SD card
   - https://www.raspberrypi.com/software/
   - current imager version 1.8.5
   - current Pi OS Released: 2024-03-15
  
3. **Boot the Raspberry Pi with the new card**

1. **change defaul password for pi**

   Note: pi default password is raspberry

   run the passwd command in a teminal window and follow instructions
   
    ~~~
    passwd
    ~~~
    
1. **Enable interface:** ssh, vnc and i2c

    ~~~
    sudo raspi-config
    ~~~
    Optional - change Hostname: raspi-config / 1. system options / S4 Hostname 

1. **Update OS to current patch level**

    ~~~
    sudo apt-get update && sudo apt-get upgrade -y
    ~~~
    
1. **Remove installed packages that are no longer required**

    ~~~
    sudo apt autoremove -y
    ~~~
    
1. **Remove update block**

    ~~~
    sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
    ~~~

    
1. **Install tensorflow lite and OpenVC**

    ~~~
    sudo pip3 install opencv-contrib-python
    ~~~

1. **View OpenCV version that was installed (4.9.0)**

    ~~~
    sudo python3 -c "import cv2; print(cv2.__version__)"
    ~~~
    OpenCV version = 4.9.0

1. **Install Juptyer Notebook**

    ~~~
    sudo pip3 install jupyter
    ~~~

1. **Additional libraries needed**

    ~~~
    sudo pip install PyYAML
    sudo pip install rpi_ws281x
    sudo pip install json-rpc
    sudo pip install matplotlib
    sudo pip install pandas
    sudo apt-get install python3-pyqt5.qtsql
    ~~~
    - sudo pip install typing-extensions --upgrade
1. **Add MasterPi and MasterPi_PC_Software folder to /home/pi/**

1. **Add AutonomousEdgeRobotics folder to /home/pi/Desktop/**


