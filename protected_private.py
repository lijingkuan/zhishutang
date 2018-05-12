class A():
    def test_public(self):
        print('this is a public function')

    def _test_protected(self):
        print('this is a protected function')

    def __test_private(self):
        print('this is a private function')


a = A()
a.test_public()
a._test_protected()
a.__test_private()

# 最后一个无法执行，因为访问不到类的private方法