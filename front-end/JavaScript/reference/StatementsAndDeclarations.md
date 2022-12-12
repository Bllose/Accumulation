# const  
Constants are block-scoped, much like variables declared using the ```let``` keyword.    
> **scope** _noun_ RANGE (C1) the range of a subject covered by a book, programme, discussion, class, etc.  
> **constant** _adjective_ FREQUENT (B2) happening a lot or all the time.  
The value of a constant can't be changed through reassignment(```=```), and it can't be redeclared. 
However, if a constant is an object or array its properties or items can be updated or removed.  
#### Description  
This declaration creates a ```const``` whose scope can be either global or local to the block in which it is declared. Global constant do **not** become properties of the ```window``` object, unlike ```var``` variables. 
> const one = '1'
> var two = '2'
> window.two
> window.one
< undefine
The ```let``` statement declares a block-scoped local variable, optionally initializing it to a value.  
#### Description  
```let``` allows you to declare variables that are limited to the scope of a block statement, or expression on which it is used, unlike the ```var``` keyword, which declares a variable globally, or locally to an entire function regardless of block scope. The other difference between ```var``` and ```let``` is that the latter is initialized to a value only when a **parser evaluates** it (see below).  
An explanation of why the name "**let**" was chosen can be found [here](https://stackoverflow.com/questions/37916940/why-was-the-name-let-chosen-for-block-scoped-variable-declarations-in-javExampleri)  
The ```var``` statement declares a function-scoped or global-scoped variable, optional initializing it to a value.  
#### Description  
```var``` declarations, wherever they occur, are processed before any code is executed. This is called _hoisting_, and is discussed further below.    
> **hoist** _verb_ to lift something heavy, sometimes using ropes or a machine.
The scope of a variable declared with ```var``` is its current _execution context_ and closures thereof, which is either the enclosing function and functions declared within it, or, for variables declared outside any function, global. Duplicate variable declarations using ```var``` will not trigger an error, even in strict mode, and the variable will not lose its value, unless another assignment is performed.  
'use strict';
function foo() {
  var x = 1;
  function bar() {
    var y = 2;
    console.log(x); // 1 (function `bar` closes over `x`)
    console.log(y); // 2 (`y` is in scope)
  console.log(x); // 1 (`x` is in scope)
  console.log(y); // ReferenceError in strict mode, `y` is scoped to `bar`
Variables declared using ```var``` are created before any code is executed in a process known as _hoisting_. Their initial value is ```undefined```.  
'use strict';
console.log(x);                // undefined (note: not ReferenceError)
console.log('still going...'); // still going...
var x = 1;
console.log(x);                // 1
console.log('still going...'); // still going...
## Example
#### Block scoping  
It's important to note the nature of block scoping.  
``` JavaScript
// 将抛出异常: Uncaught SyntaxError: Missing initializer in const declaration
const MY_FAV
const MY_FAV = 7;
// 以下所有赋值操作均将抛出异常
//  Uncaught SyntaxError: Identifier 'MY_FAV' has already been declared
const MY_FAV = 20;
var MY_FAV = 20;
let MY_FAV = 20;
if (MY_FAV === 7) {
  // this is fine and creates a block scoped MY_FAV variable
  // (works equally well with let to declare a block scoped non const variable)
  let MY_FAV = 20;
  // MY_FAV is now 20
  console.log('my favorite number is ' + MY_FAV);
// MY_FAV is still 7
console.log('my favorite number is ' + MY_FAV);
> my favorite number is 20  
> my favorite number is 7
