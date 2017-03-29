#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

class Student(object): 
	def __init__(self, name, surname, exam_scores_list, class_score_list):
		self.name = name
		self.surname = surname
		self.exam_scores = exam_scores_list
		self.class_scores = class_score_list
		self.average_exam_scores = mean(exam_scores_list)
		self.average_class_scores = mean(class_score_list)

	
xristos = Student("xristos","spyropoulos",[1,1,2],[4,6,6,7])
print xristos.average_exam_scores
print xristos.average_class_scores
