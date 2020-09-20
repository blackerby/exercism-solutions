class Garden:
    PLANTS = {
        'V': 'Violets',
        'R': 'Radishes',
        'C': 'Clover',
        'G': 'Grass'
    }

    STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=STUDENTS):
        row_one, row_two = diagram.split()
        grouped_by_students = zip(*[iter(row_one)] * 2, *[iter(row_two)] * 2) 
        self.student_plants = dict(zip(sorted(students), grouped_by_students)) 

    def plants(self, student):
        return [Garden.PLANTS[char] for char in self.student_plants[student]]