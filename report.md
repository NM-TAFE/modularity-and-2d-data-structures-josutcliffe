### Step 7: Written Report

Once you have completed your refactoring, write a brief report addressing the following:

1.  Justification for your refactoring decisions.
>JS: There were a number of reasons to refactor the original tic_tac_o_oh.py code. It was a monolithic code block, that included a number
> of hardcoded variables/values, and all the functionality is contained in the one code block. This may seem like a good idea, however
> it makes it difficult to maintain, in the sense that the code is not intuitive to read and debug. Another reason to refactor is
> that the code is challenging to add additional features, such as user quality of life options (e.g., exiting at any time). To
> add extra features would require significant effort and time to include.

2.  The challenges you would have faced maintaining and testing the original monolithic code.
>JS: Challenges in maintaining and testing the original code would include that it is likely difficult to add or modify features in the code.
> For example, the hardcoded values limit the adaptability and re-usability of the code, in that we wanted to change the hardcoded
> values (e.g., grid/board size), it would require a big effort as a number of other conditions are dependent on the hardcoded values
> (such as the winning conditions). Testing is also difficult in the original code as, due to the monolithic style, it is challenging
> to test individual components within the code. Also, adding tests to the code block will make it even larger and harder to read
> whereas it would be better practice to keep these tests separate from the main code.

3. How you would modify your refactored code to handle a custom-sized tic-tac-toe game (larger than 3x3), and how this implementation would be easier to handle than in the original code.
>JS: The new modular implementation of the code can manage different board sizes as it uses a data structure to build the grid,
> as opposed to a set hard-coded grid as in the original codeblock. With the refactored code, it should be able to take a desired
> board size as an argument when generating an instance of the Board, and the refactored code should be able to handle this.
> The game logic would allow for changes in the board size as *_has_winner_* is not hard-coded like the original code, e.g.,
> it is adaptive. It may need some tweaking but would require far less effort than re-writing the original code.
