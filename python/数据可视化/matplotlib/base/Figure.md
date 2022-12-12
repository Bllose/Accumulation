**class matplotlib.figure.**_Figure_\( figsize=None, dpi=None， facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, 
subplotpars=None, tight_layout=None, constrained_layout=None, *, layout=None, \**kwargs \)  
The top level container for all the plot elements.  
The Figure instance supports callbacks through a _callbacks_ attribute which is a CallbackRegistry instance. 
The events you can connect to are ```dpi_changed```, and the callback will be called with func\(fig\) where fig is the Figure instance.
> **plot** _noun_ \[C\]
> (C2) GROUND a small piece of land that has been marked or measured for a particular purpose:  
> DIAGRAM a diagram or chart  
> - a vegatable plot.
> - There are several plots of land for sale.  
> **figure** _noun_ \[C\] 
> (B2) PICTURE \(_written abbreviation_ **fig.**\)  
> a picture or drawing, often with a number, in a book or other ducument:
> - Please see figure 8 and 9.
#### Parameters:  
- **figsize : 2-tuple of floats, default:** ___rcParams\["figure.figsize"\](default:___ _\[6.4, 4.8\]_ **)**  
- - Figure dimension _(width, height)_ in inches.
- **dpi : float, default: rcParams\["figure.dpi"\](default:** _100.0_ **)**  
- - Dots per inch.
