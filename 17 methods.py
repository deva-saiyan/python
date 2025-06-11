class store:

    def __init__(self):
        print(f'welcome to our store')

    @staticmethod
    def shop():
        print(f'max')

    @classmethod
    def rap(cls):
        print(f'min')


aa=store()
aa.rap()
aa.shop()

