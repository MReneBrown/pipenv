class Invoice:

    def greeting(self):
        return 'Hi there'


inv_one = Invoice()
print(inv_one)

inv_two = Invoice()
print(inv_two)

# <__main__.Invoice object at 0x00000267DC18D610>
# <__main__.Invoice object at 0x00000267DC18D640>



inv_one = Invoice()
print(inv_one.greeting())

inv_two = Invoice()
print(inv_two.greeting())

Hi there
Hi there