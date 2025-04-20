echo "***********update packages**********"
sudo apt update -y

echo "***************upgrade packages***********"
sudo apt upgrade -y

echo "***************Remove Obsolete Packages************"
sudo apt autoremove -y

echo "**** System is Up to date and cleanup is completed *****"