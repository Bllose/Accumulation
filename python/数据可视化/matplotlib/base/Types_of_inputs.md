[ORIGINAL INFORMATION](https://matplotlib.org/stable/tutorials/introductory/usage.html)  
# [NumPy](https://www.scipy.org)
1. An array object of arbitrary homogeneous items
2. Fast mathematical operations over arrays
3. Linear Algebra, Fourier Transforms, Random Number Generation  
## numpy.ma.masked_arry  
numpy.ma : a package to handle missing or invalid values.
This package was initially written for numarray by Paul F. Dubois
at Lawrence Livermore National Laboratory.
In 2006, the package was completely rewritten by Pierre Gerard-Marchant
(University of Georgia) to make the MaskedArray class a subclass of ndarray,
and to improve support of structured arrays.
## numpy.asarray  
Functions in the ``as*array`` family that promote array-likes into arrays.
`require` fits this category despite its name not matching this pattern.  
## OTHERS  
Most methods will also parse an addressable object like a _dict_, a ```numpy.recarray```, or a ```pandas.DataFrame```.
Matplotlib allows you provide the __data__ keyword argument and generate plots passing the strings corresponding to the _x_ and _y_ variables.
