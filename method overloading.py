{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "19736cda",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "Missing parentheses in call to 'print'. Did you mean print(parameter_A_that_Must_Be_String)? (2053151002.py, line 39)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [1]\u001b[1;36m\u001b[0m\n\u001b[1;33m    print parameter_A_that_Must_Be_String\u001b[0m\n\u001b[1;37m          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m Missing parentheses in call to 'print'. Did you mean print(parameter_A_that_Must_Be_String)?\n"
     ]
    }
   ],
   "source": [
    "class Addition:\n",
    "\t# first sum for 2 params\n",
    "\tdef my_sum(self, a, b):\n",
    "\t\treturn a + b\n",
    "\t\n",
    "\t# second overloaded sum for 3 params\n",
    "\tdef my_sum(self, a, b, c):\n",
    "\t\treturn a + b + c\n",
    "obj = Addition()\n",
    "obj.my_sum(value1, value2)  # for first func\n",
    "obj.my_sum(value1, value2, value3)  # for second func\n",
    "print(obj.my_sum(3, 4))\n",
    "print(obj.my_sum(3, 4, 5))\n",
    "\n",
    "from multidispatch import dispatch  # importing the module\n",
    "\n",
    "@dispatch(int, int)  # using the dispatch decorator to define two parameters as int\n",
    "def mul(a, b):\n",
    "    return a * b\n",
    "\n",
    "@dispatch(int, int, int)  # defining 3 parameters as int\n",
    "def mul(a, b, c):\n",
    "    return a * b * c\n",
    "\t\n",
    "@dispatch(float, float, float)  # defining 3 parameters as float\n",
    "def mul(a, b, c):\n",
    "    return a * b * c\n",
    "print(mul(2.1, 3.4, 5.6))\n",
    "print(mul(3, 4))\n",
    "print(mul(2, 3, 4))\n",
    "\n",
    "class MyClass:\n",
    "    \"\"\"\"\"\"\n",
    "\n",
    "    #----------------------------------------------------------------------\n",
    "    def init(self):\n",
    "        \"\"\"Constructor\"\"\"\n",
    "    def my_method(self,parameter_A_that_Must_Be_String):\n",
    "        print parameter_A_that_Must_Be_String\n",
    "\n",
    "    def my_method(self,parameter_A_that_Must_Be_String,parameter_B_that_Must_Be_String):\n",
    "        print parameter_A_that_Must_Be_String\n",
    "        print parameter_B_that_Must_Be_String\n",
    "\n",
    "    def my_method(self,parameter_A_that_Must_Be_String,parameter_A_that_Must_Be_Int):\n",
    "        print parameter_A_that_Must_Be_String"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3d5da7d",
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
