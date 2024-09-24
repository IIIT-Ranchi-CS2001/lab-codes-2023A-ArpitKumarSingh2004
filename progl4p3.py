
course_codes = ["CS1001", "CS1002", "CS1003", "CS1004", "CS1005"]
course_names = ["Python", "Java", "C++", "Data Structures", "Algorithms"]

course_list = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]


print(course_list)