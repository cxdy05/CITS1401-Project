def main(csvfile_1, csvfile_2, age, sa2_1, sa2_2):


    #Output1 / Task1
    def OP1(csvfile_2, age):
        with open(csvfile_2, 'r') as file:
            headers = file.readline()
            headers = headers.strip()
            headers = headers.lower()
            headers = headers.split(',')
            for header in headers:
                # replacing "Age " and turning the header into a list of bounds
                # "Age 0-4" becomes [0, 4]
                header = header.replace('age ', '').strip()
                if '-' in header:
                    bounds = header.split('-')
                    lower_bound = int(bounds[0])
                    upper_bound = int(bounds[1])
                    if lower_bound <= age <= upper_bound:
                        return [lower_bound, upper_bound]
                elif '85' in header:
                    overeighty = header.split('and over')
                    lower_bound1 = int(overeighty[0])
                    if age >= lower_bound1:
                        return [lower_bound1, None]
        # returns empty list if no matching age is found
        return []
    OP1 = OP1(csvfile_2, age)
    
    
    #Output2 / Task2
    def OP2(csvfile_1, csvfile_2, sa2_1, sa2_2, age):
        list1 = []
        list2 = []
        sa2areas_1 = []
        sa2areas_2 = []
        
        # 1.
        # sa2_1
        with open(csvfile_1, 'r') as file1:
            headers1 = file1.readline()
            headers1 = headers1.strip()
            headers1 = headers1.lower()
            headers1 = headers1.split(',')
            sa2_index = 0
            sa3_index = 0
            target_sa3_1 = None
            for i in range(len(headers1)):
                if headers1[i] == 'sa2 code':
                    sa2_index = i
                elif headers1[i] == 'sa3 code':
                    sa3_index = i
            # looping to find the matching sa2 code,
            # if match, assign target_sa3 and append the sa3 code to list
            for line in file1:
                data = line.strip()
                data = data.split(',')
                if data[sa2_index] == sa2_1:
                    target_sa3_1 = data[sa3_index]
                    list1.append(data[sa3_index])
       
       # sa2_2
        with open(csvfile_1, 'r') as file1:
            headers2 = file1.readline()
            headers2 = headers2.strip()
            headers2 = headers2.lower()
            headers2 = headers2.split(',')
            sa2_index = 0
            sa3_index = 0
            target_sa3_2 = None
            for i in range(len(headers2)):
                if headers2[i] == 'sa2 code':
                    sa2_index = i
                elif headers2[i] == 'sa3 code':
                    sa3_index = i
            for line in file1:
                data = line.strip()
                data = data.split(',')
                if data[sa2_index] == sa2_2:
                    target_sa3_2 = data[sa3_index]
                    list2.append(data[sa3_index])
        
        # 2.
        # finding all sa2 codes in the sa3 code (looping each row for the sa2 code in that sa3 code)
        if target_sa3_1:
            with open(csvfile_1, 'r') as file1:
                file1.readline()
                for line in file1:
                    data = line.strip()
                    data = data.split(',')
                    if data[sa3_index] == target_sa3_1:
                        sa2areas_1.append(data[sa2_index])
        if target_sa3_2:
            with open(csvfile_1, 'r') as file1:
                file1.readline()
                for line in file1:
                    data = line.strip()
                    data = data.split(',')
                    if data[sa3_index] == target_sa3_2:
                        sa2areas_2.append(data[sa2_index])
                            
        # 3.
        # sa2_1
        with open(csvfile_2, 'r') as file2:
            headers2_1 = file2.readline()
            headers2_1 = headers2_1.strip()
            headers2_1 = headers2_1.lower()
            headers2_1 = headers2_1.split(',')
            area_code_lvl2_index_1 = 0
            total_population1 = []
            for i in range(len(headers2_1)):
                if headers2_1[i] == 'area_code_level2':
                    area_code_lvl2_index_1 = i
            
            # finding+appending the population in the sa2 codes and in the age group
            for line in file2:
                data = line.strip()
                data = data.split(',')
                if data[area_code_lvl2_index_1] in sa2areas_1:
                    for i, header in enumerate(headers2_1):
                        header = header.replace('age ', '').strip()
                        if '-' in header:
                            bounds = header.split('-')
                            lower_bound = int(bounds[0])
                            upper_bound = int(bounds[1])
                            if lower_bound <= age <= upper_bound:
                                total_population1.append(int(data[i]))
                        elif '85' in header:
                            overeighty = header.split('and over')
                            lower_bound1 = int(overeighty[0])
                            if age >= lower_bound1:
                                total_population1.append(int(data[i]))
        
        # sa2_2
        with open(csvfile_2, 'r') as file2:
            headers2_2 = file2.readline()
            headers2_2 = headers2_2.strip()
            headers2_2 = headers2_2.lower()
            headers2_2 = headers2_2.split(',')
            area_code_lvl2_index_2 = 0
            total_population2 = []
            for i in range(len(headers2_2)):
                if headers2_2[i] == 'area_code_level2':
                    area_code_lvl2_index_2 = i
            
            # adding the population in the specific age group for each sa2s' in sa3
            for line in file2:
                data = line.strip()
                data = data.split(',')
                if data[area_code_lvl2_index_2] in sa2areas_2:
                    for i, header in enumerate(headers2_2):
                        header = header.replace('age ', '').strip()
                        if '-' in header:
                            lower_bound, upper_bound = map(int, header.split('-'))
                            if lower_bound <= age <= upper_bound:
                                total_population2.append(int(data[i]))
                        elif '85' in header:
                            overeighty = header.split('and over')
                            lower_bound1 = int(overeighty[0])
                            if age >= lower_bound1:
                                total_population2.append(int(data[i]))
        
        # 4.
        # sa2_1
        # Calculating total population and standard deviation
        n1 = len(total_population1)
        # for assurance
        if n1 == 0:
            average_population1 = 0
            standard_dev1 = 0
        else:
            average_population1 = sum(total_population1) / n1
            if n1 > 1:
                standard_dev1 = sum((x - average_population1) ** 2 for x in total_population1)
                standard_dev1 = (standard_dev1) / (n1 - 1)
                standard_dev1 = (standard_dev1) ** 0.5
            else:
                standard_dev1 = 0
        list1.append(round(average_population1, 4))
        list1.append(round(standard_dev1, 4))
        
        # sa2_2
        n2 = len(total_population2)
        # for assurance
        if n2 == 0:
            average_population2 = 0
            standard_dev2 = 0
        else:
            average_population2 = sum(total_population2) / n2
            if n2 > 1:
                standard_dev2 = sum((x - average_population2) ** 2 for x in total_population2)
                standard_dev2 = (standard_dev2) / (n2 - 1)
                standard_dev2 = (standard_dev2) ** 0.5
            else:
                standard_dev2 = 0
        list2.append(round(average_population2, 4))
        list2.append(round(standard_dev2, 4))
        return list1, list2

    OP2 = OP2(csvfile_1, csvfile_2, sa2_1, sa2_2, age)

    
    #Output3 / Task3
    def OP3(csvfile_1, csvfile_2, age):
        # 1.
        # first finding age column (age_index)
        # using file 1
        with open(csvfile_2, 'r') as file1:
            headers1 = file1.readline()
            headers1 = headers1.strip()
            headers1 = headers1.lower()
            headers1 = headers1.split(',')
            
            age_index = 0
            for i, header in enumerate(headers1):
                if 'age' in header:
                    age_range = header.replace('age ', '').strip()
                    if '85' in age_range:
                        lower = int(age_range.replace('and over', ''))
                        if age >= lower:
                            age_index = i
                    elif '-' in age_range:
                        bounds = age_range.split('-')
                        # using .isdigit() to return True if the characters are digits 
                        if len(bounds) == 2 and bounds[0].isdigit() and bounds[1].isdigit():
                            lower_bound = int(bounds[0])
                            upper_bound = int(bounds[1])
                            if lower_bound <= age <= upper_bound:
                                age_index = i
                                
            area_code_lvl2_index = 0
            for i, header in enumerate(headers1):
                if header == 'area_code_level2':
                    area_code_lvl2_index = i
            
            # 2.
            # to store sa2 = [sa2_code, age_group_population, total_population], used for later
            # age_group_population (population of the specific age group)
            # total_population (the total population for that row for all ages)
            sa2_data1 = []
            for line in file1:
                data = line.strip()
                data = data.split(',')
                sa2_code = data[area_code_lvl2_index]
                # assigning age_group to all population in that column
                # assigned to the data of the specified age group
                # as it loops, eventually its the entire column of the specified age group
                if data[age_index].isdigit():
                    age_group_population = int(data[age_index])
                else:
                    age_group_population = 0

                # adding total population for all ages for that row
                # each line/row is being looped
                total_population = 0
                for i in range(len(data)):
                    if 'age' in headers1[i]:
                        if data[i].isdigit():
                            total_population += int(data[i])
                sa2_data1.append([sa2_code, age_group_population, total_population])
        
        # 3.
        # using file 2
        # making sa3 list = [sa3_code, sa3_name, state_name, [sa2_code]] for later
        # [sa2_code] (a list of sa2 codes in that sa3 code)
        sa3_list = []
        with open(csvfile_1, 'r') as file2:
            headers2 = file2.readline()
            headers2 = headers2.strip()
            headers2 = headers2.lower()
            headers2 = headers2.split(',')

            for i, header in enumerate(headers2):
                if header == 'sa2 code':
                    sa2_index = i
                elif header == 'sa3 code':
                    sa3_index = i
                elif header == 'sa3 name':
                    sa3_name_index = i
                elif header == 's_t name':
                    state_index = i

            for line in file2:
                data = line.strip()
                data = data.split(',')
                # loop each line/row, and assign each sa2/sa3 codes + state name
                sa2_code = data[sa2_index]
                sa3_code = data[sa3_index]
                sa3_name = data[sa3_name_index]
                state_name = data[state_index]

                found = False
                for entry in sa3_list:
                    if entry[0] == sa3_code:
                        entry[3].append(sa2_code)
                        found = True
                if not found:
                    sa3_list.append([sa3_code, sa3_name, state_name, [sa2_code]])
        
        # 4.
        # calculate population for each sa3
        # reminder: sa2_data1 = [sa2_code, age_group_population, total_population]
        sa3_population_results = []
        # [state, sa3_code, sa3_name, age_group_population, total_population]
        for entry in sa3_list:
            sa3_code = entry[0]
            sa3_name = entry[1]
            state = entry[2]
            sa2_list = entry[3]

            age_group_total = 0 # total population of the specified age group
            total_population1 = 0
            for sa2 in sa2_list:
                for row in sa2_data1:
                    if row[0] == sa2:
                        age_group_total += row[1]
                        total_population1 += row[2]

            sa3_population_results.append([state, sa3_code, sa3_name, age_group_total, total_population1])

        # 5.
        # finding sa3 with max age group population per state
        final_output = []
        # for each state not yet processed
        states_checked = []
        for entry in sa3_population_results:
            state = entry[0]
            if state not in states_checked:
                # collects all sa3s' for that state into a candidate list
                candidates = []
                for i in sa3_population_results:
                    if i[0] == state:
                        candidates.append(i)
                # sorting the candidates with a primary key of maximum age group population and secondary key of sa3 code
                candidates.sort(key=lambda x: (-x[3], int(x[1])))
                # the top candidate, the sa3 with the highest age specific population
                best = candidates[0]
                if best[4] != 0:
                    percent = round(best[3] / best[4], 4)
                else:
                    # for assurance
                    percent = 0.0

                final_output.append([state.lower(), best[2].lower(), percent])
                states_checked.append(state)
        # sorting by state name
        final_output.sort(key=lambda x: x[0])
        return final_output
        
    OP3 = OP3(csvfile_1, csvfile_2, age)
    
    
    #Output4 / Task4
    def OP4(csvfile_2, sa2_1, sa2_2):
        sa2_1_values = []
        sa2_2_values = []
        
        # finding index of sa2 code column, and age group columns
        # then, storing all sa2_1 values for later (to calculate mean+coefficient)
        with open(csvfile_2, 'r') as file:
            headers = file.readline()
            headers = headers.strip()
            headers = headers.lower()
            headers = headers.split(',')
            sa2_index = 0
            age_indices = []
            
            # 1.
            for i, header in enumerate(headers):
                if header == 'area_code_level2':
                    sa2_index = i
                elif 'age' in header:
                    age_indices.append(i)
            # 2.       
            for line in file:
                data = line.strip()
                data = data.split(',')
                
                if data[sa2_index] == sa2_1:
                    for i in age_indices:
                        value = data[i].strip()
                        if value.isdigit():
                            sa2_1_values.append(int(value))
                        else:
                            sa2_1_values.append(0)
                            
                elif data[sa2_index] == sa2_2:
                    for i in age_indices:
                        value = data[i].strip()
                        if value.isdigit():
                            sa2_2_values.append(int(value))
                        else:
                            sa2_2_values.append(0)
        
        # 3.
        # calculations (mean+coefficient)
        n = len(sa2_1_values)
        # for assurance
        if n == 0 or len(sa2_2_values) != n:
            return 0.0
        mean1 = sum(sa2_1_values) / n
        mean2 = sum(sa2_2_values) / n
        numerator = 0
        denominator1 = 0
        denominator2 = 0
        
        # 4.
        # now calculating coefficient, numerator and denominator
        # top is [x(i)-mean(x)] * [y(i)-mean(y)]
        # bot is sqrt[x(i)-mean(x)]^2 * sqrt[y(i)-mean(y)]^2
        for i in range(n):
            x = sa2_1_values[i] - mean1
            y = sa2_2_values[i] - mean2
            numerator += x * y
            denominator1 += x ** 2
            denominator2 += y ** 2
        
        if denominator1 == 0 or denominator2 == 0:
            return 0.0
        
        correlation_coefficient = numerator / ((denominator1**0.5) * (denominator2**0.5))
        return round(correlation_coefficient, 4)
    OP4 = OP4(csvfile_2, sa2_1, sa2_2)

    return OP1, OP2, OP3, OP4