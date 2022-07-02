{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e919b21b",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'student'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Input \u001b[1;32mIn [1]\u001b[0m, in \u001b[0;36m<cell line: 12>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      8\u001b[0m       \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mName: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mname\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124mGender: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mgender\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124mYear: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39myear\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     11\u001b[0m \u001b[38;5;66;03m# faculty.py\u001b[39;00m\n\u001b[1;32m---> 12\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mFaculty\u001b[39;00m:\n\u001b[0;32m     14\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21minit\u001b[39m(\u001b[38;5;28mself\u001b[39m, faculty):\n\u001b[0;32m     15\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mname \u001b[38;5;241m=\u001b[39m faculty[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m'\u001b[39m]\n",
      "Input \u001b[1;32mIn [1]\u001b[0m, in \u001b[0;36mFaculty\u001b[1;34m()\u001b[0m\n\u001b[0;32m     19\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mName: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mname\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124mSubject: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msubject\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     20\u001b[0m     \u001b[38;5;66;03m# testing.py\u001b[39;00m\n\u001b[0;32m     21\u001b[0m \u001b[38;5;66;03m# importing the Student and Faculty classes from respective files\u001b[39;00m\n\u001b[1;32m---> 22\u001b[0m     \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mstudent\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Student\n\u001b[0;32m     23\u001b[0m     \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mfaculty\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Faculty\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'student'"
     ]
    }
   ],
   "source": [
    "class Student:\n",
    "    def init(self, student):\n",
    "        self.name = student['name']\n",
    "        self.gender = student['gender']\n",
    "        self.year = student['year']\n",
    "\n",
    "def get_student_details(self):\n",
    "      return f\"Name: {self.name}\\nGender: {self.gender}\\nYear: {self.year}\"\n",
    "\n",
    "\n",
    "# faculty.py\n",
    "class Faculty:\n",
    "\n",
    "    def init(self, faculty):\n",
    "        self.name = faculty['name']\n",
    "        self.subject = faculty['subject']\n",
    "\n",
    "    def get_faculty_details(self):\n",
    "        return f\"Name: {self.name}\\nSubject: {self.subject}\"\n",
    "    # testing.py\n",
    "# importing the Student and Faculty classes from respective files\n",
    "    from student import Student\n",
    "    from faculty import Faculty\n",
    "\n",
    "# creating dicts for student and faculty\n",
    "student_dict = {'name' : 'John', 'gender': 'Male', 'year': '3'}\n",
    "faculty_dict = {'name': 'Emma', 'subject': 'Programming'}\n",
    "\n",
    "# creating instances of the Student and Faculty classes\n",
    "student = Student(student_dict)\n",
    "faculty = Faculty(faculty_dict)\n",
    "\n",
    "# getting and printing the student and faculty details\n",
    "print(student.get_student_details())\n",
    "print()\n",
    "print(faculty.get_faculty_details())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa3b0247",
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
