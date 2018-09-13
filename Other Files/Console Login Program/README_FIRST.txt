This is a LOGIN PAGE Application using Python Language.

Things to do before launching FinalCode.py:
1. Make sure that 'file.txt' is downloaded and placed into a specific path.
2. Edit FinalCode.py using Notepad. Then copy the path of 'file.txt' then paste it to line:
	with open(r'''PUT PATH WHERE THE FILE.TXT ARE SAVED''') as csv_file:

	Example:
	with open(r'''C:\Users\125\file.txt''') as csv_file:

3. Good Job! You're good to go.

Program Guide
1. After launching the 'FinalCode.py', the user must provide username and password.
2. If correct username and password:
	The program will welcome the user using the indicated name in 'file.txt' and the
	username and password will be shown. Then the user will be asked if he/she wants
	to logout. Choosing Y/y will exit the program.

   If correct username and wrong password:
	The program will prompt "Incorrect Password!" and let the user to re-login again
	with a maximum of 5 attempts.

   If wrong username:
	The program will prompt "Incorrect Username!" and let the user to re-login again
	with a maximum of 5 attempts.



Program Contributions
Angulo, Ralz			= Output user detail
Antolin, Arryll Mori		= Push files to master and produced the FinalCode.py
Castro, Paul			= Error-checking for accounts
Jawod, Danielle Nicole		= Read CSV file (file.txt)
Reyes, Jean Marc		= Login Page function