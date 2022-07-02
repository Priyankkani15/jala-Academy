{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0f813ac9",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'HW.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [5]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# Write a program to read text file.\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m file1 \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mHW.txt\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mr\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m      4\u001b[0m data \u001b[38;5;241m=\u001b[39m file1\u001b[38;5;241m.\u001b[39mread()\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28mprint\u001b[39m(data)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'HW.txt'"
     ]
    }
   ],
   "source": [
    "# Write a program to read text file.\n",
    "\n",
    "file1 = open(\"HW.txt\",\"r\")\n",
    "data = file1.read()\n",
    "print(data)\n",
    "print()\n",
    "\n",
    "file2 = open(\"Blank.txt\",\"w\")\n",
    "str1 = 'Python'\n",
    "file2.write(str1)\n",
    "print()\n",
    "\n",
    "file3 = open(\"HW.txt\",\"r+\")\n",
    "print(file3.readline(11))\n",
    "print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc571f75",
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
