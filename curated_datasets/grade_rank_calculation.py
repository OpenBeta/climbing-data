import re

def calculate_grade_rank(grade):
    
    """
        function to calculate unambiguous rock climb grades, the grade should be passed as a string, e.g. "V7" or "5.10a"
    """
    
    weight_dict = {'YDS': {'a': 0, 'a/b': 1, '-': 1, 'b':2, 'b/c':3, 'not_given':3, 'c':4, 'c/d':5, '+':5, 'd':6},
               'Vermin': {'-': 0, 'not_given': 1,  '+': 2, 'range': 2}} # e.g. V7-8 would be calculated as 7*10 + 2
    
    if grade == None:
        return grade
    
    elif 'V' in grade:
        grade_type = 'Vermin'
        noV = grade.replace('V', '')
        ran = re.match(r'\d{1,2}-\d{1,2}', noV) # check if the grade is given as a range
        num = int(re.sub('[^0-9]', '', noV.split('-')[0]))
        non_num = re.sub('[0-9]', '', noV)
        
    elif '5.' in grade:
        grade_type = 'YDS'
        no5 = grade.split('.')[-1]
        num = int(re.sub('[^0-9]', '', no5))
        non_num = re.sub('[0-9]', '', no5)
        ran = None # not using range grades here, e.g. a/b has its own entry in the weight dict
        
    else:
        message = ' '.join(['grade format of', grade, 'does not match the YDS or Vermin systems.'])
        raise ValueError(message)
    
    non_num = 'not_given' if non_num == '' else non_num
    wdict = weight_dict[grade_type]
    weight = wdict['range'] if ran else wdict[non_num]
    rank = 10 * num + weight
   
    return rank

if __name__ == '__main__':

    example_grades = ['V8-9', 'V9', 'V10-', 'V10', 'V10+', 'V10-11', '5.8', '5.9', '5.9+', '5.12a', '5.12a/b',
                      '5.12-', '5.12b', '5.12b/c', '5.12', '5.12c', '5.12c/d', '5.12+', '5.12d']

    for grade in example_grades:
        line = [grade, calculate_grade_rank(grade)]
        print('{:<7} {:<3}'.format(*line))
