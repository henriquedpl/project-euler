import unittest
import importlib

from answers import get_answers

ANSWERS = get_answers()


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution_modules = dict()
        self.answers = ANSWERS
        for problem_id in self.answers:
            self.solution_modules[problem_id] = importlib.import_module(problem_id)

    def get_answer(self, problem_id):
        return getattr(self.solution_modules[problem_id], f"solution{problem_id}")()

    def testProblem001(self):
        problem_id = "001"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem002(self):
        problem_id = "002"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem003(self):
        problem_id = "003"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem004(self):
        problem_id = "004"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem005(self):
        problem_id = "005"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem006(self):
        problem_id = "006"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem007(self):
        problem_id = "007"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem008(self):
        problem_id = "008"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem009(self):
        problem_id = "009"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem010(self):
        problem_id = "010"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem011(self):
        problem_id = "011"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem012(self):
        problem_id = "012"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem013(self):
        problem_id = "013"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem014(self):
        problem_id = "014"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem015(self):
        problem_id = "015"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem016(self):
        problem_id = "016"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem017(self):
        problem_id = "017"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem018(self):
        problem_id = "018"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem019(self):
        problem_id = "019"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem020(self):
        problem_id = "020"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem021(self):
        problem_id = "021"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem022(self):
        problem_id = "022"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem023(self):
        problem_id = "023"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem024(self):
        problem_id = "024"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem025(self):
        problem_id = "025"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem026(self):
        problem_id = "026"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem027(self):
        problem_id = "027"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem028(self):
        problem_id = "028"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem029(self):
        problem_id = "029"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem030(self):
        problem_id = "030"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem031(self):
        problem_id = "031"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem032(self):
        problem_id = "032"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem033(self):
        problem_id = "033"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem034(self):
        problem_id = "034"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem035(self):
        problem_id = "035"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem036(self):
        problem_id = "036"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem037(self):
        problem_id = "037"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem038(self):
        problem_id = "038"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem039(self):
        problem_id = "039"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem040(self):
        problem_id = "040"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem041(self):
        problem_id = "041"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem042(self):
        problem_id = "042"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem043(self):
        problem_id = "043"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem044(self):
        problem_id = "044"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem045(self):
        problem_id = "045"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem046(self):
        problem_id = "046"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem047(self):
        problem_id = "047"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem048(self):
        problem_id = "048"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem049(self):
        problem_id = "049"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem050(self):
        problem_id = "050"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem052(self):
        problem_id = "052"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem053(self):
        problem_id = "053"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem054(self):
        problem_id = "054"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem056(self):
        problem_id = "056"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem057(self):
        problem_id = "057"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem058(self):
        problem_id = "058"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem062(self):
        problem_id = "062"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem063(self):
        problem_id = "063"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem065(self):
        problem_id = "065"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem067(self):
        problem_id = "067"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem069(self):
        problem_id = "069"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem071(self):
        problem_id = "071"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem072(self):
        problem_id = "072"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem076(self):
        problem_id = "076"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem079(self):
        problem_id = "079"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem081(self):
        problem_id = "081"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem092(self):
        problem_id = "092"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem097(self):
        problem_id = "097"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem098(self):
        problem_id = "098"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem099(self):
        problem_id = "099"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem112(self):
        problem_id = "102"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))


if __name__ == "__main__":
    unittest.main()
