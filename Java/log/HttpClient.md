Solution from [stack overflow](https://stackoverflow.com/questions/4915414/disable-httpclient-logging/49173217#49173217)
httpclient 会打印如下日志。 该log并未遵循类名的规则。所以直接设置类等级没有效果。
11:31:12 DEBUG httpclient.wire.header: - >> "POST /api/relay/gateway/findShipmentList HTTP/1.1[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "X-CEC-SIGN: b4650bcd0db662b5bbb3194eab29b73f[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "X-HW-ID: app_0000000000012395[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "X-CEC-ACCOUNT: doa[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "X-HW-APPKEY: QkozM3pKS2J6JiRWMTg5bQ==[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "X-CEC-DATE: 2021-11-18T11:31:09+0800[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "User-Agent: Jakarta Commons-HttpClient/3.1[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "Host: apigw-beta.Example.com[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "Content-Length: 64[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "Content-Type: application/json; charset=UTF-8[\r][\n]"
11:31:12 DEBUG httpclient.wire.header: - >> "[\r][\n]"
11:31:12 DEBUG httpclient.wire.content: - >> " {'shipmentStatus': '20,30,31','orderNo':'...'}"
这段日志的初始化来源于```org.apache.commons.httpclient.Wire```  
public static Wire HEADER_WIRE = new Wire(LogFactory.getLog("httpclient.wire.header"));
public static Wire CONTENT_WIRE = new Wire(LogFactory.getLog("httpclient.wire.content"));
而具体打印逻辑如下:
        for(int i = 0; i < headers.length; ++i) {
            String s = headers[i].toExternalForm();
            if (Wire.HEADER_WIRE.enabled()) {
                Wire.HEADER_WIRE.output(s);
            }
            conn.print(s, charset);
        }
```          
所以如果需要关闭这些日志， 那么对于 log4j.properties 的配置添加:  
``` properties
log4j.logger.httpclient.wire.header=WARN
log4j.logger.httpclient.wire.content=WARN
而对于 log4j2.xml 而言，配置添加：  
<logger name="org.apache" level="WARN" />
<logger name="httpclient" level="WARN" /> 
