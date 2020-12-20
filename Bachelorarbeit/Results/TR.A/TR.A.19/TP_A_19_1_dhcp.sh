uci -q delete dhcp.guest
uci set dhcp.guest="dhcp"
uci set dhcp.guest.interface="guest"
uci set dhcp.guest.start="100"
uci set dhcp.guest.limit="150"
uci set dhcp.guest.leasetime="1h"
uci commit dhcp
/etc/init.d/dnsmasq restart
