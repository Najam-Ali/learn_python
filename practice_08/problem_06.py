# WAP to remove a given word from a string and strip it at the same time using function.
# def remove_word_and_strip(string, word):
#     modified_string = string.replace(word, "")
#     return modified_string.strip() # Strip method remove the leading and trailing spaces and words also.
# new_string = remove_word_and_strip("Ahmed, Good Day", "Day")
# print(new_string)

# WAP to remove a given word from a list and strip it at the same time using function.
# def remove_word_and_strip(li, word):
#     modified_list = [item.replace(word, "") for item in li]
#     return [item.strip() for item in modified_list]
# new_list = remove_word_and_strip([" Ahmed ", " Good Day ", " Hello "], "Day")
# print(new_list)

# The above solution is not my own i have taken help from chatgpt to solve this problem.But in tutorial way to resolve this problem is:
# def remove_word_and_strip(li, word):
#     empty_list = []
#     for item in li:
#         modified_item = item.replace(word, "")
#         stripped_item = modified_item.strip()
#         empty_list.append(stripped_item)
#     return empty_list
# new_list = remove_word_and_strip([" Ahmed ", " Good Day ", " Hello "], "Day")
# print(new_list)

def remove_word_and_strip(li, word):
    empty_list = []
    for item in li:
        if not(item == word):
            empty_list.append(item.strip(word))
    return empty_list

li = ["Ahmed", "ShahidDay", "Majid","Day"]
print(remove_word_and_strip(li, "Day"))
