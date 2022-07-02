{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3656e6b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Triangle: I have 3 sides\n",
      "Quadrilateral: I have 4 sides\n",
      "Pentagon: I have 5 sides\n",
      "Hexagon: I have 6 sides\n"
     ]
    }
   ],
   "source": [
    "from abc import ABC, abstractmethod\n",
    " \n",
    "class Polygon(ABC): #base class / super class\n",
    " \n",
    "    @abstractmethod\n",
    "    def noofsides(self):\n",
    "        pass\n",
    " \n",
    "class Triangle(Polygon): #subclass\n",
    " \n",
    "    # overriding abstract method\n",
    "    def noofsides(self):\n",
    "        print(\"Triangle: I have 3 sides\")\n",
    " \n",
    "class Pentagon(Polygon): #subclass\n",
    " \n",
    "    # overriding abstract method\n",
    "    def noofsides(self):\n",
    "        print(\"Pentagon: I have 5 sides\")\n",
    " \n",
    "class Hexagon(Polygon): #subclass\n",
    " \n",
    "    # overriding abstract method\n",
    "    def noofsides(self):\n",
    "        print(\"Hexagon: I have 6 sides\")\n",
    " \n",
    "class Quadrilateral(Polygon): #subclass\n",
    " \n",
    "    # overriding abstract method\n",
    "    def noofsides(self):\n",
    "        print(\"Quadrilateral: I have 4 sides\")\n",
    " \n",
    "# Driver code\n",
    "# Creating the objects to call the abstract method.\n",
    "R = Triangle()\n",
    "R.noofsides()\n",
    " \n",
    "K = Quadrilateral()\n",
    "K.noofsides()\n",
    " \n",
    "R = Pentagon()\n",
    "R.noofsides()\n",
    " \n",
    "K = Hexagon()\n",
    "K.noofsides()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8e449e8",
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
