class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        k=0
        while i<len(students):
            a=students.pop(i)
            if a==sandwiches[0]:
                choose=True
                sandwiches.pop(0)
                k=0
            else:
                students.append(a)
            if k==len(sandwiches):
                break
            k+=1
        return len(students)
