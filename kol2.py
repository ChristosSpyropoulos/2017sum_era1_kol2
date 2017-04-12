import json


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def make_list_float(this_score_list):
    new_list = []
    for item in this_score_list:
        new_list.append(float(item))
    return new_list


def provide_exams_for_student(student_name,course_name):
    exams_of_the_student = []
    for this_exam in range(2):
        exam_record = raw_input("Student: "+student_name+" ,Course: "+course_name+" record No: "+str(this_exam+1)+": ")
        exams_of_the_student.append(exam_record)
    return exams_of_the_student


def provide_student_data(course_name):
    students = {}
    for this_student in range(2):
        student_name = raw_input("Student No: "+str(this_student+1)+" in course: "+course_name+", Name: ")
        students[student_name] =  provide_exams_for_student(student_name,course_name)
    return students

classroom = {}
for this_course in range(2):
    course_name = raw_input("Provide Course Name: ")
    classroom[course_name] = provide_student_data(course_name)

print classroom
print "file myjsonfile_output.json has been updated!"

json_obj = json.dumps(classroom)
myfile = open("myjsonfile_output.json","w")
myfile.write(json_obj)
myfile.close()

a = raw_input("Press any button to proceed to the second part of the exercise ( reading from .json file ):")
myfile = open("myjsonfile_input.json","r")
json_obj = myfile.read()
myfile.close()
print json_obj
json_obj_dict = json.loads(json_obj)

counter_in_class = 0
sum_in_class = 0
for each_subject in json_obj_dict:
    this_subject = json_obj_dict[each_subject]
    print each_subject
    counter_in_subject = 0
    sum_in_subject = 0
    for each_student in this_subject:
        this_score_list = this_subject[each_student]
        this_score_list = make_list_float(this_score_list)
        this_student_mean = mean(this_score_list)
        print each_student+":"+str(this_student_mean)
        counter_in_subject +=1
        sum_in_subject += this_student_mean
        counter_in_class += 1
        sum_in_class += this_student_mean
    avg_in_subject = float(sum_in_subject) / counter_in_subject
    print "The avg of this subject is: "+str(avg_in_subject)
avg_in_class = float(sum_in_class) / counter_in_class
print "The avg of the class is: "+str(avg_in_class)
print "Data was read from the file 'myjsonfile_input.json', you can try change the data"
