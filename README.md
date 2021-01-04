# CS50x_Readability
A program that computes the approximate grade level needed to comprehend some text.
The program is based on on Harvard's CS50's Introduction to Computer Science 2021 OpenCourseWare's problem set-2.

The program computes the Coleman-Liau index which determines the US grade level needed to understand the text.
The formula is:
    index = 0.0588 * L - 0.296 * S - 15.8
Here, L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

The program takes in text as input and outputs appropriate grade level based on the computed index.
If the index number is 16 or higher, the program outputs "Grade 16+". 
If the index number is less than 1, the program outputs "Before Grade 1".
In other cases, the Grade corresponding to the index is printed .

References:
1. https://www.edx.org/course/cs50s-introduction-to-computer-science
2. https://cs50.harvard.edu/x/2021/psets/2/readability/
