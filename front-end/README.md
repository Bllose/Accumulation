# [Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)  
When writing code for the Web, there are a large number of Web APIs available. Below is a list of all the APIs and interfaces that you may be able to use while developing your Web app or site.  
Web APIs are typically used with JavaScript, although this dosen't always have to be the case.
- - [Console API](https://developer.mozilla.org/en-US/docs/Web/API/Console_API)
- - Window
The **Document Object Model** is the data representation of the objects that comprise the structure and content of a document on the web.  
### What is the DOM?  
The Document Object Model is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content.
The DOM represents the document as nodes and objects; that way, programming languages can interact with the page.  
A web page is a document that can be either displayed in the browser window or as the HTML source. 
In both cases, it is the same document but the Document Object Model representation allows it to be manipulated.
As an object-oriented representation of the web page, it can be modified with a scripting language such as JavaScript.  
All of the properties, methods, and events available for manipulating and creating web pages are organized into objects. For example, the ```document``` object that represents the document itself, any ```table``` objects that implement the ```HTMLTableElement``` DOM interface for accessing HTML tables, and so forth, are all objects.  
### Fundamental data types  
> **Note**: Because the vast majority of code that uses the DOM revolves around manipulating HTML documents, it's common to refer to the nodes in the DOM as **elements**,
> although strictly speaking not every node is an element.  
> **manipulate** _verb_ USE HANDS to control something using the hands.  
> **revolve around sb/sth** _verb_ to have someone or something as the main or most important interest or subject.
| Data type(Interface) | Description |  
| --- | --- |  
| Document | When a member returns an object of type _document_ (e.g., the _ownerDocument_ property of an element returns the _document_ to which it belongs), this object is the root _document_ object itself. The ```DOM document Reference``` chapter describes the _document_ object |
| Node | Every object located within a document is a node of some kind. In an HTML document, an object can be an element node but also a text node or attribute node. |  
| Element | The _element_ type is based on _node_. It refers to an element or a node of type _element_ returned by a member of the DOM API. Rather than saying, for example, that  the ```document.createElement()``` method returns an object reference to a _node_, we just say that this method returns the _element_ that has just been created in the DOM. _element_ objects implement the DOM _Element_ interface and also the more basic _Node_ interface, both of which are included together in this reference. |  
| NodeList | | 
| Attr | | 
| NamedNodeMap| | 
```Node.js``` is a JavaScript runtime built on Chrome's V8 JavaScript engine.  
## About Node.js  
As an asynchronous event-driven JavaScript runtime, Node.js is designed to build scalable network applications. 
In the following "hello world" example, many connections can be handled concurrently. Upon each connection, the
callback is fired, but if there is no work to be done, Node.js will sleep.  
``` Node.js
const http = require('http');  
const hostname = '127.0.0.1';
const port = 3000;  
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
server.listen(port, hostname, () => {
  console.log(`Server runing at http://${hostname}:${port}/`);
Create a file named ```app.js``` containing the contents.  
Now, run your web server using ```node app.js```. Visit ```http://localhost:3000``` and you will see a message saying "Hello World".  
## Introduction to Node.js  
Node.js is an open-source and cross-platform JavaScript runtime environment. It is a popular tool for almost any kind of project!  
Node.js runs the V8 JavaScript engine, the core of Google Chrome, outside of the browser. This allows Node.js to be very performant.  
A Node.js app runs in a single process, without creating a new thread for every request. Node.js provides a set of asynchronous I/O **primitives** in its standard library that 
prevent JavaScript code from blocking and generally, libraries in Node.js are written using non-blocking **paradigms**, making blocking behavior the exception rather than **the 
norm**.  
> **primitive** ADJECTIVE  
> If you describe something as primitive, you mean that it is very simple in style or very old-fashioned.  
> **paradigm** _noun_   
> (C2) a model of something, or a very clear and typical example of something.  
> **norm** _noun_  
> (C1) an accepted standard or a way of behaving or doing things that most people agree with.  
> **the norm**  
> (C1) a situation or type of behaviour that is expected and considered to be typcial.  
> Node.js 库使用非阻塞模式编写，这使得阻塞行为被视作异常而非规范。
In Node.js the new ECMAScrpt standards can be used without problems, as you don't have to wait for all your users to update their brosers - you are in charge of deciding which ECMAScript version to use by changing the Node.js version, and you can also enable specific experimental features by running Node.js with flags.  
#### A Vast Number of Libraries  
npm with its simple structure helped the ecosystem of Node.js proliferate, and now the npm registry hosts over 1,000,000 open source packages you can freely use.   
> **proliferate** _verb_  
> to increase a lot and suddenly in number.  
> **ecosystem** _noun_  
> all the living things in an area and the way thay affect each other and the environment.
#### Node.js Frameworks and Tools  
Node.js is a low-level platform. In order to make things easy and exciting for developers, thousands of libraries were built upon Node.js by the community.  
Many of those established over time as popular options. Here is a non-comprehensive list of the ones worth learning:  
- AdonisJS:  
- Egg.js:  
- Express:
- Fastify:  
- FeatherJS:  
- Gatsby:  
- hapi:  
- Loopback.io:  
- Meteor:  
- Micro:  
- NestJS:  
- Next.js:  
- Remix:  
- Sapper:  
- Socket.io:  
- Strapi:  
# Vue.js  
#### Introduction  
Vue is a  **progressive framework** for building user interfaces. Unlike other monolithic frameworks, Vue is designed from the ground up to be incrementally adoptable. The core
library is focused on the view layer only, and is easy to pick up and integrate with other libraries or existing projects. On the other hand, Vue is also perfectly capable of powering sophisticated Single-page Applications when used in combination with modern tooling and supporting libraries.
## HTML5  
The term HTML5 is essentially a buzzword that refers to a set of modern web technologies. This includes the HTML Living Standard, along with JavaScript APIs to enhance storage, multimedia, and hardware access.
> **buzzword** _noun_ a word or expression from a particular subject area that has become fashionable by being used a lot, especially on television and in the newspaper.   
> **essentially** _adverb_ (B2) relating to the most important characteristics or ideas of something.  
> **enhance** _verb_ (C1) to improve the quality, amount, or strength of something.
# JavaScript  
_High-level programming language_  
#### History  
**Creation at Netscape**   
> **-scape** _suffix_ used to form nouns referring to a wide view of a place, often one represented in a picture.  
> - landscape/ seExampleape/ cityscape  
The first web browser with a graphical user interface, Mosaic, was released in 1993. Accessible to non-technical people, it played a prominent role in the rapid growth of the 
nExampleent World Wide Web. The lead developers of Mosaic then founded the Netscape corporation, which released a more polished browser, Netscape Navigator, in 1994. This quickly
became the most-used.
During these formative years of the Web, web pages could only be static, lacking the capability for dynamic behavior after the page was loaded in the browser. There was a desire
in the hurgeoning web development scene to remove this limitation, so in 1995, Netscape decided to add a scripting language to Navigator. They pursued two routes to achieve this: collaborating with Sun Microsystems to embed the Java programming language, while also hiring Brendan Eich to embed the Scheme language.  
Netscape management soon decided that the best option was for Eich to devise a new language, with syntax similar to Java and less like Scheme or other extant scripting languages. Although the new language and its interpreter implementation were called LiveScript when first shipped as part of a Navigator beta in September 1995, the name was changed to JavaScript for the official release in December.
