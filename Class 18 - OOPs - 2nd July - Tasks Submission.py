import logging
logging.basicConfig(filename="logcapture.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

class list_tasks:
    logging.info("Inside the list_tasks class")
    def list_obj_extract(self, l):
        logging.info("Control is in the list_obj_extract function")
        try:
            self.l = l
            for i in self.l:
                if type(i) == list:
                    print(i)
        except Exception as e:
            logging.exception(e)


    def tuple_obj_extract(self, l):
        logging.info("Control is in the tuple_obj_extract function")
        try:
            self.l = l
            for i in self.l:
                if type(i) == tuple:
                    print(i)
        except Exception as e:
            logging.exception(e)


    def dict_obj_extract(self, l):
        logging.info("Control is in the dict_obj_extract function")
        try:
            self.l = l
            for i in self.l:
                if type(i) == dict:
                    print(i)
        except Exception as e:
            logging.exception(e)


    def num_data_extract(self, l):
        logging.info("Control is in the num_data_extract function")
        try:
            self.l = l
            list_new = []
            for i in self.l:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            list_new.append(j)

                if type(i) == set:
                    for m in list(set(i)):
                        list_new.append(m)

                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int:
                            list_new.append(k)
                            list_new.append(v)
            print("All the numeric elements:", list_new)

        except Exception as e:
            logging.exception(e)


    def sum_of_elements(self, l):
        logging.info("Control is in the sum_of_elements function")
        try:
            self.l = l
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)

                if type(i) == dict:
                    for k in i.items():
                        if type(k) == int:
                            l1.append(k)

                if type(i) == set:
                    for m in list(set(i)):
                        if type(m) == int:
                            l1.append(m)

            summation = 0
            for s in range(0, len(l1)):
                summation = summation + s
            print("sum of numbers is:", summation)

        except Exception as e:
            logging.exception(e)


    def odd_values(self, l):
        logging.info("Control is in the odd_values function")
        try:
            self.l = l
            list_new1=[]
            list_new2=[]
            for i in self.l:
                if type(i)==list or type(i)==tuple:
                    for j in i:
                        if type(j) == int:
                            list_new1.append(j)

                if type(i) == dict:
                    for k in i.items():
                        if type(k) == int:
                            list_new1.append(k)

                if type(i) == set:
                    for m in list(set(i)):
                        if type(m) == int:
                            list_new1.append(m)

            for o in range(0, len(list_new1)):
                if (o % 2) != 0:
                    list_new2.append(o)

            print("Collection of integers:", list_new1)
            print("The list of odd numbers:", list_new2)

        except Exception as e:
            logging.exception(e)


    def extract_ineuron(self, l):
        logging.info("Control is in the extract_ineuron function")
        try:
            self.l = l
            str = "ineuron"
            for i in l:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if j == "ineuron":
                            print(j, type(k))

                if type(i) == dict:
                    for k in i.items():
                        if k == "ineuron":
                            print(k, type(k))

                    for v in i.values():
                        if v == "ineuron":
                            print(v, type(v))

        except Exception as e:
            logging.exception(e)


    def occurence_of_elements(self, l):
        logging.info("Control is in the occurence_of_elements function")
        try:
            self.l = l
            list_new=[]

            for i in self.l:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        list_new.append(j)

                if type(i) == set:
                    for m in list(set(i)):
                        list_new.append(m)

                if type(i) == dict:
                    for k, v in i.items():
                        list_new.append(k)
                        list_new.append(v)

            print("All the elements in the given list:", "\n", l)
            print("All the elements in the collection:", "\n", list_new)

            for c in set(list_new):
                print("Occurence of", c, "is", list_new.count(c))

        except Exception as e:
            logging.exception(e)


    def count_of_keys(self, l):
        logging.info("Control is in the count_of_keys function")
        try:
            self.l = l
            list_new = []

            for i in self.l:
                if type(i) == dict:
                    for j in i:
                        list_new.append(j)

            print("Number of keys in Dictionary are:", len(list_new))

        except Exception as e:
            logging.exception(e)

    def filter_string_obj(self, l):
        logging.info("Control is in the filter_string_obj function")
        try:
            self.l = l
            list_new = []

            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            list_new.append(j)

                        if type(i) == dict:
                            for k, v in i.items():
                                if type(k) == str or type(v) == str:
                                    list_new.append(k)
                                    list_new.append(v)
            for i in list_new:
                print("Elements with string data type in the collection are:", list_new)

        except Exception as e:
            logging.exception(e)

    def filter_alphanum_obj(self, l):
        logging.info("Control is in the filter_alphanum_obj function")
        try:
            self.l = l
            list_new1 = []
            list_new2 = []

            for i in self.l:
                if type(i) == dict:
                    for k in i.items():
                        list_new1.append(k)

            for i in list_new1:
                for j in i:
                    if type(j)!=int:
                        list_new2.append(j)

            for a in list_new2:
                if a.isalnum():
                    print("Alphanumeric elements are:", a)

        except Exception as e:
            logging.exception(e)


    def multiply_elements(self, l):
        logging.info("Control is in the multiply_elements function")
        try:
            self.l = l
            list_new1 = self.l[0]
            list_new2 = self.l[1]
            list_new3 = self.l[2]
            s1 = list(list_new3)

            a=1
            b=1
            c=1
            d=1

            l1_mul = []
            l2_mul = []
            l3_mul = []
            s1_mul = []

            # Multiplication of elements inside l[0]
            for i in list_new1:
                a = a * i
            l1_mul.append(a)

            # Multiplication of elements inside l[1]
            for j in list_new2:
                b = b * j
            l2_mul.append(b)

            # Multiplication of elements inside l[2]
            for k in list_new3:
                c = c * k
            l3_mul.append(c)

            # Multiplication of elements inside l[3]
            for l in s1:
                d = d * l
            s1_mul.append(d)

            print("Multiplication of elements in list l[0]:", l1_mul)
            print("Multiplication of elements in list l[1]:", l2_mul)
            print("Multiplication of elements in list l[2]:", l3_mul)
            print("Multiplication of elements in list l[3]:", s1_mul)


        except Exception as e:
            logging.exception(e)


    def unwrap_elements(self, l):
        logging.info("Control is in the unwrap_elements function")
        try:
            self.l = l
            list_new = []

            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        list_new.append(j)

                if type(i) == dict:
                    for k,v in i.items():
                        list_new.append(k)
                        list_new.append(v)

            print("Unwrapped all the elements in the collection to new flat list:", "\n", list_new)


        except Exception as e:
            logging.exception(e)

class string_tasks:
    logging.info("Inside the string_tasks class")

    def string_print(self, s1):
        logging.info("Control is in the string_print function")
        try:
            self.s1 = s1
            return self.s1

        except Exception as e:
            logging.exception(e)


    def string_slicing(self, s2):
        logging.info("Control is in the string_slicing function")
        try:
            self.s2 = s2
            return self.s2[1:5]

        except Exception as e:
            logging.exception(e)


    def slicing_with_step(self, s2):
        logging.info("Control is in the slicing_with_step function")
        try:
            self.s2 = s2
            return self.s2[6:30:2]

        except Exception as e:
            logging.exception(e)


    def string_reverse(self, s2):
        logging.info("Control is in the string_reverse function")
        try:
            self.s2 = s2
            return s2[::-1]

        except Exception as e:
            logging.exception(e)


    def string_multiply(self, s1):
        logging.info("Control is in the string_multiply function")
        try:
            self.s2 = s2
            return s1 * 4

        except Exception as e:
            logging.exception(e)


    def string_split(self, s2):
        logging.info("Control is in the string_split function")
        try:
            self.s2 = s2
            return s2.split('i')

        except Exception as e:
            logging.exception(e)


l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
l1 = list_tasks()
l1.list_obj_extract(l)
l1.tuple_obj_extract(l)
l1.dict_obj_extract(l)
l1.num_data_extract(l)
l1.sum_of_elements(l)
l1.odd_values(l)
l1.extract_ineuron(l)
l1.occurence_of_elements(l)
l1.count_of_keys(l)
l1.filter_string_obj(l)
l1.filter_alphanum_obj(l)
l1.multiply_elements(l)
l1.unwrap_elements(l)

s1 = "sudhanshu"
s2 = "this is my very first programming class's"
s_obj = string_tasks()

print(s_obj.string_print(s1))
print(s_obj.string_slicing(s2))
print(s_obj.slicing_with_step(s2))
print(s_obj.string_reverse(s2))
print(s_obj.string_multiply(s1))
print(s_obj.string_split(s2))