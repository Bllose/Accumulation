<template>
    Next we need to bind the method to our <form> element's submit event handler. 
    Much like how Vue uses the v-bind syntax for binding attributes, Vue has a special directive for event handling: v-on. 
    The v-on directive works via the v-on:event="method" syntax. 
    And much like v-bind, there’s also a shorthand syntax: @event="method". 
    We'll use the shorthand syntax here for consistency. 
    Add the submit handler to your <form> element like so:  
    <form @submit="onSubmit">
    在当前设置情况下， 我们点击以下 Add， 程序会实际上调用后台（即调用地址：http://10.242.118.143:8080/?new-todo=11）， 并且刷新页面。 这是它的默认行为。  
    为了改变事件的这种默认行为， Vue提供了一个对应的格式，叫做 event modifiers，就是在 event 后面加个 点， 然后跟上需要改变的行为， 就像: @event.modifier  
    就我们目前的需求就是要关闭事件的默认行为， 使用.prevent, 这相当于 vanilla JavaScript 中的Event.preventDefault()  
    所以将 form 标签修改为：<form @submit.prevent="onSubmit">
<form @submit.prevent="onSubmit">
    <!-- 
        While we're here, there's one more semantic and styling change we can make. 
        Since our form denotes a specific section of our page, it could benefit from an <h2> element.
        The label, however, already denotes the purpose of the form. To avoid repeating ourselves, let's wrap our label in an <h2>.  
        label 作为一个特定的标签， 有其特定作用。 但是如果直接给label增加参数：class="label-wrapper" , 并不能被选择器 .label-wrapper 渲染（为什么？）。  
        通过 h2 标签的包装， 可以将对h2的渲染传递到 label标签的内容。
    <h2 class="label-wrapper">
        <label for="new-todo-input">
            What needs to be done?
        </label>
    </h2>
    <!-- 
        We now need some way to attach the value of the new-todo-input <input> field to the label field. 
        Vue has a special directive for this: v-model. 
        v-model binds to the data property you set on it and keeps it in sync with the <input>. 
        v-model works across all the various input types, including check boxes, radios, and select inputs. 
        To use v-model, you add an attribute with the structure v-model="variable" to the <input>. 
        So in our case, we would add it to our new-todo-input field as seen below. 
        Do this now:
    <input type="text" id="new-todo-input" name="new-todo" autocomplete="off" v-model.lazy.trim="label" class="input__lg" />
    <!-- 
        同样的， 针对v-model也可以改变它的默认行为。 原本，v-model仅仅将input输入的内容绑定到参数 label上。 
        现在增加一个 .trim 使得它会将输入内容前后的空格去掉后再绑定到参数 label 上。  
        另外， 针对 input 标签， Vue会在用户每次键入字符时都会将值绑定到参数label上。但是我们当前的需求并不需要如此频繁赋值。
        此时，我们增加.lazy 以修改这个默认的行为， 使得它只有在脱离焦点或者点击提交时才会被赋值到参数label上。
        故最终将 v-model="label" 修改为：v-model.lazy.trim="label"
    <button class="btn btn__primary btn__lg" type="submit">
        Add
    </button>
</template>
export default {
    methods: {
        onSubmit() {
            if (this.label === "") {
                return;
            }
            this.$emit("todo-added", this.label, "MoreInformation");
            this.label = "";
        }
    data() {
        return {
            label: ""
        }
</script>
