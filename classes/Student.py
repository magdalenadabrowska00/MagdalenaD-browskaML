class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def is_passed(self) -> bool:
    avg = sum(self.marks) / len(self.marks)

    if (avg > 50):
      return True
    else:
      return False
      
  def __str__(self):
        return f'Student: {self.name}: {self.marks}'