from horton import *
import horton
import numpy as np
import struct
import ctypes
import sys
import caffe
from gridData import Grid
import os

path = sys.argv[1]
outPath = sys.argv[2]
fileNumber = 0
lineNumber = 1
f = open('TRAINFILE', 'w').close()
f=open('TESTMOL','w').close()

print os.listdir(path)
for filename in os.listdir(path):
        mol = IOData.from_file(path + filename)
        grid = BeckeMolGrid(mol.coordinates, mol.numbers, mol.pseudo_numbers)
        dm_full = mol.get_dm_full()
        rho = mol.obasis.compute_grid_density_dm(dm_full, grid.points)
        coords = np.mgrid[-10:10:.2,-10:10:.2,-10:10:.2]
        g = np.stack(coords,axis=3)
        points = g.reshape(100*100*100,3)
        density = mol.obasis.compute_grid_density_dm(dm_full,points)
        e=np.mgrid[-10:10:.1]
        grid = Grid(grid=density.reshape((100,100,100)), origin=[0,0,0],edges=[e,e,e])
        dxName = 'out' + str(fileNumber) + '.dx'
        grid.export(outPath + dxName)
        molName = 'mol' + str(fileNumber) + '.xyz'
        horton.io.dump_xyz(outPath + molName, mol)
        temp = grid
        x = np.array(density.reshape((100,100,100)))
        print x.size,x[0][0]
        out = struct.pack('%sf'  %x.size, *x.flatten())
        outName = 'out' + str(fileNumber) + '.binmap'
        f = open(outPath + outName, 'wb')
        f.write(out)
        f.close()
        fileNumber = fileNumber + 1
	f = open('TRAINFILE','a')
	f.write(str(lineNumber) + " "  + outPath + outName + "\n")
	f.close()
	f = open('TESTMOL', 'a')
	f.write(str(lineNumber) + " "  + "none" + " " +  outPath + molName + "\n")
	f.close()
	lineNumber = lineNumber + 1
