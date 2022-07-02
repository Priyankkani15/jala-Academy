{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "561c3d1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "12\n",
      "12\n",
      "15\n",
      "12\n"
     ]
    }
   ],
   "source": [
    "# Define a static variable and access that through a class.\n",
    "\n",
    "class Python:\n",
    "# Access through class    \n",
    " staticVariable = 9 \n",
    "print(Python.staticVariable)\n",
    "\n",
    "#Change within an class\n",
    "Python.staticVariable = 12\n",
    "print(Python.staticVariable) # Gives 12\n",
    "\n",
    "#Access through an instance\n",
    "instance = Python()\n",
    "print(instance.staticVariable) # Gives 12\n",
    "\n",
    "#Change within an instance\n",
    "instance.staticVariable = 15\n",
    "print(instance.staticVariable) # Gives 15\n",
    "print(Python.staticVariable) #Gives 12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33844522",
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
