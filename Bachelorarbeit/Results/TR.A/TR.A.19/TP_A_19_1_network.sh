# Configure network
uci -q delete network.guest
uci set network.guest="interface"
uci set network.guest.type="bridge"
uci set network.guest.proto="static"
uci set network.guest.ipaddr="192.168.3.1"
uci set network.guest.netmask="255.255.255.0"
uci commit network
/etc/init.d/network restart
