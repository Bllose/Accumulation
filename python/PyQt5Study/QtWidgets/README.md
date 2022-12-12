# Widgets
## [Information below get from QT5](https://doc.qt.io/qt-5/qwidget.html)
#### Detailed Description  
The widget is the atom of the user interface: it receives mouse, keyboard and other events from the window system, and paints a representation of itself on the screen.
Every widget is rectangular, and they are sorted in a Z-order.
A widget is clipped by its parent and by the widgets in front of it.  
A widget that is not embedded in a parent widget is called a window.
In Qt, QMainWindow and the various subclasses of QDialog are the most common window types.
Every widget's constructor acceptes one or two standard arguments:  
- **QWight** \*parent = nullptr is the parent of the new widget. If it is nullptr(the default), the new widget will be a window. If not, it will be the child of parent, and be constrained by parent's geometry(unless you specify Qt::Windows as window flag)
- **Qt::WindowFlags** f = { }
#### Size Hints and Size Policies  
When implementing a new widget, it is almost always useful to reimplement ```sizeHint()``` to provide a reasonable defualt size for the widget and to set correct size policy with ```setSizePolicy()```.  
By default, composite widgets which do not provide a size hint will be sized according to the space requirements of their child widgets.  
The size policy lets you supply good default behaviour for the layout management system, so that other widgets can contain and manage yours easily.
The default size policy indicates that the size hint represents the preferred size of the widget, and this is often good enough for many widgets.
**baseSize**:```QSize```  
The base size is used to calculate a proper widget size if the widget defines ```sizeIncrement()```.  
By default, for a newly-created widget, this property contains a size with zero width and height.
**sizeIncrement**: ```QSize```  
This property holds the size increment of the widget
When the user resizes the window, the size will move in steps of ```sizeIncrement().width()``` pixels horizontally and ```sizeIncrement.height()``` pixels vertically, with ```baseSize()``` as the basis. Preferred widget sizes are for non-negative integers _i_ and _j_ :  
# Layouts
Layouts are an elegant and flexible way to automatically arrange child widgets within their container.
Each widget reports its size requirements to the layout through the ```sizeHint``` and ```sizePolicy``` properties, and the layout distributes the available space accordingly.   
## Horizontal, Vertical, Grid and Form Layouts
The easiest way to give your widgets a good layout is to use the built-in layout managers:
```QHBoxLayout```, ```QVBoxLayout```, ```QGridLayout```, and ```QFormLayout```.
These classes inherit from ```QLayout```, which in turn derives from ```QObject```(not ```QWidget```).
