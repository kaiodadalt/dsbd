header = 'date(mmddyyyy),srcIP,srcPort,dstIP,dstPort,protocol,priority,IDSID,SignatureGroup,Classification\n'
fixed_content_lines = []

with open('python_exercise.csv') as content:
    for row in content:
        row_data = row.strip().split(',')
        fixed_row = []

        for column in row_data:
            if ':' in column:
                key, value = column.split(':', 1)
                fixed_row.append(value)
            else:
                fixed_row.append('')

        fixed_content_lines.append(','.join(fixed_row))

fixed_content = '\n'.join(fixed_content_lines)

print(header + fixed_content)
