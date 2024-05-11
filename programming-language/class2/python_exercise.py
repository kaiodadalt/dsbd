header = ''
fixed_content_lines = []

with open('python_exercise.csv') as content:
    for index, row in enumerate(content):
        row_data = row.strip().split(',')
        fixed_row = []

        for column in row_data:
            if ':' in column:
                key, value = column.split(':', 1)

                if index == 1:
                    header += key + ','

                fixed_row.append(value)
            else:
                fixed_row.append('')

        fixed_content_lines.append(','.join(fixed_row))

fixed_content = '\n'.join(fixed_content_lines)
fixed_csv = header[:-1] + fixed_content

print(fixed_csv)