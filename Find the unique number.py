# I forgot about task's text
# There was said that array contained at least 3 numbers and there was one different number in any array

def find_uniq(arr):
    s_arr = sorted(arr)
    if s_arr[0] != s_arr[1]:
        return s_arr[0]
    return s_arr[-1]

print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
