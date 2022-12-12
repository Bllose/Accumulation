# index.html
该样例就是一个非常简单、原始的 Vue app 样例。  
样例代码虽然简单， 但是Vue在背后做了很多工作。 它让数据与```DOM```关联了起来， 他们是可以互动的。  
比如： 打开浏览器控制台， 然后将```app.message```修改为其他值时， 页面上也会被重新渲染成新的值。  
# Inaddtion.html
- ```v-bind``` 动态绑定
- ```v-if``` 判断条件
- ```v-for``` 循环执行
# composing.html  
### Composing with Components  
> **compose** _verb_ ARRANGE TEXT to arrange words, sentences, pages, etc. in preparation for printing   
> **component** _noun_ (C1) a part that combines with other parts to form something bigger  
The component system is another important concept in Vue, because it's an abstraction that allows us to build large-scale applications composed of small, self-contained, and often
reusable components. If we think about it, almost any type of application interface can be abstracted into a tree of components:  
![TreeComponents](https://vuejs.org/images/components.png)  
In Vue, a component is essentially a Vue instance with pre-defined options. Registering a component in Vue is straightforward:   
> **essentially** _adverb_ (B2) relating to the most important characteristics or ideas of something; _synonyms_ basically, fundamentally
// Define a new component called todo-item  
Vue.component('todo-item', {
  template: '<li> This is a todo </li>'
var app = new Vue(...)
Now you can compose it in another component's template:  
  <!-- Create an instance of the todo-item component -->
  <todo-item></todo-item>
But this would render the same text for every todo, which is not super interesting. We should be able to pass data from the parent scope into child components. Let's modify the
component definition to make it accepte a [prop](https://vuejs.org/v2/guide/components.html#Passing-Data-to-Child-Components-with-Props).  
## composing_1.html  
仿造样例自定义一个获取单词与词义进行展示的界面。  
在控制台输入：```app8.expressList.push({word:'a', exp: 'b'})``` 可以动态渲染新增词语解释。  
在此技术上增加内容：  
1. 定义数据结构 
2. 画出合适结构用以展示
3. 定义CSS美化界面
4. 定义图层，自定义展示形式
# instances.html  
针对Vue实例的一些验证。  
打开当前页面，在控制台输入：  
```data.a = 3```  
> We find that the oldValue:1 had been changed to newValue:3  
通过添加前缀```$```在参数或者方法前，用以表明这是用户自定义参数、方法。  
当前案例中， 通过```$watch```自定义对参数```a```进行监听，一旦它被改变， 则方法```$watch```就会被调用。  
另外一些基本概念，
