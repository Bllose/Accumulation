# [Using Postman Interceptor](https://go.pstmn.io/docs-interceptor-capture-cookies)  
Postman Interceptor is a Chrome extension that acts as a browser companion to the Postman Desktop app.
Interceptor enables you to capture network requests and cookies directly from a Chrome browser.  
Once Interceptor is running in Chrome, you can start a debug session, which is a timebound session of traffic capture.
You can start, pause, and stop an interceptor debug session, then later start another one.
Each debug session is logged at the history tab, and displays the total session time and all traffic captured.
From the logged session, you can send requests and responses to a collection and save cookies to the Postman cookie jar.  
> You can also use Postman Interceptor to automatically sync cookies from a Chrome browser to the Postman cookie jar. 
> Learn more about [syncing cookies.](https://learning.postman.com/docs/sending-requests/capturing-request-data/syncing-cookies)  
var jsonData = pm.response.json();
pm.environment.set("Authorization",jsonData.result);
pm.environment.set("IAuthorization","4C05F8E2F54BF94740E5905ADCEE155000FF426FAE2983F99AE8BEE95D9FDC09");
//pm.environment.set("ServiceType","publicservicce");
