clear
echo "[*] INSTALLING REQUIRED NGAGE-TOOLKIT MODULES"

pkg update -y && pkg upgrade -y && pkg install nmap fish git -y && pip install -r requirements.txt

git clone https://github.com/rajkumardusad/IP-Tracer && cd IP-Tracer && chmod +x install && bash install

cd modules && git clone https://github.com/sullo/nikto.git && cd $home

clear
echo "SETUP COMPLETE"
