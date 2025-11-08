# Write a program to fill in a letter template given below with name and date. Letter = ''' <|name |> you are selected <|Date|>'''

letter = '''<|name|>
you are selected
<|Date|>
'''
print(letter.replace("<|name|>","Najam").replace("<|Date|>","11 November 25"))