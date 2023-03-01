
subject1 ={'hour': '9:00',
           'teacher': 'Wirus',
           'subject':'microbiology'}

subject2 ={'hour': '12:00',
           'teacher': 'Kolba',
           'subject':'Chemistry'}

subject3 ={'hour': '14:00',
           'teacher': 'Olej',
           'subject':'math'}

subjectList = [subject1,subject2,subject3]

subjectDict = {}
for subject in subjectList:
    subjectDict[subject['subject']] = subject


print(subjectDict['math']['hour'])