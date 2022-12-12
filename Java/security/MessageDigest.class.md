This MessageDigest class provides applications the functionality of a message digest algorithm, such as SHA-1 or SHA-256. Message digests are secure one-way hash functions that take arbitrary-sized data and output a fixed-length hash value.  
A MessageDigest object starts out initialized. The data is processed through it using the ```update``` methods. At any point ```reset``` can be called to reset the digest. Once all the data to be updated has been updated, one of the ```digest``` methods should be called to complete the hash computation.  
The digest method can be called once for a given number of updates. After digest has been called, the MessageDigest object is reset to its initialized state.  
Implementations are free to implement the Cloneable interface. Client applications can test cloneability by attempting cloning and catching the CloneNotSupportedException:
 ``` JAVA
 MessageDigest md = MessageDigest.getInstance("SHA-256");
     md.update(toChapter1);
     MessageDigest tc1 = md.clone();
     byte[] toChapter1Digest = tc1.digest();
     md.update(toChapter2);
     md.digest();
     ...etc.
 } catch (CloneNotSupportedException cnse) {
     throw new DigestException("couldn't make digest of partial content");
Note that if a given implementation is not cloneable, it is still possible to compute intermediate digests by instantiating several instances, if the number of digests is known in advance.  
Note that this class is abstract and extends from MessageDigestSpi for historical reasons. Application developers should only take notice of the methods defined in this MessageDigest class; all the methods in the superclass are intended for cryptographic service providers who wish to supply their own implementations of message digest algorithms.  
Every implementation of the Java platform is required to support the following standard MessageDigest algorithms:
- SHA-256  
These algorithms are described in the [MessageDigest section]() of the Java Cryptography Architecture Standard Algorithm Name Documentation. Consult the release documentation for your implementation to see if any other algorithms are supported.
See Also: DigestInputStream, DigestOutputStream  
Author:  
Benjamin Renaud  
Java提供的信息消化系统，提供三种常用算法。 MD5, SHA-1, SHA-256。
使用时分为基本的三个步骤：  
1. 选择一种算法初始化实例对象```MessageDigest md = MessageDigest.getInstance("SHA-256");```
2. 将需要加密的关键字更新到实例中```md.update(toChapter1);```
3. 调用消化方法，获取加密后的密文```byte[] toChapter1Digest = tc1.digest();```
