# Configure wireless
WIFI_PSK="GUEST_WIFI_PASSWORD"
uci set wireless.guest.encryption="psk2"
uci set wireless.guest.key="${WIFI_PSK}"
uci commit wireless
wifi reload