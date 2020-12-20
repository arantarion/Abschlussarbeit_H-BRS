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
