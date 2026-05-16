# CryptoLang v1.0

**CryptoLang** is a language made for handling different data types to return them in a specific state.
## The Code
CryptoLang's syntax is really easy. Variables and user input are a very important part of the code.

### Define Variables
There are **two** types of variables: _user defined_ and  _code defined_.

**User Defined**
Are defined using the following syntax:
``Varname -> "Whatwill be asked"``
> Result will be always stored as a int after being converted to string! ("A" -> 65)

**Code Defined**
These variables aren't decided by the user, but by the programmer, to define base values, for example.
The syntax is the following:
``Varname <- "Value"``
> Will be converted to int if it's a string.

### Create Variables
There is, actually, another variable type, which are _declarated variables_.
These variables, don't have a value (int: 0) until you give them one. Useful for process variables, for example.
To create a declarated variable, we use:
``varname;``
> Very important the semicolon!

### Base
Base variables are used to define where all the process will happen and be saved. If the base is, for example a **previously created** variable called ``process``, every step of our algorithm will be saved at ``process``.
Base is defined using:
``BASE varname``

### Bindings
This is probably the most important thing of the language. When you bind two variables, _a_, and _b_, when every instruction is runned, _b_ will have the value of _a_.
To create a new binding, use
``BIND a b``
### Output
To output a value or variable, we have to define the output format, being actually or ``STR``, ``INT`` or ``BIN``.
More types incoming.
Use this to output:
``OUT varname TYPE``

### Echo
To print a **literal STRING** use:
``ECHO "message"``

### Adds: modules
You can create your own modules using the guide.
To add a module, use:
``ADD module``
and, to execute a function it has, use,
``module.funcname.[args]``

The result of the function will be saved in the ``base`` variable.

## Creating your modules!

There are two parts of a module: _functions_ and _run function_.
The _functions_ part if very straighforward: just define them!
```python
def sum(A, B):
	return A + B
	
# Rest of the functions
```
And for the _run function_, we use a match case. The run function is made to ensure that every function can be called independently of its number of arguments.
```python
def  run(n, array):
	args  = [int(i) for  i  in  array]

	a  =  args[0]
	b  =  args[1]

	match  n:
		case  "sum":
			result  =  sum(a, b)
			
	return  result
```
## Example Code

This code returns the XOR of "A" and "B":
```
// Find all used modules in the add/ folder
ADD basic

a <- "A"
b <- "B"
process;
BASE process
basic.XOR.[a, b]
OUT process INT
// OUTPUT: 3
```
