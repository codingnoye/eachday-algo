class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def __str__(self):
        return self.title
a = Article('제목','내용')
print(a)