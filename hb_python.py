#test comment1
import happybase
connection = happybase.Connection('localhost')
connection.create_table('tab',{'vi': dict()})
table = connection.table('tab')
table.put('row1', {'vi:name': 'abcdef'})
table.put('row1', {'vi:dob_year': '2012'})
table.put('row2', {'vi:addr': 'LA'})
table.put('row2', {'vi:Gender': 'Male'})
for key, data in table.scan():
    print key, data
row = table.row('row1')
print row['vi:name']
print row['vi:addr']
