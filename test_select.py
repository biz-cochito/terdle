import questionary
style = questionary.Style([('instruction', 'fg:#808080')])
q = questionary.select("Choose", choices=["A", "B"], style=style)
print(q.application.style)
