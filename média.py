#algoritimo de calculo de média
nome_aluno=input('digite o nome do aluno ')
av1 = float(input('digite nota da avaliação 1 '))
av2 = float(input('digite nota da avaliação 2 '))
av3 = float(input('digite nota da avaliação 3 '))
av4 = float(input('digite nota da avaliação 4 '))

media = (av1 + av2 + av3 + av4)/4

if media >= 7:
    print('A média de {} é {:.2f}, aprovado'.format(nome_aluno, media))

else:
    n_rec=float(input('por favor digite a nota de recuperação de {}:'.format(nome_aluno)))
    n_media= (n_rec + media)/2
    if n_media >= 6:
        print('a média de {} é {:.2f}, e está aprovado!'.format(nome_aluno, n_media))

    elif n_media < 6:
        print('a média de {} é {:.2f}, e está reprovado!'.format(nome_aluno, n_media))


print('Fim')














