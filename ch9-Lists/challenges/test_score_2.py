def get_test_score(answer_sheet, student_answers):
    right_answer_count = 0
    student_name = student_answers[0]
    del student_answers[0]

    for i in range(0,len(answer_sheet)):
        if answer_sheet[i] == student_answers[i]:
            right_answer_count += 1
    return student_name,(right_answer_count*100)/len(answer_sheet)