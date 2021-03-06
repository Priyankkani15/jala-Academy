{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6c2098d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Second element =  2\n",
      "An error occurred\n",
      "\n",
      "Both Equal\n",
      "\n",
      "Can't divide by zero\n",
      "This is always executed\n"
     ]
    }
   ],
   "source": [
    "a = [1, 2, 3]\n",
    "try:\n",
    "    print (\"Second element = \",a[1])\n",
    " \n",
    "    # Throws error since there are only 3 elements in array\n",
    "    print (\"Fourth element = \",a[3])\n",
    "    \n",
    "except:\n",
    "    print (\"An error occurred\")\n",
    "\n",
    "print()\n",
    "\n",
    "b = [3,2,1]\n",
    "try:\n",
    "    a == b\n",
    "except:\n",
    "    print(\"They are not equal\")\n",
    "else:\n",
    "    print(\"Both Equal\") \n",
    "\n",
    "print()\n",
    "\n",
    "try:\n",
    "    k = 5/0\n",
    "    print(k)\n",
    "except ZeroDivisionError:\n",
    "    print(\"Can't divide by zero\")\n",
    "finally:\n",
    "    print('This is always executed')                 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8337dd43",
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
