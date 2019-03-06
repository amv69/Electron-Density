# Electron-Density
## Undergraduate Research Project
### Requirements
* Install Requirements from requirements.txt
* Install Horton from https://github.com/theochem/horton

### File Structure
* newOut.py outputs files from your dataset (Example file included in data) as binmaps, dx, and xyz
* name.py creates the TESTMOL and TRAINFILE files needed for the model(Examples included)
  * empty and ligmap are needed for the model and these files
* modelTan.prototxt is the current architecture of the network
* solvers included are the best working SGD and Adam based solvers
* Train & Test using caffe
* use printError.py to output actual Grids and predicted Grids and print max per voxel error
