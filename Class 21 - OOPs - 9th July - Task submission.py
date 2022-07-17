import logging
logging.basicConfig(filename="oops_logcapture.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

# Constructor-Example
class student:
    def __init__(self, name , email, contact) :
        logging.info("Student details from ineuron_student class")
        self.name = name
        self.email = email
        self.contact = contact

class classtype:
    def __init__(self, classname, classmode) :
        logging.info("Type of class student attending from ineuron_classtype")
        self.classname = classname
        self.classmode = classmode

class courses_enrolled:
    def __init__(self, courses_enrolled, course_fee):
        logging.info("Number of courses enrolled in ineuron_courses_enrolled class")
        self.courses_enrolled = courses_enrolled
        self.course_fee = course_fee

    def details(self, course_name, course_ID):
        logging.info("course details from ineuron_courses_enrolled class")
        self.__course_name = "Big data bootcamp"
        self.course_ID = "BDBC_2022"

    def details_updated(self):
        logging.info("Updated course details from ineuron_courses_enrolled class")
        self.__course_name = "Fullstack DS bootcamp"
        self._course_ID = "FSDS_2022"

class internship:
    def __init__(self, project, division):
        logging.info("Details from internship class")
        self.project = project
        self.division = division

class job_offer:
    def __init__(self, org, package, position):
        logging.info("Job offer details from ineuron_job_offer class")
        self.__org = org
        self.__package = package
        self.position = position

class affiliates:
    def __init__(self, course, number_of_referrals) :
        logging.info("class detail from class")
        self.course = course
        self.number_of_referrals = number_of_referrals

class blog:
    def __init__(self, topiccategory , author) :
        logging.info("Blog topic details from blog")
        self.topiccategory = topiccategory
        self.author = author

# ---Inheritance------

class enrolledstudent:
    def student(self, fullname, experience, background):
        logging.info("Details of student in student class")
        self.fullname = fullname
        self.experience = experience
        self.background = background

class enrolledbatch:
    def course_details(self, coursename, loginstatus):
        logging.info("course details from enrolledbatch")
        self.coursename = coursename
        self.loginstatus = loginstatus

class internship(enrolledbatch):
    def project(self):
        logging.info("student internship name details")
        try:
            if self.coursename == 'FSDS' and self.loginstatus == 'successful':
                logging.info("Able to go proceed for intership portal")
            else:
                print("Not authorized to access internship portal")
        except Exception as e:
            print(e)

class courses_enrolled1:
    def details(self):
        logging.info("Details of courses enrolled in ineuron_courses_enrolled class")
        self.course_name = "FSDS bootcamp"
        self.course_ID = "FSDS_2022"

class internportal(courses_enrolled1):
    def access(self) :
        try:
            if self.courseID == 'FSDS_2022':
                logging.info("Access details from internportal class")
                print("Navigating to intern portal")
            else:
                print("Please contact administrator for access")
        except Exception as e:
            print(e)

class jobportal(enrolledstudent,enrolledbatch):
    def joboffer(self):
        logging.info("Job details from job class")
        try:
            if self.experience <= 0:
                logging.info("Enrolled student is fresher")
                print("Eligible for the current drive")
            elif self.coursename == 'FSDS':
                print("Eligible for the current drive")
            else:
                print("Drive is only for 0-4 year exp")
        except Exception as e:
            print(e)

# --method overriding

class courses_enrolled1:
    def __init__(self, courses_enrolled, course_fee):
        logging.info("Number of courses enrolled in ineuron_courses_enrolled class")
        self.courses_enrolled = courses_enrolled
        self.course_fee = course_fee

    def details1(self):
        logging.info("course details from ineuron_courses_enrolled class")
        try:
            self.__course_name = "Big data bootcamp"
            self.course_ID = "BDBC_2022"
        except Exception as e:
            logging.exception(e)

class new_details_updated(courses_enrolled1):
    def details_updated(self):
        logging.info("Updated course details from ineuron_courses_enrolled class")
        try:
            self.__course_name = "Fullstack DS bootcamp"
            self._course_ID = "FSDS_2022"
        except Exception as e:
            logging.exception(e)


# ---------Abstraction
import logging
logging.basicConfig(filename="oops_logcapture.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
class enrolledstudent1:
    def student(self, fullname, experience, background):
        logging.info("Details of student in student class")
        self.fullname = fullname
        self.experience = experience
        self.background = background

class enrolledbatch1:
    def course_details(self, coursename, loginstatus):
        logging.info("course details from enrolledbatch")
        self.coursename = coursename
        self.loginstatus = loginstatus

class internship1(enrolledbatch1):
    def project(self):
        logging.info("student internship name details")
        try:
            if self.coursename == 'FSDS' and self.loginstatus == 'successful':
                logging.info("Able to go proceed for intership portal")
            else:
                print("Not authorized to access internship portal")
        except Exception as e:
            print(e)


class job_details(enrolledstudent1):
    def __init__(self, org, package, position):
        logging.info("Job offer details from ineuron_job_offer class")
        self.__org = org
        self.__package = package
        self.position = position

        try:
            if self.coursename == 'FSDS':
                logging.info("student is from FSDS batch")
                print("Can Attend current drive")
            elif self.background == 'tech':
                logging.info("student is from tech background")
                print("Can Attend current drive")
            elif self.experience <= 4:
                logging.info("student is from FSDS batch")
                print("Position offered is:", job_details.__position)
                print("Package offered is:",job_details.__package)

            else:
                print("Drive is only for 0-4 year exp")
        except Exception as e:
            print(e)


# ---------Encapsulation
class login:

    def admin_login(self, username, student_name, batch):
        try:
            logging.info("Admin 1 logged in")
            self.username = username
            self.student_name = student_name
            self.batch = batch
            self.fee = 17000
            print("fee for student is:",self.fee)
        except Exception as e:
            logging.exception(e)

    def admin_login2(self, username, new_value):
        # logging.info("Admin 2 logged in")
        self.username = username
        try:
            self.fee = new_value
            logging.info("Discounted Fees updated by Admin 2")
            print("Updated fee for student is:",self.fee)
        except Exception as e:
            logging.exception(e)
