
# This is the start of the program. Used for user login and register

echo -e "\nWelcome to the Flight Management System"
options=("Login" "Register" "Exit Program")
touch userinfo.txt
while true;
do
	PS3='Please enter your choice: '
	echo ""
	select opt in "${options[@]}"
	do
    	case $opt in
        	"Login")
                	echo -e "\nLogin Page:\n"

			bash login.sh

			break 2
                	;;
        	"Register")
			echo -e "\nRegister Page:\n "

			bash register.sh

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
