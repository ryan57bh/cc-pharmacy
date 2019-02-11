import sys
input_path = sys.argv[1]
output_path = sys.argv[2]

def process_name(data): 
    '''
    read in text file linewise
    capture the drug name
    create a dictionary that counts the appearace of 
    
    example:
    1000000001,Smith,James,AMBIEN,100
    1000000002,Garcia,Maria,AMBIEN,200
    1000000003,Garcia,Maria,AMBIEN,100
    as
    name_list={AMBIEN: [James-Smith, Maria-Garcia, Maria-Garcia]} 
    name_count={AMBIEN: 2} 
    
    '''  
    drug = {}
    
    for line in data: 
        id, last, first, drug_name, cost = line.split(',')
        patient_name = first + " " + last
        drug.setdefault(drug_name, []).append(patient_name)  
        
    for k, v in drug.items(): 
        drug[k] = len(set(v))
    
    return drug


def process_cost(data): 
    '''
    read in text file linewise
    capture the drug name
    create a dictionary that counts the appearace of 
    
    example:
    1000000001,Smith,James,AMBIEN,100
    1000000002,Garcia,Maria,AMBIEN,200
    1000000003,Garcia,Maria,AMBIEN,100
    as
    drug = {AMBIEN: 400}
    
    '''  
    drug = {}
    for line in data: 
        *_, drug_name, cost = line.split(',')
        cost_num = round(float(cost.rstrip('\n')),2)
        drug[drug_name] = drug.get(drug_name, 0) + cost_num
  
    return drug


def pharm_count(input_path, output_path): 
    
    #process the txt data to proper format
    with open(input_path,'r') as f: 
        data = f.readlines()
    
    #ignore the header
    data = data[1:]
    
    #count unique patients 
    dict_name = process_name(data)
    
    #count cost 
    dict_cost = process_cost(data)
    
    #merge two dictionary. drug_name: [patient, cost]
    dict_name_cost = {}
    for k, v in dict_name.items(): 
        dict_name_cost.setdefault(k, [v]).append(dict_cost[k])
    
    #sort the merged dictionary by total cost and name 
    sorted_by_value = sorted(dict_name_cost.items(), key=lambda x: x[1][1], reverse = True)
    
    #generate an output file 
    output = open(output_path, "w")
    output.write('drug_name,num_prescriber,total_cost' + '\n')
    
    for i in sorted_by_value:
        output.write(i[0] + ','+ str(i[1][0]) + ',' + str(i[1][1]) + '\n')
    output.close()
    
    return None


if __name__ == "__main__":

    pharm_count(input_path, output_path)

