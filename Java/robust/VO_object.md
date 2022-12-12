# 域为对象时  
典型的， 当VO对象中保存着一个日期对象时， 那么用户在调用 get/set 方法获取或修改其值时， 应该确保不会跨越我们设想的范围。
比如， 针对```Date lastUpdateTime;```域，我们只提供了get方法，那就意味着，我们不希望被使用者修改该字段。
但是，如果我们仅仅是一个通用的get方法 - 直接```return lastUpdateTime;```那么这种情况下，使用者是可以修改此对象的。也就相当于可以调用```set```方法。  
为了避免这种风险， 我们在针对对象操作时，不要简单粗暴地 GET/SET。
针对```Date```对象操作时一个样例:  
public Date getBirthDate(){
    return new Date(birthDate.getTime());// essentially a clone
public void setBirthDate(Date birthDate){
   this.updateTime = (Date) birthDate.clone();// essentially a clone
针对时间戳```Timestamp```对象时，操作样例:
public Timestamp getCreateTime()
    // 不判空 会报 UWF_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR: Low
    if (null != this.createTime)
        return (Timestamp) this.createTime.clone();
    return null;
public void setCreateTime(Timestamp createTime)
    // 不判空 会报 UWF_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR: Low
    if (null != createTime)
        this.createTime = (Timestamp) createTime.clone();
        this.createTime = null;
针对数组 array 的操作样例:
