pkg install figlet
pkg install screenfetch
figlet "   VS CODE"
screenfetch -L
echo "+--------------------------------------------+"
echo "|          This is made by Partha            |"
echo "|    Just chill this file program will do    |"
echo "|     everything for you automatically!      |"
echo "+--------------------------------------------+"
sleep 2
echo "+--------------------------------------------+"
echo "|     Grant storage permissions to termux    |"
echo "|    Click on allow as the message pops up   |"
echo "+--------------------------------------------+"
sleep 5
termux-setup-storage
sleep 2
echo "+--------------------------------------------+"
echo "|       Change the repository to grimler     |"
echo "|          Go to main repository and         |"
echo "|        Select Grimler and click on OK      |"
echo "+--------------------------------------------+"
sleep 2
termux-change-repo
apt-get upgrade -y && apt-get update
apt-get install wget -y
apt-get install proot -y
apt-get install git -y
cd
git clone https://github.com/MFDGaming/ubuntu-in-termux.git
cd ubuntu-in-termux
apt update && apt upgrade
chmod +x ubuntu.sh
./ubuntu.sh -y
./startubuntu.sh
apt install wget
wget https://github.com/cdr/code-server/releases/download/v3.11.1/code-server-3.11.1-linux-amd64.tar.gz
tar -xvf ./code-server-3.11.1-linux-arm64.tar.gz
rm ./code-server-3.11.1-linux-arm64.tar.gz
cp -r code-server-3.11.1-linux-arm64 /lib/
ln -s /lib/code-server-3.11.1-linux-arm64/code-server /bin/
code-server
^C
clear
tail ~/.config/code-server/config.yaml
echo "\n\n\n+--------------------------------------------+"
echo "|         Copy the password from here        |"
echo "|     You will be asked for the password     |"
echo "|        and save it somewhere because       |"
echo "|            while you open VS code          |"
echo "|           Now open you web browser         |"
echo "|              and search for this           |"
echo "|                127.0.0.1:8080              |"
echo "|           copy this address exactly        |"
echo "|   and paste it in the search box of your   |"
echo "|                  WEB BROWSER               |"
echo "|Till then wait for the code-server to start |"
echo "+--------------------------------------------+"
code-server

