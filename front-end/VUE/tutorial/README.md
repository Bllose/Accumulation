# [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_getting_started)  
通过 ```Vue-cli``` 初始化一个 VUE 项目 ``` vue create moz-todo-vue ``` 。  
进入项目后， 执行命令即可运行当前项目 ```npm run serve```
# moz-todo-vue  
通过搭建一个 todo list 项目， 逐步说明 vue 项目的构建、原理  
首先、项目通过Vue的命令行脚手架进行初始化。  
然后通过添加组件，一点一点完善功能。  
在当前案例中，并未使用```vue```对象，而是直接通过js操作HTML，编译过程中已经完成对HTML的element的修改。 所以在控制台中没有 vue对象。  
### 已知的知识点  
#### package.json  
该文件保存了项目中的各种元信息， 比如项目名称、版本、依赖等等。  
申明依赖后， 可以在js model中import。  
例如，在依赖中申明了:  
  "dependencies": {
    "core-js": "^3.6.5",
    "lodash.uniqueid": "^4.0.1",
    "vue": "^3.0.0"
那么在项目中可以导入：  
import uniqueId from 'lodash.uniqueid'  
import { createApp } from 'vue'
其中，对于 vue 的依赖，是脚手架初始化过程中就已经写入的。 而针对```lodash.uniqueid```依赖的添加，是通过命令```npm install --save lodash.uniqueid```添加的。  
#### 绑定  
```{{}}``` 这种格式将```vue```中的参数绑定到HTML页面上。 通常这个绑定的内容是一个字符串。   
```v-bind:attribute="expression"```，同时支持缩写，即在被绑定的attribute/prop前直接加冒号即可。所以如下的两种形式是一样的:  
<input type="checkbox" id="todo-item" v-bind:checked="isDone" />
<input type="checkbox" id="todo-item" :checked="isDone" />
### 待确认问题  
通过脚手架建立的 VUE 项目， 没有明确指定首页调用路径或者路由没有， 不知道如何指向到```moz-todo-vue/public/index.html```的。    
之前官网学习的内容是通过引入 ```vue.js``` 然后初始化一个```vue```对象：```var app = new Vue({...})```的， 或者初始化、注册一个组件```Vue.component(...)```。  
而脚手架搭建的项目，组件是直接以```.vue```文件的形式呈现的，名字也是以 PExamplealCase 与 kebab-case 的形式一一对应的。 这些规则并没有具体的说明，只能通过真实的运行结果推测，该项目的运作机制就是如此。
引入 vue.js 文件的页面可以被 vue devtools 识别， 但是通过 vue cli init 的项目却不能？
