# Overview
Provide brief answers to the knowledge-question worksheet.

## Answers

1. Briefly explain what is modular programming
>JS: Modular programming is the programming technique of splitting the functionality of program into multiple, 
independent modules. Each module contains a separate and specific functionality of the code.

2. How can you import only a specific function or class from a module in Python? What is the syntax for this?
>JS: To import a specific function or class from a module in Python, use 
> 
> '_from_' ... '_import_' ... 
> 
> In the created tic_tac_toe program, an example is 
> 
>_from board import Board_
> 
>(meaning, from the board.py file, import the Board class).

3. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference? Justify your answer.
>JS: Parameter-passing in Python refers to when an argument, or input, is giving for function when it is called. The argument is then
> used by the function. In Python, the parameter-passing is either similar to pass-by-value or pass-by-reference depending on what
> object is being passed into the function. When an object such as a string or integer is passed, Python will act using pass-by-value, but
> when passing a mutable object like a list or dictionary, Python will perform pass-by-reference type parameter-passing. When a pass-by-value is passed,
> the original parameter is not modified within the function, however a list can be. This is why Python can act as both pass-by-value
> or pass-by-reference.

4. Given the following Python code, what will be the output and why?

    ```python
    def modify_list(list_):
        list_.append("new")
        list_ = ["completely", "new"]

    items = ["original"]
    modify_list(items)
    print(items)
    ```

>JS: The output for the code is:
> 
> ['original', 'new'].
> 
>JS: This is due to the behavior of Python and its handling of parameter-passing. In this example code, the *items* list contains "original",
> and is passed into the function. Within the function, *new* is appended to the list object. The list itself is then redefined with variables
> *completely* and *new*. This however does not affect the list outside the function, even if it passed through it. This can be demonstrated
> by adding *print(list_)* within the function, which shows that it prints ['original', 'new'].

5. In Python, even though variables created within a function are local, there are still situations where you can modify data outside the scope with a local variable. Explain this anomaly and relate it to both mutability and pass by reference.
>JS: This is briefly explained in the previous answer. Python can modify data outside the function, only if it is a mutable variable, such as
> a list or dictionary. This is pass-by-reference mechanism.
> 
6. List two benefits of modular coding approaches. How do these benefits assist in the development of medium-sized applications?
>JS: Two benefits of modular coding approaches are maintainability and reusability. The benefits of these approaches assist in medium-sized
> applications is that the code is more manageable to read and modify for the programmer. When code is modular, it may be easier to reuse
> the code elsewhere within the application e.g., copy a similar function and modify, which is a more efficient approach.