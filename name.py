import glob
import ntpath

f = open("/net/pulsar/home/koes/amv69/TRAINFILE", "w").close()
f = open("/net/pulsar/home/koes/amv69/TESTMOL", "w").close()

trainFile = open("/net/pulsar/home/koes/amv69/TRAINFILE", "w")
testMol = open("/net/pulsar/home/koes/amv69/TESTMOL", "w")
print ("reached")
dxFiles = glob.glob("/net/pulsar/home/koes/amv69/data/" + "*.binmap")
molFiles = glob.glob("/net/pulsar/home/koes/amv69/data/" + "*.xyz")
print("reached")
lineNumber = 0
print dxFiles
dir = "/scr/amv69/"
for filename in dxFiles:
    try:
        trainFile.write(str(lineNumber) + " " + dir + ntpath.basename(filename) + '\n')
        lineNumber += 1
	print lineNumber
    except FileNotFound:
        continue

trainFile.close()
lineNumber = 0

for filename in molFiles:
    try:
        testMol.write(str(lineNumber) + " " + "none" + " " +  dir + ntpath.basename(filename) + '\n')
        lineNumber += 1
    except FileNotFound:
        continue

testMol.close()
