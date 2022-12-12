# Double colon (::) operator in Java  
also known as method reference operator.   
This operator is used to call a method by referring to it with the help of its class directly. They hehave exactly as the lambda expressions.
The only difference it has from lambda expressions is that this uses direct reference to the method by name instead of providing a delegate to the method.  
> :: is an operator  
> -> is an expression  
    public static void main(String[] args) {
        Stream<String> stream = Stream.of("Greeting", "Bllose", "Nice", "To", "Meet", "You");
        stream.forEach(s -> System.out.println(s));
        System.out.println("=======================");
        stream = Stream.of("Next", "Time", "See", "You", "Again", "!");
        stream.forEach(System.out::println);
