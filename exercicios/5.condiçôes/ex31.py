kms = float(input('quantos kms de viagem: '))
if kms >= 200:
   print('sua viagem e de {}kms, vai custar {:.2f}'.format(kms, kms * 0.45))
else:
   print("sua viagem e de {}kms, vai custar {:.2f}".format(kms, kms * 0.50))