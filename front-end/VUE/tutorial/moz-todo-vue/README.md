Vue has three common approaches to styling apps:
- External CSS files.
- Global styles in Single File Components (```.vue``` files).
- Component-scoped styles in Single File Components.
To start with, create a file called reset.css in the src/assets directory. Files in this folder get processed by Webpack. This means we can use CSS pre-processors (like SCSS) or post-processors (like PostCSS).
While this tutorial will not be using such tools, it's good to know that when including such code in the assets folder it will be processed automatically.  
#### 缺乏相关知识记录
在assets目录下的文件，会被```Webpack```执行，这意味着我们可以定义使用预加载样式（SCSS）和延后加载样式（PostCSS）。
