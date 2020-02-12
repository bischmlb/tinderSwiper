# tinderSwiper (also works for badoo)

In order to run the program you should create a file ```secrets.py``` in the main folder, and set the variables ```username``` and ```password```.  
They should be set to the credentials you wish to log in with.   
Ex:  
```py
username = 'user123'
password = 'pass123'
```  
Currently the ```chromedriver.exe``` is for Windows, but if you use other OS you should make sure that chromedriver is reachable from the files.  

You will also need ```selenium``` which can be installed with ```pip```  

##### todo:
- *add ```randomness``` to which the bot should swipe right/left in future for premium users to make bot detection harder, but should not be needed for free versions*
- *add UI (with tkinter?)*
