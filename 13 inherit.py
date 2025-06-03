class A:
    def dad(self):
        print('dad')

    def phone(self):
        print('phone')


class B(A):
    def mom(self):
        print('mom')

    def sweet(self):
        print('sweet')


class C(B):
    def sis(self):
        print('sis')

    def money(self):
        print('money')


class D(B):
    def frd(self):
        print('frd')

    def bike(self):
        print('bike')


class All(C, D):  # Multiple inheritance
    def me(self):
        print('me')
        super().bike()  # Calls D's bike() because of MRO (C comes before D in the method resolution order)
        self.mom()


# Create object and call methods
deva = All()
deva.me()
deva.dad()



'''Multilevel Inheritance: A → B → C

Hierarchical Inheritance: B → C and B → D

Multiple Inheritance: All → (C, D)'''