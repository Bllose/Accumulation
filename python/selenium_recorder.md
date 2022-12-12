# invalid cookie domain
当我们尝试给 driver 添加 cookie 时报错：invalid cookie domain  
    "value": {
        "error": "invalid cookie domain",
        "message": "invalid cookie domain\\n  (Session info: chrome=104.0.5112.101)",
        "stacktrace": "Backtrace:\\n\\tOrdinal0 [0x00AF5FD3+2187219]\\n\\tOrdinal0 [0x00A8E6D1+1763025]\\n\\tOrdinal0 [0x009A3D40+802112]\\n\\tOrdinal0 [0x00A0B318+1225496]\\n\\tOrdinal0 [0x009ECB8C+1100684]\\n\\tOrdinal0 [0x009FCFC2+1167298]\\n\\tOrdinal0 [0x009EC9A6+1100198]\\n\\tOrdinal0 [0x009C6F80+946048]\\n\\tOrdinal0 [0x009C7E76+949878]\\n\\tGetHandleVerifier [0x00D990C2+2721218]\\n\\tGetHandleVerifier [0x00D8AAF0+2662384]\\n\\tGetHandleVerifier [0x00B8137A+526458]\\n\\tGetHandleVerifier [0x00B80416+522518]\\n\\tOrdinal0 [0x00A94EAB+1789611]\\n\\tOrdinal0 [0x00A997A8+1808296]\\n\\tOrdinal0 [0x00A99895+1808533]\\n\\tOrdinal0 [0x00AA26C1+1844929]\\n\\tBaseThreadInitThunk [0x75B5FA29+25]\\n\\tRtlGetAppContainerNamedObjectPath [0x773C7A7E+286]\\n\\tRtlGetAppContainerNamedObjectPath [0x773C7A4E+238]\\n"
[MDN Web Docs - WebDriver - Invalid cookie domain](https://developer.mozilla.org/en-US/docs/Web/WebDriver/Errors/InvalidCookieDomain) 有对上面异常进行详细说明。  
大体的意思就是添加的cookie不允许与当前网址所属 host 属于不同的 domain.  
所以假如我们需要添加一个cookie， 这个cookie 的host属于 ```.Example.com```, 那么我们就应该让WebDriver打开的网页也是类似于 ```http://www.Example.com```, ```https://login.Example.com```的网址。 这样才是添加合法的 cookie.
