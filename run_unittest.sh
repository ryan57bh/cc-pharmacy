#!/bin/bash
#
#this file will run the test for the relevant functions in pharm_counting.py
#use run.sh to run the source file pharmacy_unittest.py first

python ./src/pharm_unittest.py ./insight_testsuite/tests/unittest/input/itcont.txt ./insight_testsuite/tests/unittest/output/top_cost_drug.txt
