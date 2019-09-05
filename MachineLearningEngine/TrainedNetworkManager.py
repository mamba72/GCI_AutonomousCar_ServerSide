#This class will be the object that manages reading and writing of the tensorflow models.
#This will also be creating a .csv file to manage the performance of each model.

class TrainedNetworkManager:
	
	public:
	#this will write the model to the file and also include it in a .csv file
	def WriteModel():
		print("Writing model to file.")
		pass

	#this function will read in and return the model and all the stats about that model listed in the .csv file.
	#it should also present a warning if the user is trying to use a model that does not have the highest recorded accuracy.
	def ReadModel():
		print("Reading model from file.")
		pass


