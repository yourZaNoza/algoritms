class NoteTwo:
    def __init__(self, text, count, iscompleted):
        self.text = text
        self.count = count
        self.iscompleted = iscompleted

    def upcount(self, plus):
        self.count += plus

    def reset(self):
        self.count = 0


note1 = NoteTwo("Task1", 5, True)

print(note1.__dict__)
print(dir(note1))

print(note1.text)
print(note1.iscompleted)

note1.upcount(2)
print(note1.count)

note1.reset()
print(note1.count)
