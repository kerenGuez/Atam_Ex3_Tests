#!/bin/bash
gcc -g better_test1.c aux_hw3.o students_code.S -o hw3_part1.out

if [ -f "hw3_part1.out" ]; then
	timeout 20s echo "$3" | ./hw3_part1.out > $1
	diff $1 $2 > /dev/null
	if [ $? -eq 0 ]; then
		echo -e "\033[96mTest:\t\033[32mPASS\033[0m"
	else
		echo -e "\033[96mTest:\t\033[31mFAIL\033[0m"
		echo ""
		echo -e "\033[93mactual_output_path =\033[0m $1"
		echo -e "\033[93mexpected_output_path =\033[0m $2"
		echo ""
		echo -e "\033[31mExpected:\033[0m"
		cat -v $2
		echo ""
		echo -e "\033[31mGot:\033[0m"
		cat -v $1
		
	fi
else
	echo -e "\033[96mTest:\tFAIL - compile with test error"
fi
rm hw3_part1.out
