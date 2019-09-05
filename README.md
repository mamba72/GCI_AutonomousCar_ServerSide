# GCI_AutonomousCar_ServerSide
This will be the code for the while Sever Side of the autonomous car.
This is the part of the code that will run on the base machine. 
It will serve two functions:
	1. This will be able to train the neural network on the images provided.
	2. This will be able to open up a socket that listens for incoming connections that will send this server a stream of images and it will
	sent back information gathered from the images to the Raspberry Pi.
		This is supposed to be doing the heavy lifting of the machine learning part so the Pi doesnt have to.

