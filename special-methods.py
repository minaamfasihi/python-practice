class Book(object):
    def __init__(self, title, author, pages):
        print("Book has been created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, Author: %s, Pages: %s " %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('Book is deleted')

b = Book('Python', 'Jose', 10)
print(b) # Now the __str__ of book will be called
# output: Title: Python, Author: Jose, Pages: 10


print(len(b)) # 10 (no. of pages of book because we have overridden the len method)

del b # Book is deleted