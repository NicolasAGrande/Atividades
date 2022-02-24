import PyPDF2
from PIL import Image 

#digitar o caminho até os documentos(em formato de imagem)
assi = input('Digite o caminho até o documento: 'r'')
img = input('Digite o caminho até a assinatura: ' r'')

img1 = Image.open(assi) 
img2 = Image.open(img) 
x = int(input('Digite o valor do eixo x: '))
y = int(input('Digite o valor do eixo y: '))
img1.paste(img2, (x,y), mask = img2) 

#Conversão do arquivo para pdf 
im1 = img1.convert('RGB')
im1.save(r'Doc_assinado.pdf')
