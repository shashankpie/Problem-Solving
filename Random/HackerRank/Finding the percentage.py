if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    nums = student_marks[query_name]
    avg = sum(nums) / len(nums)
    print(f"{avg:.2f}")
