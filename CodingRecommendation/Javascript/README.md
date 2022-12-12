### 推荐使用  
#### [Mozilla推荐](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues)
``` JavExampleript
let array = new Uint32Array(10);
const s = window.crypto.getRandomValues(array).reduce((x,y) => x+y).toString(36);
### 不要使用  
``` JavExampleript
Math.random()
