# Stony Brook Script

A statically scoped, interpreted programming language built using PLY, a Yacc and Lex parser for Python. It supports variables, print statements, while loops, complex arithmetic, conditionals, heterogenous lists, as well as string concatenation and comprehensive error handling. This language was originally created for my CSE307 class at Stony Brook but has been expanded upon by me.

### Scope
Currently, all of a program must be contained in a "global" set of curly braces like so.

```
{
  ...
}
```

Additional scopes can be created within this global scope by adding additional curly braces, however there is currently no implementation for function handling. While this is currently limited, the plan is to add functions and create a more robust static language.

### Arthimetic

Expressions can be evaluated in either print statements or when being saved into a variable. Operations include the following:

```
+   : addition
-   : subtraction
*   : multiplication
/   : division (integer)
//  : division (float)
%   : modulo
**  : exponent
()  : parentheses
```

Integer and floats in the same expression are allowed but will always return a float. String concatenation is allowed ("hi" + " there" = "hi there") however using any other operations results in a syntax error. Typecasting is currently not implemented. 

### Data Types

Variables are instantiated by simply typing in the name and having it equal to a data type. Data types are integers, floats, strings, and lists. 

```
myInt = 3;
myFloat = 1.3445;
myString = "hello";
myList = [1,2,3];
```

Lists can be heterogenous, meaning that different data types can be stored in the same list.

```
myList = [1, 2.34, ["hey", "there"]];
```

Individual elements can be taken from these lists by indexing them. Indexes are 0 based.

```
myIndexedElement = [1,2,3][0]; # returns 1
```

The same can be done for strings.

```
myIndividualString = "hello"[1]; # returns "e"
```

Variables can also be used to compute new values. However, when one variable is set to be equal to another a new instance of that variable is created.

### Built in functions

There are a few builtin functions in Stony Brook Script. One of them is "while", which follows the standard form of a while loop. 

```
while (statement) {
  expr
}
```

There is also "print", which simply prints out to standard output.

```
print("Hello World"); # prints 'Hello World'
print(myVar); # will print any data type
print(expr); # expr is an arithmetic expression
```

### Conditionals

Currently, there are standard if, if-else, and else statements. These statements must be followed by curly braces, although single statement if statements are slated on the todo list. 

There are currently a number of different ways to evaluate a statement. Basic conditional operators include <, >, <=, >=, ==, but there's also boolean NOT, OR, AND, and IN.

## Built With

* [PLY](http://www.dabeaz.com/ply/) - lex and yacc parsing tools for Python

## Authors

* **Michael Brasile** - [mbrasile2](https://github.com/PurpleBooth)
