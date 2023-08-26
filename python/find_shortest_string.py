
"""
base case should be if the array length is 1, return.... should be the single element

next we should test the length of element at position 0 = against length of the return value of calling the function but we should slice off the begining.
    this allows us to hit our base case at some point

if the length of element 0 is less than or equal to the return,
    return element 0

else
    return the function call but with the front sliced off.

    
this guarentes we will hit our base case.
"""

def find_shortest_string(arr):
    if len(arr) == 1:
        return arr[0]

    if len(arr[0]) <= len(find_shortest_string(arr[1:])):
        return arr[0]
    else:
        return find_shortest_string(arr[1:])
        

if __name__ == "__main__":

    test_values = [
        ['aaa', 'a', 'bb', 'ccc'],
        ['cat', 'hi', 'dog', 'an'],
        ['flower', 'juniper', 'lily', 'dandelion']
    ]

    test_answers = [
        "a",
        "hi",
        "lily"
    ]


    for value, answer in zip(test_values, test_answers):
        result = find_shortest_string(value)

        # assert result == answer, f"Test failed for {value}. Expected {answer}, got {result}"
        try:
            assert result == answer
        except:
            print(f"Test failed for {value}. Expected {answer}, got {result}")
        else:
            print(f"Test successful")