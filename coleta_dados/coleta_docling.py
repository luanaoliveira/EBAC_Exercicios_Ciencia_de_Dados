import json

from docling.document_converter import DocumentConverter

source = 'cotacao_de_precos_ama.pdf'
converter = DocumentConverter()
result = converter.convert(source)

# Converte para markdown
json_markdown = result.document.export_to_markdown()
print(result.document.export_to_markdown())

# Converte para JSON
json_output = result.document.export_to_dict()
print(json.dumps(json_output, ensure_ascii=False, indent=4))

# Salvar o JSON em um arquivo
with open("cotacao_de_precos_convertido_sem_formatacao.json", "w", encoding="utf-8") as json_file:
    json.dump(json_output, json_file, ensure_ascii=False, indent=4)