read -p "Enter username: " inputUserName
read -sp "Enter password: " inputPassword; echo;

result=( $(awk -v username=${inputUserName,,} -F"," '{if (username == $2) {print $1, $6}}' userinfo.txt) )
# for extracting the userid and password for further usage and verification.

userid=${result[0]}
paa=${result[1]}

if [ -z $userid ]
then
	echo "User does not exist"
else
	if [ $paa  =  $inputPassword ]
	then
		echo -e "\nLogin Successful"
		bash menu.sh $userid
	else
		echo "Login UnSuccessful"
	fi
fi	
