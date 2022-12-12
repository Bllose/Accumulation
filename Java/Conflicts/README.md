# [How Maven chooses the version of dependency](https://medium.com/@liam.su8/how-to-solve-dependency-conflicts-with-maven-76f3b08f89a2)  
2 rules:  
- **Nearest definition wins**  
- **First declaration wins**  
| `-B 1.0
    `-B 2.0
Becouse of the first path is shorter than the second one, version 1.0 will be chosen by Maven.  
| `-B 1.0
  `-B 2.0
If two dependency versions are at the same depth, the dependency which be imported earlier will be chosen.
## To specify the version we want
There are 3 solutions.  
- excluding the version you don't want when importing the dependency.  
- importing the version you want directly in your project.
- using dependency management.  
Note: The dependency management's priority is lower than the directly imported one.
