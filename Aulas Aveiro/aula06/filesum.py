from tkinter import filedialog

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    name = input("File? ")
                                    
    name = filedialog.askopenfilename(title="Choose File") 
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)

total = 0

def fileSum(filename):
	with open (name,"r") as numbers:
		for line in name:
			total += float(line)
			print(total)


if __name__ == "__main__":
    main()

