# 10053  
fatal: unable to access ‘https://github.com/xxx/xxx/’:OpenSSL SSL_read: Connection was aborted, errno 10053  
Git默认限制推送的大小，运行命令更改限制大小即可  
git config --global http.postBuffer 524288000
git config --global http.sslVerify "false"
