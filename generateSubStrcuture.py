
import sys
import os 


baseFolder = os.path.abspath(os.path.dirname(__file__))
crnt = os.getcwd()
os.chdir(baseFolder)
subFolders = ["Images"]

sub = sys.argv[1]

def safeCreate(path) :
	if not os.path.exists(path) :
		os.makedirs(path)

safeCreate(f".//{sub}")

os.chdir(f".//{sub}")

for subFolder in subFolders :
	safeCreate(f".//{subFolder}")

for chapter in sys.argv[2:] :
	if not os.path.exists(f".//{chapter}.md") :
		with open(f".//{chapter}.md","x") :
			pass 
	for subFolder in subFolders :
		safeCreate(f".//{subFolder}//{chapter}") 



os.chdir(crnt)
