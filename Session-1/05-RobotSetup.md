# **05 Robot Setup**

<img src="https://github.com/stemoutreach/AutonomousEdgeRobotics/blob/main/Session-1/images/IMG_2048.jpg" width="400" > 

## Prerequisites:

1. Robot is assembled
1. SD card is in the Raspberry Pi on the robot
1. Batteries are charged and installed
1. Robot Pi is connected to monitor and keyboard

## Steps:

1. **Turn on Robot**
1. **Run start up script**
  
   Open a terminal and enter the following command. (This script initualizes the robot and sets the arm to starting position) 
   ~~~
   sudo python StartUp.py
   ~~~

1. **Run servo test**

   The following script will move each servo a little starting with the claw. Check to make sure all servos are plugged into the correct location. The wheels will also run in order:
   - left front
   - right front
   - left back
   - right back  

    ~~~
   sudo python MasterPi/HiwonderSDK/Servo_test.py
    ~~~

1. **Run Camera test**

    NOTE: monitor must be connected to the robot to vew camera window.
    ~~~
    sudo python CameraTest.py
    ~~~

1. **Calibrate servos**  if needed

    ~~~
    sudo python MasterPi/MasterPi.py &
    python MasterPi_PC_Software/Arm.py
    ~~~
