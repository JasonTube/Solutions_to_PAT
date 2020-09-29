class student:
    def __init__(self,name,id,score):
        self.name = name
        self.id = id
        self.score = int(score)
        
if __name__ == "__main__":
    n = int(input())
    students = []
    for i in range(0,n):
        name, id, score = input().split(" ")
        students.append(student(name,id,score))
    best_student = students[0]
    worst_student = students[0]
    for j in range(1,n):
        if students[j].score > best_student.score:
            best_student = students[j]
        elif students[j].score < worst_student.score:
            worst_student = students[j]
            
    print(best_student.name + " " + best_student.id)
    print(worst_student.name + " " + worst_student.id)
