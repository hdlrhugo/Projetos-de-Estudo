# LISTA 2
# 15/09/2021


print("PARA COMEÇAR A LISTA :")
opcao = int(input("ESCOLHA :\n1= INICIAR \n2= PRA SAIR"))
print(' ')
while opcao == 1:

    quest = int(input("QUAL A QUESTAO VC QUER ACESSAR 1 A 5 : "))
    print(' ')

    while (quest >= 1 & quest <=5):

        if quest == 1:
            # 1.Se listarmos todos os números naturais menores que  10  que são múltiplos de  3  ou  5 ,
            # obteremos  3 ,  5 ,  6  e  9 . A soma desses múltiplos é  23 .
            # Encontre a soma de todos os múltiplos de  3  ou  5  abaixo de  1000 .
            soma = 0
            for x in range(0, 1000):
                if x % 3 == 0 or x % 5 == 0:
                    soma = x + soma
            print(soma)
            print(' ')
            break

        elif quest == 2:
            #2.Usando uma estrutura de repetição,
            # crie um programa que imprima os valores dos n primeiros termos de uma sequência Fibonacci.
            # Lembre-se que os números que compõem essa sequência são:  1,1,2,3,5,8,13,21,34...
            n=int(input("INFORMAR A QUANTIDADE DE TERMOS: "))
            n1=0
            n2=1
            print("%d -- %d"%(n1,n2),end='')
            cont=3
            while cont<=n:
                n3=n1+n2
                print(" -- %d "%(n3),end='')
                n1=n2
                n2=n3
                cont +=1
            print("-- :")
            print(' ')



            break
        elif quest == 3:
            a=2
            n=10
            x=4
            for i in range(n):
                x=0.5*(x+a/x)
                print(f"NOSSO:{x}")
                import math
                print(f"math: {math.sqrt(2)}")




            break
        elif quest == 4:
            num=int(input("DIGITE UM NUMERO INTEIRO: "))
            cont=3
            while num<=cont:
                total=num
                cont-=1
                if num %2==0:
                    total=(num/2)
                    print("- %d  "%(total),end='')


                elif num %2 ==1:

                    total=(num*3)+1
                    print(" %d--" % (total))
                    print(" %d--" % (total))

            print(total)
            break
        elif quest == 5:
            import math
            s=0
            for n in range(1,10**6+1):
                s+= 1/ math.pow(n,2)
            resultado=math.sqrt(6*s)
            print(resultado)

            break

    opcao = int(input(" \n ESCOLHA  :\n1= CONTINUAR \n2= PRA SAIR"))
print(' ')
print("FIM PROGRAMA ")