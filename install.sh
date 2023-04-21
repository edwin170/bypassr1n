#!/bin/bash/
if [ "$EUID" -ne 0 ]
  then
  echo "Please run with SUDO (as root)"
  exit
fi
if [[ -f "/etc/lsb-release" || -f "/etc/debian_version" ]]
    then
        echo "Linux Ubuntu detected and is supported"
    else
        echo "This Linux Distro is not supported, exiting..."
        exit
    fi
echo "Written by ios_rifox"
sudo add-apt-repository universe && sudo apt-get update && sudo apt install libimobiledevice-utils libusbmuxd-tools git curl python3-pip unzip libc6-i386 -y && python3 -m pip install pyimg4 && sudo wget http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.17_amd64.deb && sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.17_amd64.deb && sudo rm libssl1.1_1.1.1f-1ubuntu2.17_amd64.deb && sudo wget https://github.com/darlinghq/darling/releases/download/v0.1.20220704/darling_0.1.20220704.focal_amd64.deb && sudo dpkg -i darling_0.1.20220704.focal_amd64.deb && sudo rm darling_0.1.20220704.focal_amd64.deb
echo "All Done!"
echo ""
echo "[+] Installing linux packages..."
echo ""
sleep 3
# Install Linux dependencies
sudo apt update
# git for ideviceactivation
sudo apt-get install git-all
echo ""
git version
echo "Git done!"
echo ""
# ideviceinfo
sudo apt install snapd
sudo apt install sshpass
sudo apt install irecovery
pip install pyinstaller
sudo snap install libimobiledevice --edge
sudo apt install libimobiledevice-utils
# irecovery
sudo apt install irecovery
pip3 install pyinstaller
# ideviceactivation
sudo apt-get install \
	build-essential \
	pkg-config \
	checkinstall \
	git \
	autoconf \
	automake \
	libtool-bin \
	libplist-dev \
	libimobiledevice-dev \
	libxml2-dev \
	libcurl4-openssl-dev \
	usbmuxd
cd Linux
git clone https://github.com/libimobiledevice/libideviceactivation.git
cd libideviceactivation
./autogen.sh
make
sudo make install
export LD_LIBRARY_PATH=/usr/local/lib
ideviceactivation
cd /home/$whoami
# PLEASE COPY AND MANUALLY RUN THIS LINE BELOW TO FIX IDEVICEACTIVATION
export LD_LIBRARY_PATH=/usr/local/lib
echo ""
echo "[+] Linux packages installed!"
echo ""
