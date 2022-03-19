options=("Display all flights avaiable" "Book a flight" "See Plane Ticket" "Cancel Ticket" "Exit Program")

while true;
do
	PS3='Please enter your choice: '
	echo ""
	select opt in "${options[@]}"
	do
    	case $opt in
        	"Display all flights avaiable")
                	echo -e "\nFlights avaiable:\n"

                	awk -v date=`date +"%d/%m/%Y"` -F',' '
                	BEGIN{
                	printf "%-15s %-15s %-15s %-15s %-15s %-15s %-15s\n", "Flight ID", "Airline", "Source", "Destination","Date","Premium Seats", "Economy Seats"
                	printf "---------------------------------------------------------------------------------------------------------\n"
                	}
			{
				if ($5 >= date)
                		{
					printf "%-15s %-15s %-15s %-15s %-15s %-15s %-15s\n", $1,$2,$3,$4,$5,$6,$7
				}
			}
                	' flights.txt
			# used to display the flights which are from or after the current date (latest flights)
                	echo
			break
                	;;
        	"Book a flight")
			echo
			read -p "Enter Flight ID number: " flightid
			flightid=${flightid^}
			
			flag=( `grep "^$flightid" flights.txt | wc -l` )
			
			if [ $flag -ne 1 ]
			then
				echo -e "\nFlight does not exist"
				break
			fi


			a=$(awk -v fid=$flightid -v date=`date +"%d/%m/%Y"` -F',' '
			{
				if ($1 == fid)
				{			
                                	if ($5 >= date)
                                	{
                                        	print "true"
                                	}
					else
					{
						print "false"
					}
				}

                        }
			' flights.txt);

			if [ $a = "false" ]
			then
				echo -e "\nFlight does not exist"
                                break
                        fi

			python3 bookFlight.py $1 $flightid

			break
                	;;
        	"See Plane Ticket")
			read -p "Enter Flight ID number: " flightid
                        flightid=${flightid^}

                        flag=( `grep "^$flightid" flights.txt | wc -l` )

                        if [ $flag -ne 1 ]
                        then
                                echo -e "\nFlight does not exist"
                                break
                        fi

			a=$(awk -v fid=$flightid -v date=`date +"%d/%m/%Y"` -F',' '
                        {
                                if ($1 == fid)
                                {
                                        if ($5 >= date)
                                        {
                                                print "true"
                                        }
                                        else
                                        {
                                                print "false"
                                        }
                                }

                        }
                        ' flights.txt);

                        if [ $a = "false" ]
                        then
                                echo -e "\nFlight does not exist"
                                break
                        fi

			
			sed -n -e "/$1 $flightid/p" db.txt > temp.txt

			python3 displayFlight.py $flightid

			break
                	;;

		"Cancel Ticket")
			echo
			read -p "Enter Flight ID number: " flightid
                        flightid=${flightid^}

                        flag=( `grep "^$flightid" flights.txt | wc -l` )

                        if [ $flag -ne 1 ]
                        then
                                echo -e "\nFlight does not exist"
                                break
                        fi

			a=$(awk -v fid=$flightid -v date=`date +"%d/%m/%Y"` -F',' '
                        {
                                if ($1 == fid)
                                {
                                        if ($5 >= date)
                                        {
                                                print "true"
                                        }
                                        else
                                        {
                                                print "false"
                                        }
                                }

                        }
                        ' flights.txt);

                        if [ $a = "false" ]
                        then
                                echo -e "\nFlight does not exist"
                                break
                        fi

                        sed -n -e "/$1 $flightid/p" db.txt > temp.txt
			
			python3 cancelFlight.py $flightid

			rm temp.txt

			break
			;;
			
        	"Exit Program")
                	break 2
                	;;
        	*)
                	echo -e "invalid option $REPLY\n"
                	;;
   	esac
	done
done
