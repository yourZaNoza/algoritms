class Comment:

    count = 0

    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comments(first, second):
        return f"{first}{second}"

    def upcount(self):
        self.count += 1


my_comment = Comment("My comment")
my_comment.upcount()
print(my_comment.count)
my_comment.count = 17
print(my_comment.__dict__)
print(my_comment.count)

print(Comment.count)
print(Comment.__dict__)

m_1 = Comment.merge_comments("Привет","студент!")
print(m_1)
m_2 = Comment.merge_comments("Great","OK")
print(m_2)
