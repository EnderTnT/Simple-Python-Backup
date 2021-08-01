from time import sleep as Sleep;
from distutils.dir_util import copy_tree as Copy;
from sys import argv as Arguments;
import datetime;
import os


class AutoBackup ():
	def __init__ (self, MainFolder, Delay):
		self.MainFolder = MainFolder;

		self.Delay = Delay;

		self.Backup ();


	def Backup (self):
		while True:
			try:
				today = datetime.datetime.now();
				os.mkdir("Backup/" + today.strftime('%Y.%m.%d.%H.%M.%S'));
				Copy (self.MainFolder, "Backup/" + today.strftime('%Y.%m.%d.%H.%M.%S'));
			except:
				print ("Could Not Execute The Backup.");
				break;

			print ("Backup Done!\n Files Copied From: %s To: Backup." % (self.MainFolder));

			Sleep (int (self.Delay));



if __name__ == "__main__":
	if len (Arguments)	> 3 or len (Arguments) < 3:
		print ("\n\nUsage:\npython3 backup.py directory interval\n");
	else:
		if not os.path.exists("Backup"):
			os.mkdir("Backup")
			print("Directory 'Backup' Created ")