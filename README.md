# Table of Contents
1. [Problem](README.md#problem)
1. [Design](README.md#design)
1. [Repo directory structure](README.md#structure)
1. [Instruction](README.md#instruction)
1. [Results](README.md#result)

# Problem
Given the records of all the prescription by patient and cost, the program will generate a list of **all drugs**,  the total number of UNIQUE **individuals who prescribed the medication**, and the total drug **cost**. The list will be ranked by the cost in a descending order. If there's a tie, the drugs with the same amount of total cost will be ranked based on drug name in an ascending order. 

For example

If the input data, **`itcont.txt`**, is
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

then the output file, **`top_cost_drug.txt`**, would contain the following lines
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

These files are provided in the `insight_testsuite/tests/test_1/input` and `insight_testsuite/tests/test_1/output` folders, respectively.

# Design 

## Input processing 

This program utilizes the embedded dictionary class in Python. To create a list summarizing each drug's information, I design the dictionary with drug names as the **key** and a list as its **values**. It achieves the tidiness of the data structure, when each drug name only has one entry for look-up. The list of value contains the **total number of unique patients** as its **first** element and the **total cost** as its **second** element. 

In order to count the number of unique patients prescribed for each drug, I create a separate dictionary with drug name as its key and a list of patients names as its value. Then, after converting the list to a set and calculate its size, I create a dictionary with the number of unique patients. 

Similarly, exploiting the attributes of dictionary, I create another one for the total cost of each drug. Since two dictionaries share the exactly same key, I can merge them to get the final dictionary as planned. 

## Sorting 

To present all the drugs sorted in a descending order by cost first and in an ascending order by name second, I leverage ``sorted`` function based on the dictionary value. I specify the cost sorting as descending, while Python sorts the drug name among those with the same cost in an ascending order alphabetically by default. 


# Repo directory structure

The directory structure of this project is as follows: 

    ├── README.md 
    ├── run.sh
    ├── run_unittest.sh 
    ├── src
    │   └── pharmacy-counting.py
    |   └── pharm_unittest.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
            ├── unittest
                ├── input
                │   └── itcont.txt
                |── output
                    └── top_cost_drug.txt


## Instruction 

### The original test from Insight 

I executed the provided test using the following command :

```
insight_testsuite~$ sh run_tests.sh 
```

The output is

    -e [PASS]: test_1 top_cost_drug.txt
    -e [PASS]: unittest top_cost_drug.txt
    [Sat Feb  9 16:42:26 CST 2019] 2 of 2 tests passed

### The extra unittest in `tests/unittest` folder

In addition to the provided test, I included a separate unittest in `insight_testsuites/tests/unittest` folder to test the functions defined in the `pharmacy-counting.py`. The input file is part of `de_cc_data.txt` which was downloaded from the link to 24 million dollars. 

To perform the test, use `run_unittest.sh` in the main directory as follows. 

```
pharmacy_counting~$ sh run_unittest.sh 
```    

## Results

The first seven lines in the output file from `unittest` looks like the following

```
drug_name,num_prescriber,total_cost
TECFIDERA,1,263130.96
ABILIFY,3,246337.24
LANTUS SOLOSTAR,5,201088.25
LATUDA,3,152003.02
LANTUS,5,148321.66
TRADJENTA,1,136089.47
```