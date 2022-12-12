- npm / cnpm
- webpack
- vue-cli
对于想纯净学习，不像花太多精力在其他工具上时，可以直接使用如下命令添加vue:
<!-- dev version -->
<!-- <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script> -->
<!-- production version, optimized for size and speed -->
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
## Vue Devtools
强烈建议在浏览器上安装[Vue Devtools](https://github.com/vuejs/devtools#vue-devtools)
由于各种原因，无法在线初始化 vue 项目时。 即 ```vue init webpack project_name``` 无法成功时，使用离线实现 ```vue init webpack vuedemo --offline```
[离线初始化解决方案](https://blog.csdn.net/feinifi/article/details/104578546)  
总体来说，就是将项目[vue-templates/webpack](https://github.com/vuejs-templates/webpack)下载到本地，并将其解压到默认路径(windows下为C:\Users\YourName\.vue-templates\webpack)。  
# A clearer Vue  
Vue is a modern JavaScript framework that provides useful facilities for progressive enhancement - unlike many other frameworks, you can use Vue to enhance existing HTML. 
This lets you use Vue as a drop-in replacement for a library like JQuery.   
> **facilities** (B1) the buildings, equipment, and services provided for a particular purpose.  
> **progressive** _adjective_ GRADUAL (c1) developing or happening gradully.  
> **drop-in** used to describe a place where people can go, usually to get help or advice, at any time without making an appointment.  
> PS: a drop-in centre for the homeless.  
That being said, you can also use Vue to write entire Single Page Applications (SPAs). This allows you to create markup managed entirely by Vue, which can improve developer experience and performance when dealing with complex applications. It also allows you to take advantage of libraries for client-side routing and state management when you need to. Additionally, Vue takes a "middle ground" approach to tooling like client-side routing and state management. While the Vue core team maintains suggested libraries for these functions, they are not directly bundled into Vue. This allows you to select a different routing/state management library if they better fit your application.    
> **entirely** _adverb_ (B2) completely; _Synonyms_ completely, exclusively, totally, wholly;  
> **exclusively** _adverb_ (C1) ONLY; PS: This offer is available exclusively to our established customers.
