# https://docs.pytest.org/en/latest/getting-started.html
# https://code.visualstudio.com/docs/python/unit-testing
# command pallette 'Python: Discover Unit Tests'
import schedule_formatter
import unittest
import os


class Test_ScheduleFormatter(unittest.TestCase):
    def setup(self):
        base_folder = os.path.dirname(__file__)
        self.filename = os.path.join(base_folder, "test_sample.txt")
        file = open(self.filename, w)
        file.write(
            "7:00 AM CT	9:00 PM	IT Maintenance	MDWY - 22	Information Technology Services\\n7:00 AM CT	9:00 PM	IT Maintenance	MDWY - 27	Information Technology Services\\n7:00 AM CT	9:00 PM	IT Maintenance	MDWY - 370-CC	Information Technology Services\\n7:30 AM CT	10:00 AM	IT Replacement project	MDWY - 8	Information Technology Services\\n5:00 PM CT	8:00 PM	EDU-383-01 Information Technology for K-12 Education	MDWY - M	School of Urban Education(UED)\\n6:00 PM CT	9:50 PM	PSYC-309-01 Cognitive Psychology	MDWY - 104	Col of Community Studies & Public Affairs (CSPA)\\n6:00 PM CT	9:50 PM	MATH-215-02 Discrete Mathematics	MDWY - 107	College of Sciences(COS)\\n6:00 PM CT	8:40 PM	WRIT-231-01 Writing II	MDWY - 13	College of Liberal Arts (CLA)\\n6:00 PM CT	9:35 PM	MPNA-690-01 Public Ethics and the Common Good	MDWY - 140	Col of Community Studies & Public Affairs (CSPA)\\n6:00 PM CT	9:50 PM	MGMT-499-01 Case Studies in Strategic Management	MDWY - 146	College of Management(COM)\\n6:00 PM CT	9:50 PM	ICS-372-01 Object-Oriented Design and Implementation	MDWY - 148	College of Sciences(COS)\\n6:00 PM CT	9:50 PM	ICS-440-01 Parallel and Distributed Algorithms	MDWY - 154	College of Sciences(COS)\\n6:00 PM CT	9:50 PM	MIS-310-02 Principles of Management Information Systems	MDWY - 158	College of Management(COM)\\n6:00 PM CT	9:50 PM	PSYC-300-01 Abnormal Psychology	MDWY - 16	Col of Community Studies & Public Affairs (CSPA)\\n6:00 PM CT	9:00 PM	PSYC-611-01 Advanced Lifespan Developmental Psychology	MDWY - 18	Col of Community Studies & Public Affairs (CSPA)\\n6:00 PM CT	9:00 PM	EDU-483-01 Foundations of Teaching Reading in Urban Grades K-6	MDWY - 34	School of Urban Education(UED)\\n6:00 PM CT	9:50 PM	MATH-310-01 Calculus III: Multivariable Calculus	MDWY - 35	College of Sciences(COS)"
        )
        file.close()

    def test_print_header(self):
        pass


if __name__ == "__main__":
    unittest.main()
