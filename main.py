import student

def main():
    student1 = student.Student("Enping", 121212)
    student2 = student.Student("John", 111111)
    transfer_classes = ["Comp151", "Comp152", "Comp206",
                        "Comp250", "Math130", "Math120",
                        "Math151", "Chem131"]
    student1.transfer_classes(transfer_classes)
    if student2.can_graduate():
        print(f"{student1.name} can graduate")
    else:
        print("Not enough classes to graduate yet")
main()
