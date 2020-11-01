#1
import numpy as np

#2
# print(np.__version__)
# np.show_config()

#3　
# a = np.zeros(10)
# print(a)

#4
# a = np.zeros([10,10])
# print(a)
# print(a.size,a.itemsize)
# print("%d bytes" % (a.size * a.itemsize))

#5
#python -c "import numpy; numpy.info(numpy.add)"

#6
# a = np.zeros(10)
# a[4] = 1
# print(a)

#7
# a = np.arange(10,50)
# a = a[::-1]
# print(a)

#8
# a = np.arange(10,50)
# a = a[::-1]
# print(a)

#9
# a = np.arange(9).reshape([3,3])
# print(a)

#10
# a = np.asarray([1,2,0,0,4,0])
# print(a.nonzero())

#11
# a = np.eye(3)
# print(a)

#12
# a = np.random.randint(1,10,(3,3,3))
# print(a)

#13
# a = np.random.rand(10,10)
# print(a)
# print("max=",a.max(),"min=",a.min())

#14
# a = np.random.rand(30)
# print(a)
# print(a.mean())

#15
# a = np.ones((10,10))
# a[1:-1,1:-1] = 0
# print(a)

#16
# a = np.ones([5,5])
# a = np.pad(a,pad_width=1,mode="constant",constant_values=0)
# print(a)

#17
# print(0*np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(np.nan in set([np.nan]))
# print(0.3 == 3*0.1)

#18
# a = np.diag(np.arange(1,5), k=-1)
# print(a)

#19
# a = np.zeros([8,8])
# a[1::2,::2] = 1 #２行から１個飛ばしでスタート、一番左はしの列から一個飛ばしで１を入れる、
# a[::2,1::2] = 1 #一番上の列から１個飛ばし、２列から１個飛ばしで１を入れる
# print(a)

#20
# print(np.unravel_index(100,(6,7,8)))

#21
# a = np.tile([[0,1],[1,0]],(4,4))
# print(a)

#22
# a = np.random.random([5,5])
# a = (a-np.min(a))/(np.max(a)-np.min(a))
# print(a)

#23
# a = np.dtype([("r",np.ubyte,1),("g",np.ubyte,1),("b",np.ubyte,1),("a",np.ubyte,1)])

#24
# a = np.ones([5,3])
# b = np.ones([3,2])
# print(a.dot(b))

#25
# a = np.arange(1,10)
# a[(3<a)&(a<8)] *= -1
# print(a)

#26
# print(sum(range(5),-1))
# from numpy import *
# print(sum(range(5),-1))

#27
# Z = np.asarray([1,2,3])
# print(Z**Z)
# print(2 << Z >> 2)
# print(Z <- Z)
# print(1j*Z)
# print(Z/1/1)
# print(Z<Z>Z)

#28
# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
# print(np.array([np.nan]).astype(int).astype(float))

#29
# a = np.random.uniform(-10,10,10)
# print(np.copysign((np.ceil(np.abs(a))),a))

#30
# a = np.random.randint(1,10,10)
# b = np.random.randint(1,10,10)
# print(np.intersect1d(a,b))

#31

