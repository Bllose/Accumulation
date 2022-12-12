Do note the difference between ```isNaN()``` and ```Number.isNaN()``` : the former will return ```true``` if the value is currently ```NaN```, or if it is going to be ```NaN``` after it is coerced to a number, while the latter will return ```true``` only if the value is currently ```NaN```:  
isNaN('Hello World');    //true
Number.isNaN('Hello World'); // false
> **coerce** _verb_ to persuade someone forcefully to do something that they are unwilling to do.  
> Synonyms: force/pressure
# eval()  
> **evaluate** _verb_ (C1) to judge or calculate the quality, importance, amount, or value of something.  
#### ***Warning***: Excuting JavaScrpt from a string is an enormous security risk. It is far too easy for a bad actor to run arbitrary code when you use ```eval()```.   
> **enormous** _adjective_ (B1) extremely large  
> Potential risk.  
> **arbitrary** _adjective_ CHANCE (C2) based on chance rather than being planned or based on reason.  
#### Syntax  
eval(string)
##### Parameters  
**string**  
A string representing a JavaScript expression, statement, or sequence of statements. The expression can include variables and properties of existing objects.  
##### Retrun value  
The completion value of evaluating the given code. If the completion value is empty, ```undefined``` is returned.
