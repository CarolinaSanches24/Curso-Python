import colorama;

colorama.init();


# colorindo texto 
print(colorama.Fore.RED + "vermelho.") 
print(colorama.Fore.GREEN + "verde.")
print(colorama.Fore.YELLOW + "amarelo.")

# cor vazado
print(colorama.Fore.BLUE + "Harry Potter e a Pedra Filosofal (2001)");
print("Título original: Harry Potter and the Philosophers Stone  (no Reino Unido)") 

# Style.RESET_ALL não deixa vazar a cor pra outra linha
print(colorama.Fore.BLUE + "Harry Potter e a Pedra Filosofal (2001)");
print(colorama.Style.RESET_ALL+"Título original: Harry Potter and the Philosophers Stone  (no Reino Unido)") 