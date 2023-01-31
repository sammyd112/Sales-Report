"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

f = open('sales-report.txt')

for line in f:
    """Stripping the last characters from each line"""
    line = line.rstrip()
    """Creating a list and indices"""
    entries = line.split('|')
    """Assigning Salesperson to a variable"""
    salesperson = entries[0]
    """Assigning Melons to a variable"""
    melons = int(entries[2])


    """If statement to Check if sales person is already in salespeople"""
    if salesperson in salespeople:
        """Assigned a variable to the index of salesperson"""
        position = salespeople.index(salesperson)
        """At the same index, add the number of melons to melons_sold"""
        melons_sold[position] += melons
        
    else:
        """Add sales person and melons sold to their respective lists"""
        salespeople.append(salesperson)
        melons_sold.append(melons)


"""Using the length of the salespeople, create range, and find index"""
for i in range(len(salespeople)):
    """Recall the salespeople and melons sold using index"""
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

"""Suggested Code improvement"""

# melon_sales_dic = {}

# for line in f:
#     """Stripping the last characters from each line"""
#     line = line.rstrip()
#     """Creating a list and indices"""
#     entries = line.split('|')
#     """Assigning Salesperson to a variable"""
#     salesperson = entries[0]
#     """Assigning Melons to a variable"""
#     melons = int(entries[2])
#     """If salesperson is not in dictionary, they will be added, if they are,
#      the value of melons will continue to increase"""
#     melon_sales_dic[salesperson] = melon_sales_dic.get(salesperson, 0) + melons

# for salesperson, melons in melon_sales_dic.items():
#     print(salesperson, melons)