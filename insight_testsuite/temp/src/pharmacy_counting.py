import sys
import random
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

#embeded unittest due to the repo structure limitation
def _print_success_message(): 
    print('Tests Passed')

def test_dict_name():
    
    sample = '''1000000001,Smith,James,AMBIEN,100
             1000000002,Garcia,Maria,AMBIEN,200
             1000000003,Johnson,James,CHLORPROMAZINE,1000
             1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
             1000000005,Smith,David,BENZTROPINE MESYLATE,1500'''
    sample_text = sample.split('\n')

    output = process_name(sample_text)
    #check instance 
    assert isinstance(output, dict), \
        'output is not a dictionary'

    _print_success_message()


def test_dict_cost():

    sample = '''1000000001,Smith,James,AMBIEN,100
             1000000002,Garcia,Maria,AMBIEN,200
             1000000003,Johnson,James,CHLORPROMAZINE,1000
             1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
             1000000005,Smith,David,BENZTROPINE MESYLATE,1500'''
    sample_text = sample.split('\n')

    output = process_cost(sample_text)
    #check instance 
    assert isinstance(output, dict), \
        'output is not a dictionary'

    _print_success_message()

def test_main(input_path, output_path): 

    pharm_count(input_path, output_path)

    with open(output_path,'r') as f: 
        sample_output = f.readlines()

    if len(sample_output) <= 1: 
        print('There is no valid value in the output.')
    else: 
        #check the value has two numbers and two numbers only
        a = random.randint(1, len(sample_output)-1)
        a_text= sample_output[a].split(',')
        assert float(a_text[1]) >= 1, \
            'the number of unique patients has exceptional value'
        assert round(float(a_text[2].rstrip('\n')),2) > 0, \
            'the number of total cost has exceptional value'


        #check the descending order of cost 
        b = random.randint(1, len(sample_output)-2) 
        b_text = sample_output[b].split(',')
        b_next_text = sample_output[b+1].split(',')
        
        assert round(float(b_text[2].rstrip('\n')),2) >= round(float(b_next_text[2].rstrip('\n')),2), \
            'cost is not ranked in a descending order'
    
        #check the ascending order of names among those with the same cost 

        #find the cost where there is a tie
        counts = dict()
        for line in sample_output: 
            drug_name, num_patient, cost = line.split(',')
            cost = cost.rstrip('\n')
            counts[cost] = counts.get(cost, 0) + 1
        
        if max([c for k, c in counts.items()]) == 1: 
            print('No tie')
        else:
            #pick a random cost amount with a tie and find the drug names 
            tie = [cost for cost, count in counts.items() if count > 1]
            c = random.randint(0, len(tie)-1)
    
            drug = {}
            for line in sample_output[1:]: 
                drug_name, patient, cost = line.split(',')
                cost = cost.rstrip('\n')
                drug[drug_name] = cost 

            names = [name for name, cost in drug.items() if cost == tie[c] ] 
            check = True 
            for i in range(len(names) - 1): 
                if names[i] > names[i+1]: 
                    check = False 

            assert check == True, \
                'Among the ties, names are not in an ascending alphabetic order.'

        _print_success_message()

if __name__ == "__main__":

    pharm_count(input_path, output_path)

    print('Regarding the unique patient names,') 
    test_dict_name()
    print('Regarding the total cost,')
    test_dict_cost()
    print('Regarding the essential sorting function,') 
    test_main(input_path, output_path)

