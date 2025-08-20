import random
import string
import os
import platform
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

# Limpa o terminal
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

def print_panel(text, width=70):
    border = "=" * width
    print(Fore.RED + border)
    text_centered = text.center(width)
    print(Fore.WHITE + text_centered)
    print(Fore.RED + border + Style.RESET_ALL)

print_panel("Feito por Ghost The God")

try:
    total_lines = int(input(Fore.RED + "Digite o número de senhas a gerar: "))
    min_len = int(input(Fore.RED + "Digite o tamanho mínimo de cada senha: "))
    max_len = int(input(Fore.RED + "Digite o tamanho máximo de cada senha: "))
    file_name = input(Fore.RED + "Digite o nome do arquivo de saída (ex: wordlist.txt): ")
except ValueError:
    print(Fore.RED + "Entrada inválida. Use apenas números para quantidade e tamanho.")
    exit()

chars = string.ascii_letters + string.digits + "!@#$%&*"

with open(file_name, "w") as f:
    for _ in range(total_lines):
        length = random.randint(min_len, max_len)
        combo = ''.join(random.choices(chars, k=length))
        f.write(combo + "\n")

print(Fore.RED + f"\nWordlist gerada: {file_name} com {total_lines} linhas")
print(Fore.RED + "Feito por Ghost The God")

try:
    if platform.system() == "Windows":
        os.startfile(file_name)
    elif platform.system() == "Darwin":
        subprocess.call(["open", file_name])
    else:
        subprocess.call(["xdg-open", file_name])
except Exception as e:
    print(Fore.RED + f"Não foi possível abrir o arquivo automaticamente: {e}")
