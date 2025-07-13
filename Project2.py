def main(csvfile_1, csvfile_2):
    #csvfile_1 = area
    #csvfile_2 = population
    #output1
    def OP1(csvfile_1, csvfile_2):
        #1
        area_mapping = {} #sa2_code->(state_name, sa3_name, sa2_name)
        with open(csvfile_1, 'r') as file1:
            headers = file1.readline().strip().lower().split(',')
            sa2_code_index = 0
            sa2_name_index = 0
            sa3_name_index = 0
            state_name_index = 0
            for i, header in enumerate(headers):
                if header == 'sa2 code':
                    sa2_code_index = i
                if header == 'sa2 name':
                    sa2_name_index = i
                if header == 'sa3 name':
                    sa3_name_index = i
                if header == 's_t name':
                    state_name_index = i
                    
            for line in file1:
                data = line.strip().split(',')
                sa2_code = data[sa2_code_index]
                sa2_name = data[sa2_name_index].strip().lower()
                sa3_name = data[sa3_name_index].strip().lower()
                state_name = data[state_name_index].strip().lower()
                area_mapping[sa2_code] = (state_name, sa3_name, sa2_name)
                
        #2
        keys = {} #age_group->list of [state, sa3, sa2, population]
        with open(csvfile_2, 'r') as file2:
            headers = file2.readline().strip().lower().split(',')
            for i, header in enumerate(headers):
                if header == 'area_code_level2':
                    area_code_level2_index = i
            age_indices = {}
            for i, column in enumerate(headers):
                if column.startswith("age "):
                    age_group = column.replace("age ", "").strip()
                    if ' and over' in age_group:
                        age_group = age_group.replace(" and over", "-None").strip()
                    age_indices[i] = age_group
                    keys[age_group] = []
            
            #3
            for line in file2:
                data = line.strip().split(',')
                sa2_code = data[area_code_level2_index].strip()
                if sa2_code in area_mapping:
                    state, sa3, sa2 = area_mapping[sa2_code] #area_mapping[sa2_code] = (state_name, sa3_name, sa2_name)
                    #state = state_name
                    #sa3 = sa3_name
                    #sa2 = sa2_name
                    for i, age_group in age_indices.items():
                        try:
                            population = int(data[i])
                        except:
                            population = 0
                        keys[age_group].append((state, sa3, sa2, population))
                        
        #4
        op1 = {}
        for age_group in keys:
            #state total, sa3 total, max sa2 area
            state_total_population = {}
            sa3_total_population = {}
            sa2_max = ('', 0)
            max_sa2 = ''
            
            for state, sa3, sa2, population in keys[age_group]:
                state_total_population[state] = state_total_population.get(state, 0) + population
                sa3_total_population[sa3] = sa3_total_population.get(sa3, 0) + population
                #looping and storing the largest pop in sa2 area
                #if tied, pick sa2 area alphabetically 
                if population > sa2_max[1] or (population == sa2_max[1] and sa2 < sa2_max[0]):
                    sa2_max = (sa2, population)
                    max_sa2 = sa2
            
            #max state, and tie-breaking
            max_state_pop = max(state_total_population.values())
            for state in sorted(state_total_population):
                if state_total_population[state] == max_state_pop:
                    max_state = state
                    break
            
            #max sa3, and tie-breaking
            max_sa3_pop = max(sa3_total_population.values())
            for sa3 in sorted(sa3_total_population):
                if sa3_total_population[sa3] == max_sa3_pop:
                    max_sa3 = sa3
                    
            op1[age_group] = [max_state, max_sa3, max_sa2]
        
        return op1


    #output2
    def OP2(csvfile_1, csvfile_2):
        #1
        area_mapping = {} #sa2_code->(state_code, sa3_code)
        with open(csvfile_1, 'r') as file1:
            headers = file1.readline().strip().lower().split(',')
            sa2_code_index = 0
            sa3_code_index = 0
            state_code_index = 0
            for i, header in enumerate(headers):
                if header == 'sa2 code':
                    sa2_code_index = i
                if header == 'sa3 code':
                    sa3_code_index = i
                if header == 's_t code':
                    state_code_index = i
            
            for line in file1:
                data = line.strip().split(',')
                sa2_code = data[sa2_code_index]
                sa3_code = data[sa3_code_index]
                state_code = data[state_code_index]
                area_mapping[sa2_code] = (state_code, sa3_code)
        
        #2
        state_data = {} #state_code->{sa3_code->[sa2_code, population, age_groups]}
        with open(csvfile_2, 'r') as file2:
            headers = file2.readline().strip().lower().split(',')
            area_code_lvl2_index = 0
            age_indices = {}
            
            for i, header in enumerate(headers):
                if header == 'area_code_level2':
                    area_code_lvl2_index = i
                elif header.startswith("age "):
                    age_group = header.replace("age ", "").strip()
                    if ' and over' in age_group:
                        age_group = age_group.replace(" and over", "-None").strip()
                    age_indices[i] = i
            
            for line in file2:
                data = line.strip().split(',')
                sa2_code = data[area_code_lvl2_index].strip()
                if sa2_code in area_mapping:
                    state_code, sa3_code = area_mapping[sa2_code]
                    #get population in that sa2 area + total population in that sa2 area
                    total_population = 0
                    populations = []
                    for i in age_indices:
                        value = data[i]
                        if value:
                            populations.append(int(value))
                        else:
                            populations.append(0)
                    for population in populations:
                        total_population += population
                    
                    #initiate nested dictionary
                    if state_code not in state_data:
                        state_data[state_code] = {}
                    if sa3_code not in state_data[state_code]:
                        state_data[state_code][sa3_code] = []
                    state_data[state_code][sa3_code].append((sa2_code, total_population, populations))
        
        
        #3
        op2 = {}
        for state_code in sorted(state_data.keys(), key=str):
            op2[state_code] = {}
            for sa3_code in sorted(state_data[state_code].keys(), key=str):
                sa3_data = state_data[state_code][sa3_code] #sa3_code->(sa2_code, total_population, populations)
                total_sa3_population = sum(data[1] for data in sa3_data) #sums up the population for each sa2 area in that sa3 code
                if total_sa3_population >= 150000:
                    sa2_max = ('', 0)
                    max_sa2_code = ''
                    max_sa2_population = 0
                    max_sa2_standard_dev = 0
                    
                    for sa2_code, total_population, populations in sa3_data:
                        #chooses the alphabetically first sa2 code in case of a tie
                        if total_population > sa2_max[1] or (total_population == sa2_max[1] and sa2_code < sa2_max[0]):
                            sa2_max = (sa2_code, total_population)
                            max_sa2_code = sa2_code
                            max_sa2_population = total_population
                            #calculate standard deviation 
                            n = len(populations)
                            if n == 0:
                                average_population = 0
                                standard_dev = 0
                            else:
                                average_population = sum(populations) / n
                                if n > 1:
                                    standard_dev = sum((x - average_population) ** 2 for x in populations)
                                    standard_dev = (standard_dev) / (n - 1)
                                    standard_dev = (standard_dev) ** 0.5
                                else:
                                    standard_dev = 0
                            max_sa2_standard_dev = standard_dev
                        
                        if max_sa2_code:
                            op2[state_code][sa3_code] = [max_sa2_code, max_sa2_population, round(max_sa2_standard_dev, 4)]
        
        for state_code in op2:
            op2[state_code] = dict(sorted(op2[state_code].items(), key=lambda item: item[1][1], reverse=True))
        
        return op2
    
    
    #output3
    def OP3(csvfile_1, csvfile_2):
        #1
        area_mapping = {} #sa2_code->(sa3_name, sa2_name)
        with open(csvfile_1, 'r') as file1:
            headers = file1.readline().strip().lower().split(',')
            sa2_code_index = 0
            sa2_name_index = 0
            sa3_name_index = 0
            for i, header in enumerate(headers):
                if header == 'sa2 code':
                    sa2_code_index = i
                if header == 'sa2 name':
                    sa2_name_index = i
                if header == 'sa3 name':
                    sa3_name_index = i
            
            for line in file1:
                data = line.strip().split(',')
                sa2_code = data[sa2_code_index]
                sa2_name = data[sa2_name_index].strip().lower()
                sa3_name = data[sa3_name_index].strip().lower()
                area_mapping[sa2_code] = (sa3_name, sa2_name)
        
        #2
        sa3_data = {} #sa3_name->(sa2_name, percentages)
        with open(csvfile_2, 'r') as file2:
            headers = file2.readline().strip().lower().split(',')
            sa2_code_index = 0
            for i, header in enumerate(headers):
                if header == 'area_code_level2':
                    sa2_code_index = i
            
            age_indices = []
            for i, header in enumerate(headers):
                if header.startswith('age '):
                    age_indices.append(i)
            
            for line in file2:
                data = line.strip().split(',')
                sa2_code = data[sa2_code_index].strip()
                if sa2_code in area_mapping:
                    sa3_name, sa2_name = area_mapping[sa2_code]
                    populations = []
                    total_population = 0
                    for i in age_indices:
                        population = int(data[i])
                        populations.append(population)
                        total_population += population
                    if total_population == 0:
                        percentages = []
                        for i in populations:
                            percentages.append(0.0)
                    else:
                        percentages = []
                        for i in populations:
                            percentages.append(i / total_population)
                    if sa3_name not in sa3_data:
                        sa3_data[sa3_name] = []
                    sa3_data[sa3_name].append((sa2_name, percentages))
                    
        #3
        def cosine_similarity(p1, p2):
            numerator = sum(p1[i] * p2[i] for i in range(len(p1)))
            denominator1 = sum(p1[i] * p1[i] for i in range(len(p1))) ** 0.5
            denominator2 = sum(p2[i] * p2[i] for i in range(len(p2))) ** 0.5
            if denominator1 == 0 or denominator2 == 0:
                return 0.0
            return numerator / (denominator1 * denominator2)
        
        #get best pair by cosine similarity in each sa3 with >= 15 sa2s
        op3 = {}
        for sa3_name in sa3_data:
            if len(sa3_data[sa3_name]) >= 15:
                best_pair = ('', '', 0.0)
                n = len(sa3_data[sa3_name])
                for i in range(n):
                    sa2_name_1, percentage_1 = sa3_data[sa3_name][i] #sa3_name->(sa2_name, percentages)
                    #sa2_name_1 = sa2_name
                    #percentage_1 = percentages
                    for j in range(i + 1, n):
                        sa2_name_2, percentage_2 = sa3_data[sa3_name][j]
                        cos_similarity = cosine_similarity(percentage_1, percentage_2)
                        first_pair, second_pair = sorted([sa2_name_1, sa2_name_2])
                        if cos_similarity > best_pair[2] or (cos_similarity == best_pair[2] and (first_pair, second_pair) < (best_pair[0], best_pair[1])):
                            best_pair = (first_pair, second_pair, cos_similarity)
                
                op3[sa3_name] = [best_pair[0], best_pair[1], round(best_pair[2], 4)]
        
        return op3
        
    return OP1(csvfile_1, csvfile_2), OP2(csvfile_1, csvfile_2), OP3(csvfile_1, csvfile_2)