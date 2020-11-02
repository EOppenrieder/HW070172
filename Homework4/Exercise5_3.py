#A program to convert exam scores into grades

def main():
        n = (eval(input("Enter a number score: ")))
        grade = []
        for x in range(0, 60):
            grade.append("F")
        for x in range(60, 70):
            grade.append("D")
        for x in range(70, 80):
            grade.append("C")
        for x in range(80, 90):
            grade.append("B")
        for x in range(90, 300):
            grade.append("A")

        #print results 
        print(grade[n])

main()
