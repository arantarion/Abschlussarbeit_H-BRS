# Configure firewall
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