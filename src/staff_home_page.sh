x=1
while [ $x -eq 1 ]	
do
	echo "                                             "
	echo "Press Following Keys for Following Operations"
	echo "                                             "
	echo "1)    Search for a Flight"
	echo "2)    Book a flight"
	echo "3)    Cancel a flight"
	echo "4)    Display flight details"
	echo "5)    To EXIT"
	echo "											   "

	read operation_num

	if [ $operation_num -eq 1 ]
	then
		echo "                                             "
		echo "Enter Flight id / Flight Name / Author Name"
		echo "                                             "

		read search_query

		echo "                                             "
		echo " *****************  Books *******************"
		grep  $search_query books.txt
		echo "*********************************************"
		echo "                                             "

	elif [ $operation_num -eq 2 ]
	then
		python3 issue_data_base_management.py

	elif [ $operation_num -eq 3 ]
	then
		python3 return_data_base_management.py

	elif [ $operation_num -eq 4 ]
	then
		echo "											   "
		echo "*********************************************"
		cat books.txt
		echo "*********************************************"
		echo "											   "
	elif [ $operation_num -eq 5 ]
	then
		x=2
		echo "											   "
		echo "*********************************************"
		echo "				Exiting ....					"
		echo "*********************************************"
		echo "											   "
	fi
done