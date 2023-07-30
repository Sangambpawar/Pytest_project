class Test_pr1:
    from selenium  import webdriver
    def test_sum(self):
        a=15
        b=15
        c=a+b
        print('sum  is',c)
        if c==30:
            print('test is pass')
            assert True
        else:
            print('test is failed')
            assert False
    def test_sub(self):
        a=15
        b=15
        c=a-b
        if c==0:
            print('test is pass')
            assert True
        else:
            print('test is faiiled')
            assert False

