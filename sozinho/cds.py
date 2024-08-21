import barcode
from barcode.writer import ImageWriter

def gerar_codigo_barras(dados_produto, arquivo_saida):
    # Cria um objeto de código de barras
    codigo_barras = barcode.get('ean13', dados_produto, writer=ImageWriter())
    codigo_barras.save(arquivo_saida)

# Exemplo de uso
dados_produto = '123456789012'  # Código EAN-13 válido
gerar_codigo_barras(dados_produto, 'produto_barras')
