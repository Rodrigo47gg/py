vlc = float(input('qual a velocidade do seu veiculo: ')) 
if vlc >=80:
    print('você foi multado em R$:{:.2f}'.format((vlc - 80) * 7))
else:
    print('no limite de velocidade, siga em frente')