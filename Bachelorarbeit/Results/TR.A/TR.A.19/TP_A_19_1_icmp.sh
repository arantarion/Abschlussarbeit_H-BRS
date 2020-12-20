# Configure firewall
uci rename firewall.@rule[1]="icmp"
uci rename firewall.@rule[5]="icmp6"
uci set firewall.icmp.src="*"
uci set firewall.icmp6.src="*"
uci commit firewall
/etc/init.d/firewall restart