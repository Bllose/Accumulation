# The Axes class  
``` Python 
class matplotlib.axes.Axes( fig, rect, *, facecolor=None, frameon=True, sharex=None, sharey=None, label='', 
xscale=None, yscale=None, box_aspect=None, **kwargs)  
Bases: ***matplotlib.axes._base._AxesBase***  
The Axes contains most of the figure elements: **Axis, Tick, Line2D, Text, Polygon,** etc., and sets the coordinate system.  
The Axes instance supports callbacks through a callbacks attribute which is a CallbackRegistry instance. The events you can connect to are
```xlim_changed``` and ```ylim_changed``` and the callback will be called with func(ax) where ax is the Axes instance.  
> **coordinate** _noun_ (POSITION)  
> one of a pair of numbers and/or letters that show the exact position of a point on a map or graph:
> - Put in the GPS coordinates and zoom in on the map.
> - Students learn the fundamentals of graphs and how X and Y coordinates work.
An Axes is an Artist attached to a Figure that contains a region for plotting data, and usually includes tow (or three in the case of #D) Axies objects
(be aware of the difference between **Axes** and **Axis**) that provide ticks and tick labels to provide scales for the data in the Axes.
### Axis  
These objects set the scale and limits and generate ticks (the marks on the Axis) and ticklabels (strings labeling the ticks). The location of the ticks
is determined by a Locator object and the ticklabel strings are formatted by a Formatter. The combination of the correct Locator and Formatter gives very
fine control over the tick locations and labels.  
> **scale** _noun_  
> (B2) MEASURE \[C\] a set of numbers, amounts, etc., used to measure or compare the level of something.  
> - How would you rate his work on a scale of 1 to 5.
