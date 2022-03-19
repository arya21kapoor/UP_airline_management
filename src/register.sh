
# Program Code for user registration

read -p  "Enter username: " newUserName
read -sp "Enter password: " newPassword; echo;
read -p "Enter full named: " fullname
read -p "Enter Date of Birth: " dob
read -p "Enter Gender (M or F): " gender

flag=$( grep -e "^U.*,$newUserName" userinfo.txt | wc -l ) # checks if the username is already taken

if [ $flag -ne 0 ]
then
	echo "Username is already used."
else
	id=$( expr `cat userinfo.txt 2>/dev/null | wc -l` + 1)
	echo "U$id,${newUserName,,},$fullname,${gender^},$dob,$newPassword" >> userinfo.txt
	echo -e "\nNew User $newUserName has been successfully created"
	echo "Log in to continue.."
fi
