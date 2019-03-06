import caffe
from gridData import Grid
import numpy as np
caffe.set_mode_gpu()
net = caffe.Net('modelTan.prototxt', 'TanH_00001SGD_100000.caffemodel', caffe.TEST)
maxs = open("maxs.txt", "w")
e =np.mgrid[-10:10:1]
for i in range(0, 50):
        net.forward()
        for x in range(0, 20):
                grid = Grid(grid=net.blobs['ndim'].data[x].reshape((100,100,100)), origin=[0,0,0], edges=[e,e,e])
                grid.export('binmaps/actualGrid' + str(i) + str(x) + '.dx')
                grid = Grid(grid=net.blobs['unit3_conv'].data[x].reshape((100,100,100)), origin=[0,0,0], edges=[e,e,e])
                grid.export('binmaps/predictedGrid' + str(i) + str(x) + '.dx')
                print "Mean " + str(x) + ":"
                z = abs(net.blobs['ndim'].data[x] - net.blobs['unit3_conv'].data[x][0].mean())
                print z[0][0][0]
                print "Max" + str(x) + ":"
                y = abs(net.blobs['ndim'].data[x] - net.blobs['unit3_conv'].data[x][0].max())
                print y[0][0][0]

maxs.close()


