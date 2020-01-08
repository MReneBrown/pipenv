class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

#    def get_client():
#         return self.client
# Example of Java code to be able grab the client

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)

# print(google.get_client)
# Example of Java code to be able to get client (getter method)
print(google.client)

google.client = 'Yahoo'
# Setter process-go into object and set the value

print(google.client)