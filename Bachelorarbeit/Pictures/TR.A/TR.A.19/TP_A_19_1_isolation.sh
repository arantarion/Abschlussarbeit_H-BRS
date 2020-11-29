# Configure wireless
uci set wireless.guest.isolate="1"
uci commit wireless
wifi reload