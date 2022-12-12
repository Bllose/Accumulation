# NumPy  
**The fundamental package for scientific computing with Python.**  
# PIP & CONDA  
The two main tools that install Python packages are ```pip``` and ```conda```. Their functionality partially overlaps (e.g. both can install ```numpy```), however, they can also work
together. We'll discuss the major differences between pip and conda here - this is important to understand if you want to manage packages effectively.  
> **overlap**  
The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that
same Python install only. This also means conda can install non-Python libraries and tools you may need (e.g. compilers, CUDA, HDF5), while pip can't.  
The second difference is that pip installs from the Python Packaging Index (PyPI), while conda installs from its own channels (typically "defaults" or "conda-forge"). PyPI is the 
largest collection of packages by far, however, all popular packages are available for conda as well.
The third difference is that conda is an integrated solution for managing packages, dependencies and environments, while with pip you may need another tool (there are many!) for
dealing with environments or complex dependencies.  
> **integrate**
# TUTORIAL  
## Content  
- Numpy Features  
- - Linear algebra on n-dimensional arrays  
- - Saving and sharing your NumPy arrays  
- - Masked Arrays
> **Linear**  
> _adjective_ LINES **consisting of or to do with lines**  
> _adjective_ LENGTH **relating to length, rather than area or volume**  
> _adjective_ CONNECTION **involving a series of events or thoughts in which one follows another one directly.**    
> **algebra**  
> _noun_ **a part of mathematics in which signs and letters represent numbers**(代数)  
> **-dimensional**  
> _suffixx_ **having measurements in the stated directions**
- NumPy Applications  
- - Determining Moore's Law with real data in NumPy  
- - Deep learning on MNIST  
- - Deep reinforcement learning with Pong from pixels  
- - Sentiment Analysis on notable speeches of the last decade   
- - X-ray image processing  
- - Determining Static Equilibrium in NumPy  
- - Plotting Fractals  
> **determine**  
> _verb_ DECIDE to control or influence something directly, or to decide what will happen.  
> _verb_ DISCOVER to discover the facts or truth about something  
> **Moore's law**  
> _noun_ **the ideal stated by Gordon Moore of Intel Corporation that the cost of a computer chip (= very small piece of electronic computer equipment ) for a particular amount of processing power will continue to fall by half every two years.**  
## NumPy Features
### Linear algebra on n-dimensional arrays   
If you want to be able to run the examples in this tutorial, you should also have ```matplotlib``` and ```SciPy``` installed on your computer.
#### Content  
In this tutorial, we will use a ***matrix decomposition*** from linear algebra, the Singular Value Decomposition, to generate a compressed approximation of a image. We'll use the **face** image from the ```scipy.misc``` module:  
``` Python
from scipy import misc
img = misc.face()
Now, **img** is a NumPy array, as we can see when using the ```type``` function:  
``` Python
type(img)
> numpy.ndarray  
We can see the image using the ```matplotlib.pyplot.imshow``` function to display plots:  
``` Python  
import matplotlib.pyplot as plt  
plt.imshow(img)
plt.show()
#### Shape, axis and array properties  
Note that, in linear algebra, the dimension of a vector refers to the number of entries in an array. In  NumPy, it instead defines the number of axes.
For example, a 1D array is a vector such as **\[1, 2, 3\]**, a 2D array is a matrix, and so forth.  
> **vector**
> _noun_ CALCULATION something physical such as a force that has size and direction  
> **refer** - refer sb/sth to sb/sth  
> phrasal verb with refer verb  
> to direct someone or something to a different place or person for information, help, or action.  
> **refer** FROM Collins VERB  
> If a word refers to a particular thing, situation, or idea, it describes it in some way.   
> **axis** _plural_:**axes**  
> An _axis_ is an imaginary line through the middle of something.  
> An _axis_ of a graph is one of the two lines on which the scales of measurement are marked.
在上一个例子中， 我们使用的```img```保存了我们图像的数组。一般理解下来，可能会觉得图像就是一个二维对象，所以保存的数组也应该是一个二维的。但实际上并非如此，可以通过如下命令查看其结构:  
``` Python
img.shape
> (768, 1024, 3)  
这意味着```img```这个数组，一共存在三维， 纵向768个对象， 横向1024个对象。二维表达的是图像中每个像素点的位置，这个很好理解。而第三维是一个RGB（red, green and blue）颜色对象， 这个对象也是一个数组。  
通过参数```ndim```可以直接返回对象的维度: ```img.ndim``` -> 3  
实际上，NumPy将每一个维度作为一个独立的轴(axis)进行保存， 这跟```imread```的工作原理有关。 在上面例子中可以通过下面命令查看**红色**元素的轴信息:  
>>> img[:,:,0]
array([[121, 138, 153, ..., 119, 131, 139],
       [ 89, 110, 130, ..., 118, 134, 146],
       [ 73,  94, 115, ..., 117, 133, 144],
       ...,
       [ 87,  94, 107, ..., 120, 119, 119],
       [ 85,  95, 112, ..., 121, 120, 120],
       [ 85,  97, 111, ..., 120, 119, 118]], dtype=uint8)
显然，单独一个颜色元素，就不需要像RGB一样，单独再多出来一个维度。所以它是二维矩阵:  
>>> img[:,:,0].shape
(768, 1024)
Since we are going to perform linear algebra operations on this data, it might be more interesting to have real numbers between 0 and 1 in each entry of the matrices to represent the RGB values. We can do that by setting:  
``` Python
img_array = img / 255  
This operation, dividing an array by a scalar, works because of NumPy's broadcasting rules.  
我们通过获取最大最小值， 可以看出我们的运算是否生效：  
>>> img_array.max(), img_array.min()
(1.0, 0.0)
>>> img.max(), img.min()
同样的， 通过类型也可以判断：  
>>> img_array.dtype
dtype('float64')
>>> img.dtype
dtype('uint8')
Note that we can assign each color channel to a separate matrix using the slice syntax:  
``` Python
red_array = img_array[:,:,0]  
green_array = img_array[:,:,1]
blue_array = img_array[:,:,2]
> **assign** _verb_ COMPUTING to put a value in a particular position in the memory of a computer.
