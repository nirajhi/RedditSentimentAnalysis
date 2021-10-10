import os
#https://cppsecrets.com/users/830011497115104109105114100971155364103109971051084699111109/Python-FTP-Downloading-Text-Files.php
from ftplib import FTP

with FTP("ftp.nasdaqtrader.com") as ftp:
	#nasdaqlisted.txt
	#otherlisted.txt
	file_location = "SymbolDirectory/otherlisted.txt"
	save_file = "ticker-data/otherlisted.txt"
	try:
		ftp.login()
		with open(save_file, 'w') as f:
			res = ftp.retrlines('RETR ' + file_location, callback=lambda line: f.write(line+"\n"))
			if not res.startswith('226 Transfer complete'):
				print('Downloaded Failed')
				if os.path.isfile(save_file):
					os.remove(save_file)
				exit()


	except Exception as ex:
		print(ex.args)
	finally:
		ftp.quit()



