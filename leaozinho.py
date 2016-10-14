"""
Aplicativo de detecção de designações para professores de ensino básico.
"""

#Rows - para a exploração de tabelas.
import rows
from io import BytesIO

#Whats app caller
import subprocess

#Splinter - Para o acesso à página das designações
from splinter import Browser

browser = Browser('phantomjs')
browser.visit('http://controlequadropessoal.educacao.mg.gov.br/divulgacao')

browser.click_link_by_id('__abrir-filtro')

browser.select('data[Filtro][Vaga][regional_id]', '42')

browser.select('data[Filtro][Escola][municipio_id]', '1860')

browser.select('data[Filtro][Vaga][carreira_id]', '7')

browser.find_by_name('Filtrar').click()

html = bytes(str(browser.html).encode('utf-8'))

csv = rows.import_from_html(BytesIO(html))
"""
Campos a serem procurados:
regional | municipio | escola | cargo | categoria_profissional | conteudo | situacao | edital 
"""


for row in csv:
	if row.conteudo == "QUIMICA":
		subprocess.call(['yowsup-cli', 'demos', '-l', '553173610349:CVTx7Mg307vu42MR7UJVGp7jPu0=', '-s', '553199571127', 'Tem designação florzinha!'])