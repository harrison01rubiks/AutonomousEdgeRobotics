# **06 Connect Desktop Pi to Robot Pi**

## Prerequisites:

1. Robot is on
1. Desktop Pi is connected to monitor, keyboard and powered on

## Steps:

1. **SSH Connection**
  
   ~~~
   ssh pi@XXX.XXX.XXX.XXX
   ~~~

1. **VNC Connection**
  
   ~~~
   sudo python 
   ~~~

1. **Jupyter Lab Connection**
  
   ~~~
   ssh pi@XXX.XXX.XXX.XXX
   ~~~
   ~~~
   cd /home/pi/Desktop/JupyterNotebooks
   sudo jupyter notebook --ip='*' --port=8888 --no-browser --allow-root
   ~~~

   First time login - create a password
   - Copy the token from the terminal window 
   - Open a browser and connect to http://XXX.XXX.XXX.XXX:8888
   - Use the token copied from the terminal window and paste it in the section **Setup a Password** then add your own password 

  
