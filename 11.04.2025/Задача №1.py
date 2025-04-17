input_data = input()
students = []
i = 0
while i < len(input_data):
    if input_data[i:i+8] == "student_":
        student_number = input_data[i+8:i+11]
        i += 11
        score = ""
        while i < len(input_data) and input_data[i].isdigit():
            score += input_data[i]
            i += 1
        students.append((student_number, int(score)))
    else:
        i += 1

max_score = max(score for _, score in students)

max_students = [student for student, score in students if score == max_score]

print('-'.join(max_students))