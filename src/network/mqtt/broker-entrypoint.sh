#!/bin/ash
set -e

# Set permissions
user="$(id -u)"
if [ "$user" = '0' ]; then
    [ -d "/mosquitto" ] && chown -R mosquitto:mosquitto /mosquitto || true
    [ -d "/app" ] && chown -R mosquitto:mosquitto /app || true
fi

exec "$@"