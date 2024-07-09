import string

def reverse_without_punctuation_using_stack(s):
  
    punctuation = string.punctuation
    

    stack = []
    

    for char in s:
        if char not in punctuation:
            stack.append(char)

    result = []
    

    for char in s:
        if char in punctuation:
            result.append(char)
        else:
            result.append(stack.pop())

    return ''.join(result)


input_str = "ahmad,bahram$cookie"


output_str = reverse_without_punctuation_using_stack(input_str)


print(output_str)