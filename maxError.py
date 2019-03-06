import caffe
import numpy as np
caffe.set_mode_gpu()
net = caffe.Net('model.prototxt', 'model_iter_250000.caffemodel', caffe.TEST)
maxs = open("maxs.txt", "w")
net.forward()
for i in range(0, 50):
	for x in range(0, 20):
		f = open("binmaps/actualGrid" + str(x) +".binmap", "w")
		f.write(net.blobs['ndim'].data[x])
		f.close()
		f = open("binmaps/predictedGrid" + str(x) +".binmap", "w")
        	f.write(net.blobs['unit3_conv'].data[x])
		f.close()
		print "Mean " + str(x) + ":"
		z = abs(net.blobs['ndim'].data[x] - net.blobs['unit3_conv'].data[x][0].mean())
		print z[0][0][0]
        	print "Max" + str(x) + ":"
		y = abs(net.blobs['ndim'].data[x] - net.blobs['unit3_conv'].data[x][0].max())
		print y[0][0][0]
		maxs.write(y[0][0][0])

maxs.close()


