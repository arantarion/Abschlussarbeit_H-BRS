# Configure network
uci -q delete network.guest
uci set network.guest="interface"
uci set network.guest.type="bridge"
uci set network.guest.proto="static"
uci set network.guest.ipaddr="192.168.3.1"
uci set network.guest.netmask="255.255.255.0"
uci commit network
/etc/init.d/network restart


# Configure wireless
WIFI_DEV="$(uci get wireless.@wifi-iface[0].device)"
uci -q delete wireless.guest
uci set wireless.guest="wifi-iface"
uci set wireless.guest.device="${WIFI_DEV}"
uci set wireless.guest.mode="ap"
uci set wireless.guest.network="guest"
uci set wireless.guest.ssid="guest"
uci set wireless.guest.encryption="none"
uci commit wireless
wifi reload


# Configure DHCP
uci -q delete dhcp.guest
uci set dhcp.guest="dhcp"
uci set dhcp.guest.interface="guest"
uci set dhcp.guest.start="100"
uci set dhcp.guest.limit="150"
uci set dhcp.guest.leasetime="1h"
uci commit dhcp
/etc/init.d/dnsmasq restart


# Configure firewall
uci -q delete firewall.guest
uci set firewall.guest="zone"
uci set firewall.guest.name="guest"
uci set firewall.guest.network="guest"
uci set firewall.guest.input="REJECT"
uci set firewall.guest.output="ACCEPT"
uci set firewall.guest.forward="REJECT"
uci -q delete firewall.guest_wan
uci set firewall.guest_wan="forwarding"
uci set firewall.guest_wan.src="guest"
uci set firewall.guest_wan.dest="wan"
uci -q delete firewall.guest_dns
uci set firewall.guest_dns="rule"
uci set firewall.guest_dns.name="Allow-DNS-Guest"
uci set firewall.guest_dns.src="guest"
uci set firewall.guest_dns.dest_port="53"
uci set firewall.guest_dns.proto="tcp udp"
uci set firewall.guest_dns.target="ACCEPT"
uci -q delete firewall.guest_dhcp
uci set firewall.guest_dhcp="rule"
uci set firewall.guest_dhcp.name="Allow-DHCP-Guest"
uci set firewall.guest_dhcp.src="guest"
uci set firewall.guest_dhcp.dest_port="67"
uci set firewall.guest_dhcp.family="ipv4"
uci set firewall.guest_dhcp.proto="udp"
uci set firewall.guest_dhcp.target="ACCEPT"
uci commit firewall
/etc/init.d/firewall restart


# Configure wireless encryption
WIFI_PSK="GUEST_WIFI_PASSWORD"
uci set wireless.guest.encryption="psk2"
uci set wireless.guest.key="${WIFI_PSK}"
uci commit wireless
wifi reload


# Configure client isolation
uci set wireless.guest.isolate="1"
uci commit wireless
wifi reload


# Configure firewall - icmp
uci rename firewall.@rule[1]="icmp"
uci rename firewall.@rule[5]="icmp6"
uci set firewall.icmp.src="*"
uci set firewall.icmp6.src="*"
uci commit firewall
/etc/init.d/firewall restart


# Configure firewall - restrictions
uci -q delete firewall.guest_wan
uci -q delete firewall.guest_fwd
uci set firewall.guest_fwd="rule"
uci set firewall.guest_fwd.name="Allow-HTTP/HTTPS-Guest-Forward"
uci set firewall.guest_fwd.src="guest"
uci set firewall.guest_fwd.dest="wan"
uci add_list firewall.guest_fwd.dest_port="80"
uci add_list firewall.guest_fwd.dest_port="443"
uci set firewall.guest_fwd.proto="tcp"
uci set firewall.guest_fwd.target="ACCEPT"
uci commit firewall
/etc/init.d/firewall restart

# Configure firewall
uci rename firewall.@zone[0]="lan"
uci set firewall.lan.masq="1"
uci commit firewall
/etc/init.d/firewall restart