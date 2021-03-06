{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dcc7bb6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Display Inside class A \n",
      "Print Inside class B\n",
      "Show Inside class C \n"
     ]
    }
   ],
   "source": [
    "class A():  \n",
    "    def display(dp):\n",
    "        print(\"Display Inside class A \")\n",
    " # class A show method    \n",
    "    def show(self):\n",
    "        print(\"Show Inside class A\")\n",
    "    \n",
    "# Inherited or Sub class (Note A in bracket) \n",
    "class B (A): \n",
    "    def print(pt):\n",
    "        print(\"Print Inside class B\")    \n",
    "    # class B show method\n",
    "    def show(self):\n",
    "        print(\"Show Inside class B\")\n",
    "    \n",
    "# Inherited or Sub class (Note B in bracket) \n",
    "class C (B): \n",
    "          \n",
    "    # class C show method\n",
    "    def show(self):\n",
    "        print(\"Show Inside class C \")         \n",
    "    \n",
    "# Driver code \n",
    "s = A()\n",
    "s.display()\n",
    "k= B()\n",
    "k.print()\n",
    "g = C()   \n",
    "g.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9de50af7",
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
