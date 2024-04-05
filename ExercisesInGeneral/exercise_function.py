def test_4():
    ...
    def test_3():
        ...
        def test_2():
            ...
            def test_1():
                ...
                def test_0(number):
                    return f'Number is: {number}'
                return test_0
            return test_1()
        return test_2()
    return test_3()
    


variable_1 = test_4()
print(variable_1(1))
    