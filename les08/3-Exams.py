# Incomplete.
# ----------------------------------------------------------------------------------------------------------------------
class Student:
    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname
        self._exams = []

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_exams(self):
        return self._exams

    def set_firstname(self, firstname):
        self._firstname = firstname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def set_exams(self, exams):
        self._exams = exams

    def add_exam(self, exam):
        self._exams.append(exam)

    def total_score(self):

        return None


class Exam:
    def __init__(self, course, score_theory, score_practice):
        self._course = course
        self._score_theory = score_theory
        self._score_practice = score_practice

    def get_course(self):
        return self._course

    def get_score_theory(self):
        return self._score_theory

    def get_score_practice(self):
        return self._score_practice

    def set_course(self, course):
        self._course = course

    def set_score_theory(self, score_theory):
        self._score_theory = score_theory

    def set_score_practice(self, score_practice):
        self._score_practice = score_practice

    def calc_total_score(self):
        return self._score_practice + self._score_theory

    def calc_average_score(self):
        return self.calc_total_score() / 2


class Course:
    def __init__(self, name, points, weightfactor):
        self._name = name
        self._points = points
        self._weightfactor = weightfactor

    def get_name(self):
        return self._name

    def get_points(self):
        return self._points

    def get_weightfactor(self):
        return self._weightfactor

    def set_name(self, name):
        self._name = name

    def set_points(self, points):
        self._points = points

    def set_weightfactor(self, weightfactor):
        self._weightfactor = weightfactor


def main():

    # Examens
    igor = Student("Igor", "Wauters")

    bvp = Course("Beginselen van Programmeren", 6, 0.2)
    ex_bvp = Exam(bvp, 5, 13)
    print("Het examen voor BvP heeft een totale score van", ex_bvp.calc_total_score())
    igor.add_exam(ex_bvp)

    filo = Course("Filosofie", 3, 0.9)
    ex_filo = Exam(filo, 9, 13)
    print("Het examen voor Filo heeft een totale score van", ex_filo.calc_total_score())
    igor.add_exam(ex_filo)

    print("De totale score van " + igor.get_firstname()+" is: " + str(round(igor.total_score(), 2)) + " procent.")


# start the main method
main()
