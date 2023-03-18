def check_one_away(test_text, check_text):
    blank_char = "_"
    if abs(len(test_text) - len(check_text)) > 1:
        return False
    if len(check_text) > len(test_text):
        for i in range(len(check_text)):
            checkList = list(check_text)
            testList = list(test_text)
            checkList[i] = blank_char
            testList.insert(i, blank_char)
            if (checkList == testList):
                return True
        return False
    elif len(check_text) < len(test_text):
        for i in range(len(test_text)):
            checkList = list(check_text)
            testList = list(test_text)
            testList[i] = blank_char
            checkList.insert(i, blank_char)
            if (checkList == testList):
                return True
        return False
    else:
        for i in range(len(test_text)):
            checkList = list(check_text)
            testList = list(test_text)
            testList[i] = blank_char
            checkList[i] = blank_char
            if (checkList == testList):
                return True
        return False

if __name__ == "__main__":
    check_tuples = [
            ('pale', 'ple'),
            ('pales', 'pale'),
            ('pale', 'bale'),
            ('pale', 'bake')
            ]
    
    for str_tup in check_tuples:
        print(str_tup)
        print(check_one_away(str_tup[0], str_tup[1]))
