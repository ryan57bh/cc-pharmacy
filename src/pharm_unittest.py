
from pharmacy_counting import process_name, process_cost, pharm_count
import sys
import random

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
        assert int(a_text[1]) >= 1, \
            'the number of unique patients has exceptional value'
        assert int(a_text[2]) > 0, \
            'the number of total cost has exceptional value'


        #check the descending order of cost 
        b = random.randint(1, len(sample_output)-2) 
        b_text = sample_output[b].split(',')
        b_next_text = sample_output[b+1].split(',')
        
        assert int(b_text[2].rstrip('\n')) >= int(b_next_text[2].rstrip('\n')), \
            'cost is not ranked in a descending order'
    
        #check the ascending order of names among those with the same cost 

        #find the cost where there is a tie
        counts = dict()
        for line in sample_output: 
            drug_name, num_patient, cost = line.split(',')
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
                drug[drug_name] = cost 

            names = [name for name, cost in drug.items() if cost == tie[c] ] 
            check = True 
            for i in range(len(names)): 
                if names[i] > names[i+1]: 
                    check = False 

            assert check == True, \
                'Among the ties, names are not in an ascending alphabetic order.'

        _print_success_message()


if __name__ == "__main__":

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    print('Regarding the unique patient names,') 
    test_dict_name()
    print('Regarding the total cost,')
    test_dict_cost()
    print('Regarding the essential sorting function,') 
    test_main(input_path, output_path)
  