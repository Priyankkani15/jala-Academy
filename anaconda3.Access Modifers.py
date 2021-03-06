{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0cb519cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Public Data Member:  UG\n",
      "Protected Data Member:  5\n",
      "Private Data Member:  UG !\n",
      "Object is accessing protected member: 5\n"
     ]
    }
   ],
   "source": [
    "# super class\n",
    "class Super:\n",
    "     \n",
    "     # public data member\n",
    "     var1 = None\n",
    " \n",
    "     # protected data member\n",
    "     _var2 = None\n",
    "      \n",
    "     # private data member\n",
    "     __var3 = None\n",
    "     \n",
    "     # constructor\n",
    "     def __init__(self, var1, var2, var3): \n",
    "          self.var1 = var1\n",
    "          self._var2 = var2\n",
    "          self.__var3 = var3\n",
    "     \n",
    "    # public member function  \n",
    "     def displayPublicMembers(self):\n",
    "  \n",
    "          # accessing public data members\n",
    "          print(\"Public Data Member: \", self.var1)\n",
    "        \n",
    "     # protected member function  \n",
    "     def _displayProtectedMembers(self):\n",
    "  \n",
    "          # accessing protected data members\n",
    "          print(\"Protected Data Member: \", self._var2)\n",
    "      \n",
    "     # private member function  \n",
    "     def __displayPrivateMembers(self):\n",
    "  \n",
    "          # accessing private data members\n",
    "          print(\"Private Data Member: \", self.__var3)\n",
    " \n",
    "     # public member function\n",
    "     def accessPrivateMembers(self):    \n",
    "           \n",
    "          # accessing private member function\n",
    "          self.__displayPrivateMembers()\n",
    "  \n",
    "# derived class\n",
    "class Sub(Super):\n",
    "  \n",
    "      # constructor\n",
    "       def __init__(self, var1, var2, var3):\n",
    "                Super.__init__(self, var1, var2, var3)\n",
    "           \n",
    "      # public member function\n",
    "       def accessProtectedMembers(self):\n",
    "                 \n",
    "                # accessing protected member functions of super class\n",
    "                self._displayProtectedMembers()\n",
    "  \n",
    "# creating objects of the derived class    \n",
    "obj = Sub(\"UG\", 5 , \"UG !\")\n",
    " \n",
    "# calling public member functions of the class\n",
    "obj.displayPublicMembers()\n",
    "obj.accessProtectedMembers()\n",
    "obj.accessPrivateMembers()\n",
    " \n",
    "# Object can access protected member\n",
    "print(\"Object is accessing protected member:\", obj._var2)\n",
    " \n",
    "# object can not access private member, so it will generate Attribute error\n",
    "#print(obj.__var3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8390e0dc",
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
