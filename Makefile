day=day18
file=./${day}_example.txt ./${day}_input.txt 

run:
	cd ./${day}/ && python ${day}.py $(file)

run1:
	cd ./${day}/ && python ${day}_1.py $(file)


format:
	black .