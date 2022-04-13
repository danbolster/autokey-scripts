import netifaces as ni


try:
  ni.ifaddresses('eth0')
  tun_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

except ValueError:
  dialog.info_dialog('eth0 not found', 'Can not obtain eth0 IP. Is the device connected?')
  
else:
    keyboard.send_keys(tun_ip)