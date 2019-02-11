#!/bin/bash
#
#this file will run the test for the relevant functions in pharm_counting.py
#use run.sh to run the source file pharmacy_unittest.py first

python ./src/pharm_unittest.py ./insight_testsuite/tests/unittest/input/test_input.txt ./insight_testsuite/tests/unittest/output/test_output.txt
