keyboard.send_keys("<ctrl>+z")
time.sleep(0.5)


keyboard.send_keys('stty raw -echo;fg')
keyboard.send_keys("<enter>")
time.sleep(1)


keyboard.send_keys('reset')
keyboard.send_keys("<enter>")
keyboard.send_keys("<enter>")
time.sleep(0.5)


