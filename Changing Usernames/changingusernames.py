# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
s = set()
t = set()
for line in fileinput.input():
    try:
        s_i, t_i = line.strip().split()
        s.add(s_i)
        t.add(t_i)
    except:
        n=int(line.strip())

if s == t:
    print("No")
else:
    missing_elements = t - s
    if len(missing_elements) > n or len(s) + len(missing_elements) > 2 * n:
        print("No")
    else:
        print("Yes")