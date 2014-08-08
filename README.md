volepsou
========

capturing network on rasp-pi for photobooth application

## install

Make sure the wifi dongle is working with `ifconfig wlan0`.
(I am using `tp-link tl-wn725n v2 chipset` which is not recognise directly.)

#### package install
    sudo apt-get install hostapd
    sudo apt-get install dnsmasq

#### files to change
##### /etc/network/interfaces
add this under wlan0

    iface wlan0 inet static
    address 192.168.42.1
    netmask 255.255.255.0

##### /etc/default/hostapd
enable the configuration

    DAEMON_CONF="/etc/hostapd/hostapd.conf"

##### /etc/hostapd/hostapd.conf
define the AP

    interface=wlan0
    ssid=RaspberryAP
    hw_mode=g
    channel=11
    beacon_int=100
    auth_algs=3
    wmm_enabled=1

##### /etc/dnsmasq.conf
    interface=wlan0
    dhcp-range=192.168.42.2,192.168.42.50,255.255.255.0,12h
    address=/#/192.168.42.1  #redirect all DNS requests

##### /etc/hosts
    192.168.3.1    eins

#### to relaunch in case no IP is given
    sudo reboot
    sudo service hostapd stop
    sudo ifconfig wlan0 down
    sudo ifconfig wlan0 up
    sudo service hostapd start
    sudo service dnsmasq restart
