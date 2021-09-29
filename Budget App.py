budget = {}

print('Type "exit" to stop adding categories.')
while True:
    category = input('Type a new budget category. ')
    if category.upper() == 'EXIT':
        break
    else:
        cat_budget = input(f'Type the budget for the {category} category. $') # cat short for category
        try:
            if isinstance(int(cat_budget), int) == True:
                budget[category] = cat_budget
        except ValueError:
            print('Please type a number and re-enter the previous category.')
        pass

print('Type "exit" to end program.')
while True:
    for x in budget:
        print(x.upper(), end=", ")
    user_cat = input("\nChoose a budget category from above. ")
    for cat in budget:
        if cat.upper() == user_cat.upper():
            add_remove = input('Before the number type in "+" to add money and "-" to remove money.  ')
            try:
                num = int(add_remove)
                cat_num = int(budget[cat])
                if '+' in add_remove:
                    cat_num += num
                    print(f'${cat_num} left in {cat} budget.')
                    budget[cat] = cat_num
                    pass
                elif '-' in add_remove:
                    cat_num += num
                    print(f'${cat_num} left in {cat} budget.')
                    budget[cat] = cat_num
                    pass
                elif '+' or '-' not in add_remove:
                    print('Please make sure your number includes a "+" or "-".')
                    pass
            except ValueError:
                print('PLEASE TYPE A NUMBER')
    if user_cat.upper() == 'EXIT':
        for key in budget:
            print(f'{key.upper()}: ${budget[key]}')
        break

