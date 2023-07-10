from spektrum import Spec, DataSpec
from spektrum import expect, require, skip_if, incomplete, metadata, fixture
from spektrum.runner import SpektrumRunner

'''
def mydecorator(func):
    def wrapped(self, *args, **kwargs):
        name = func.__name__
        func(self, *args, **kwargs)

        for cls in self.__class__.__mro__:
            if cls.__dict__.get(name) is func:
                break
            supermeth = getattr(super(cls, self), name, None)
            if supermeth is not None:
                supermeth(*args, **kwargs)
    return wrapped
'''
import functools






'''
def dependencies(*cases):
    
    def wrapper(f):
        @functools.wraps(f)
        def decorated(self, *args, **kwargs):
            #print(self.__qualname__)

            print(cases)
            print(self.msg)
            print(self.__test_cases__)
            for case in cases:
                for i in range(len(self.__test_cases__)):
                    print(f'case: {self.__test_cases__[i].__qualname__}')
                    print(f'this: {f.__qualname__}')
                    if self.__test_cases__[i].__qualname__ == f.__qualname__:
                        self.__test_cases__.insert(i, case)

            print(f'all cases: {self.__test_cases__}')

            return f(self, *args, **kwargs)

        return decorated
    return wrapper
'''
'''
def dependencies(*cases):

    def wrapper(self, *args, **kwargs):
        print(self)
        def decorated(f):
            return f
        return decorated(self, *args, **kwargs)
    return wrapper
'''
'''
def dependencies(*cases):

    def wrapper(self, *args, **kwargs):
        print(self)
        def decorated(f):
            return f
        return decorated(self, *args, **kwargs)
    return wrapper
'''
'''
def dependencies(*cases):

    def wrapper(f):
        @functools.wraps(f)
        def decorated(self, *args, **kwargs):
            #print(self.__qualname__)
            print('im running')
            print(cases)
            print(self.msg)
            print(self.__test_cases__)
            for case in cases:
                for i in range(len(self.__test_cases__)):
                    print(f'case: {self.__test_cases__[i].__qualname__}')
                    print(f'this: {f.__qualname__}')
                    if self.__test_cases__[i].__qualname__ == f.__qualname__:
                        self.__test_cases__.insert(i, case)

            print(f'all cases: {self.__test_cases__}')

            return f(self, *args, **kwargs)

        return decorated
    return wrapper
'''

def dependencies(*cases):
    def decorated(f):

        '''
        str_cases = ()
        for case in cases:
            print(case.__qualname__)
            str_cases = str_cases + (case.__name__,)


        print(str_cases)
        '''
        SpektrumRunner.global_runner.add_test_dependencies(f, *cases)
        return f
    return decorated
'''
class SuperParent(Spec):

    class Parent(Spec):

        msg = 'foo'

        def navigate_to_site(self):
            expect('bam').to.equal('bam')

        @dependencies(navigate_to_site)
        def signup(self):
            expect('bam').to.equal('bam')

        def add_credits(self):
            expect('bam').to.equal('bam')

        @dependencies(signup, add_credits)
        def checkout(self):
            print('checkout ran')
            expect('bam').to.equal('bam')

        @dependencies(checkout)
        def purchase_parent(self):
            print('purchase ran')
            expect('bam').to.equal('bam')

        class Child(Spec):

            def login(self):
                expect('bam').to.equal('bam')

            def checkout(self):
                expect('bam').to.equal('bam')

            @dependencies(checkout)
            def purchase_child(self):
                expect('bam').to.equal('bam')
'''

class SuperParent(Spec):

    class DatasetParent(Spec):

        msg = 'bar'

        DATASET = {
            'test': {'sample': 1},
            'test2': {'args': {'sample': 2}, 'meta': {'test': 'sample'}}
        }

        def first(self, sample):
            pass

        @dependencies(first)
        def second_depends_on_first(self, sample):
            pass

        def third(self, sample):
            pass

        @dependencies(second_depends_on_first, third)
        def fourth_depends_on_second_third(self, sample):
            pass
        '''
        @dependencies(checkout)
        def purchase_parent(self, sample):
            print('purchase ran')
            expect('bam').to.equal('bam')

        class Child(Spec):

            def login(self):
                expect('bam').to.equal('bam')

            def checkout(self):
                expect('bam').to.equal('bam')

            @dependencies(checkout)
            def purchase_child(self):
                expect('bam').to.equal('bam')
        '''
