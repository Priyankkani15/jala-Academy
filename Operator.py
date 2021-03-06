{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3234617",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first number: 4\n",
      "Enter second number: 3\n",
      "The sum of 4 and 3 is 7.0\n",
      "The subtraction of 4 and 3 is 1.0\n",
      "The multiplication of 4 and 3 is 12.0\n",
      "The division of 4 and 3 is 1.3333333333333333\n",
      "The value of a is  2\n",
      "INCREMENTED FOR LOOP\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "\n",
      "DECREMENTED FOR LOOP\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "# Write a function for arithmetic operators(+,-,*,/)\n",
    "\n",
    "# Store input numbers:  \n",
    "num1 = input('Enter first number: ')  \n",
    "num2 = input('Enter second number: ')  \n",
    "  \n",
    "# Add two numbers  \n",
    "sum = float(num1) + float(num2)  \n",
    "# Subtract two numbers  \n",
    "min = float(num1) - float(num2)  \n",
    "# Multiply two numbers  \n",
    "mul = float(num1) * float(num2)  \n",
    "#Divide two numbers  \n",
    "div = float(num1) / float(num2)  \n",
    "# Display the sum  \n",
    "print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  \n",
    "# Display the subtraction  \n",
    "print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  \n",
    "# Display the multiplication  \n",
    "print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  \n",
    "# Display the division  \n",
    "print('The division of {0} and {1} is {2}'.format(num1, num2, div))  \n",
    "\n",
    "# Write a method for increment and decrement operators(++, --)\n",
    "\n",
    "# A sample use of increasing the variable value by one.\n",
    "a = 0\n",
    "a += 1\n",
    "a = a+1\n",
    "print('The value of a is ',a)\n",
    "# Use of increment operator, here start = 1,step = 1(by default) and stop = 5 \n",
    "print(\"INCREMENTED FOR LOOP\")\n",
    "for i in range(0, 5):\n",
    "   print(i)\n",
    "#Use of decrement operator, here start = 5, step = -1 and  stop = -1\n",
    "print(\"\\nDECREMENTED FOR LOOP\")\n",
    "for i in range(4, -1, -1):\n",
    "   print(i)\n",
    "\n",
    "# Write a program to find the two numbers equal or not.\n",
    "\n",
    "a = input('Enter first number: ')\n",
    "b = input('Enter second number: ')\n",
    "if a==b:\n",
    "    print(\"Both numbers are equal\")\n",
    "else:\n",
    "    print(\"Both numbers are not equal\")\n",
    "\n",
    "# Program for relational operators (<,<==, >, >==)\n",
    "\n",
    "a = 4\n",
    "b = 5\n",
    "print(a < b)  #This operator(<) returns True if the left operand is less than the right operand.\n",
    "print(a <= b) #This operator(<=)returns True if the left operand is less than or equal to the right operand.\n",
    "print(a > b)  #This operator(>) returns True if the left operand is greater than the right operand.\n",
    "print(a >= b) #This operator(>=)returns True if the left operand is greater than or equal to the right operand.   \n",
    "print(a == b) #This operator(==)returns True if both the operands are equal i.e. if both the left and the right operand are equal to each other.\n",
    "print(a != b) #This operator(!=)returns True if both the operands are not equal.\n",
    "\n",
    "# Print the smaller and larger number.\n",
    "\n",
    "a = float(input('Enter first number: '))\n",
    "b = float(input('Enter second number: '))\n",
    "#To print larger number\n",
    "if a > b: \n",
    "     print(a, \"is greater \")\n",
    "else:\n",
    "    print(b, \" is greater \")\n",
    "#To print samller number\n",
    "if a < b:\n",
    "     print(a, \"is smaller2 \")\n",
    "else:\n",
    "    print(b, \" is smaller \")         "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6f780e9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
