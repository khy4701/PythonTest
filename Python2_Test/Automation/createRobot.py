data_list = ['dat1', 'dat2', 'dat3']
data_dict = {'dat1': 'abc',
             'dat2': [4, 5, 6],
             'dat3': [7, 8, 9],
             'dat4': [0, 4, 6]}

class MyAwesomeClass:

    def __init__(self, data_list, data_dict):
        counter = 0

        for key, value in data_dict.iteritems():
            if key in data_list:
                setattr(self, key, value)
            else:
                setattr(self, 'unknown' + str(counter), value)
                counter += 1
                
                
A = MyAwesomeClass(data_list,data_dict)

print( getattr(A, "dat1"))

print A.dat1




