import string
import secrets
import pikepdf
import time
import pyfiglet
from colorama import Fore, Style
def testing_pass(password):
    if len(password) <8:
        print(f"{Fore.RED}[!]{Fore.RESET} Too short, Enter 8 or more characters")
        return
    list_test =[
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(not char.isalnum() for char in password),
    ]
    weak_msg =f'''{Fore.RED}[!]{Fore.RESET} Your password is weak!, Make sure your password:
{Fore.GREEN}[+]{Fore.RESET} Have an upper and lower letter.
{Fore.GREEN}[+]{Fore.RESET} Have a symbol e.g (!,@,#,$, etc..).'''
    if all(list_test):
        print(f'{Fore.LIGHTGREEN_EX}{Style.BRIGHT}[+] Your password {password} Strong!{Fore.RESET}')
    else:
        print(weak_msg)
def generate_pass():
    while True:
        try:
         len_psw = int(input(f'{Fore.WHITE}[-] Enter The Length of the password{Fore.YELLOW} At least 8 :{Fore.RESET}'))
         if len_psw >=8:
             break
         print(f'{Fore.RED}[!]{Fore.RESET} Your choice is too short, Try again')
        except ValueError:
             print(f'{Fore.RED}[×]{Fore.RESET} Invalid input, Please Enter a number!')
    while True:
        char = string.digits + string.ascii_letters
        ask_sym = input(f'{Fore.WHITE}[-]{Fore.RESET} Do you want to add symbols ?{Fore.YELLOW}YES/NO : {Fore.RESET}').lower().strip()
        if ask_sym in('yes', 'no'):
            break
        else:
            print(f'{Fore.RED}[×]{Fore.RESET} Please Enter{Fore.YELLOW}YES/NO:{Fore.RESET}!')
    if ask_sym == 'yes':
       password = ''.join(secrets.choice(char+string.punctuation) for _  in range(len_psw))
    else:
       password = ''.join(secrets.choice(char) for _ in range(len_psw))
    return password

def ist_open(path):
    print(f'{Fore.WHITE}[-]{Fore.RESET} Checking the file name...')
    time.sleep(3)
    print(f'{Fore.GREEN}[+]{Fore.RESET} DONE!')
    time.sleep(2)
    try:
      with pikepdf.open(path):
              print(f'{Fore.GREEN}[=]{Fore.RESET} The file is open.')
              exit()
    except pikepdf.PasswordError:
        print(f'{Fore.WHITE}[-]{Fore.RESET} Checking if the file locked..')
        time.sleep(3)
        print(f'{Fore.LIGHTRED_EX}[=]{Fore.RESET} File LOCKED!')
        time.sleep(2)
        print(f'{Fore.WHITE}[-]{Fore.RESET} Preparing the attack..')
        time.sleep(5)
    except FileNotFoundError:
        print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Invalid!')
        exit()

def try_pdf(path, password):
    try:
        with pikepdf.open(path, password=password):
            return True
    except pikepdf.PasswordError:
        return False
def brute_force(path):
    attempts=0
    start = time.time()
    print(f'{Fore.LIGHTRED_EX}[=]{Fore.RESET} STARTING BRUTE-FORCE ATTACK ...')
    time.sleep(4)
    found = False
    for i in range(9999999999):
        pass_guess = f'{i:03}'
        print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Trying ---->> {pass_guess}')
        attempts +=1
        if try_pdf(path, pass_guess):
            end = time.time()
            total = end - start
            print(f'{Fore.LIGHTGREEN_EX}[+] Found The Password! --> {pass_guess}{Fore.RESET}')
            print(f'{Fore.GREEN}[+]{Fore.RESET}{Fore.YELLOW} The attempts --> {attempts} attempts{Fore.RESET}.')
            print(f'{Fore.GREEN}[+]{Fore.RESET}{Fore.BLUE} The full time of attack is --> {total:.2f}{Fore.RESET}')
            found = True
            break
    if not found:
        print(f'{Style.BRIGHT}{Fore.RED}{Fore.RED}[!]{Fore.RESET} NOT FOUND!')

ToolTitle= pyfiglet.figlet_format("PassTool", font="puffy")
colored_tool_title = Fore.RED + ToolTitle+ Fore.RESET
print(colored_tool_title)
while True:
    menu=f'''
[1] Testing Your Password.
[2] Generate a strong Password.
[3] PDF attack {Fore.LIGHTBLACK_EX}FOR EDUCATIONAL!.{Fore.RESET}
[4] Tips for protection.
[5] Quit.
'''
    print(menu)
    user_input = input(f'{Fore.WHITE}[-]{Fore.RESET} Select a number : ')
    if user_input =='1':
        while True:
         user_password = input(f'{Fore.WHITE}[-]{Fore.RESET} Enter Your password To test : ')
         testing_pass(user_password)
         out_test = input(f'{Fore.WHITE}[-]{Fore.RESET} Do you want to test again? YES/NO : ').lower()
         if out_test =='no':
               break

    elif user_input =='2':
        while True:
            print(f'{Fore.GREEN}[+]{Fore.RESET}{Fore.LIGHTMAGENTA_EX} Your Password is -->{Fore.RESET}(( {generate_pass()} )){Fore.LIGHTMAGENTA_EX} Keep it safe !{Fore.RESET}')
            out_generate = input(f'{Fore.WHITE}[-]{Fore.RESET} Do you want to Generate again? YES/NO : ').lower()
            if out_generate == 'no':
                break
            else:
                print(f'{Fore.RED}[!]{Fore.RESET} Please select YES/NO')
    elif user_input =='3':
        while True:
         user_path= input(f'{Fore.WHITE}[-]{Fore.RESET} Enter The file Location : {Fore.RESET}')
         if ist_open(user_path):
             break

         brute_force(user_path)
         out_attack = input(f'{Fore.WHITE}[-]{Fore.RESET} Do you want to Attack again? YES/NO : ').lower()
         if out_attack =='no':
            print(f'{Fore.RED}[!]{Fore.RESET} Please select YES/NO')
    elif user_input =='4':
        print(f'{Fore.MAGENTA}{Style.BRIGHT}About This Tool:{Fore.RESET}')
        print(f'{Fore.LIGHTGREEN_EX}This tool is developed to test password strength and secure PDF files.\nIts goal is to educate users on digital security by simulating brute-force attacks\n{Fore.RESET}')
        print(f'{Fore.MAGENTA}{Style.BRIGHT}Using the Tool Safely:{Fore.RESET}')
        print(f'{Fore.LIGHTGREEN_EX}Always ensure you are using the tool in a test environment or on PDF files you have permission to access.\nDo not use the tool on files or accounts you are not authorized to test.\n{Fore.LIGHTRED_EX}Using the tool illegally could result in legal consequences.\n{Fore.RESET}')
        print(f'{Fore.MAGENTA}{Style.BRIGHT}Testing Password Strength:{Fore.RESET}')
        print(f'{Fore.LIGHTGREEN_EX}Use the tool to test the strength of your passwords.\nEnsure your password contains a mix of uppercase and lowercase letters, numbers, and symbols.\nTesting your passwords helps you improve account security and avoid using weak, easily guessable passwords.\n{Fore.RESET}')
        print(f'{Fore.MAGENTA}{Style.BRIGHT}Securing PDF Files:{Fore.RESET}')
        print(f'{Fore.LIGHTGREEN_EX}The tool can also test the security of PDF files by checking the strength of passwords used to protect them.\nThis helps ensure your files are safe from unauthorized access.\nPDF files often contain sensitive information.\nUsing strong passwords to secure them is crucial for maintaining their security.\n{Fore.RESET}')
        print(f'{Fore.MAGENTA}{Style.BRIGHT}Tool for Educational Purposes Only{Fore.RESET}')
        print(f'{Fore.LIGHTGREEN_EX}Remember, the purpose of this tool is educational.\nUse it to learn how to protect your files and accounts from potential attacks, and do not use it to breach accounts or systems you do not have permission to test.\nUsing the tool for illegal purposes can result in legal consequences.\n{Fore.LIGHTRED_EX}Again Its important to use it for educational purposes only.{Fore.RESET}')
        print(f'{Fore.YELLOW}By:Sulaiman Sahhari{Fore.RESET}')
        print(f'{Fore.YELLOW}sulaiman.mohammed.career@gmail.com{Fore.RESET}')
    elif user_input =='5':
        print(f'{Fore.MAGENTA}Thank You for using PassTool!, Bye.{Fore.RESET}')
        break