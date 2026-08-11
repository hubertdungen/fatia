<p align="center">
  <img src="fatia-logo.svg" width="110" alt="Fatia">
</p>

<h1 align="center">Fatia</h1>

<p align="center">
  Calculadora de preços para impressão 3D — a partir da estimativa do teu slicer.<br>
  <a href="README.md">English</a> · <b>Português</b>
</p>

---

Metes o que o slicer te dá — gramas, tempo, custo — e o Fatia devolve o preço, o lucro real e um orçamento pronto a enviar ao cliente. Como app local é um único ficheiro HTML, sem servidor e sem conta — e instalável como aplicação com um clique. Para uso permanente, o servidor Python incluído acrescenta login e memória partilhada por utilizador.

**[▶ Abrir o Fatia](https://hubertdungen.github.io/fatia/)**

## Porquê

A maior parte das calculadoras de impressão 3D só soma filamento e eletricidade. Isso não é o teu custo — é uma fração dele. Fica de fora a amortização da máquina, o tempo de preparação de cada mesa, o desperdício, a embalagem, e sobretudo o tempo de impressora, que é onde os trabalhos longos silenciosamente deixam de dar lucro.

O Fatia calcula as duas coisas em paralelo: **o que te custa** e **o que cobras**. A diferença entre elas é o teu lucro, e está sempre visível.

## O que faz

**Base pelo slicer.** Cada mesa tem peso, tempo e custo em euros. Se preencheres o custo, ele manda e o cálculo por peso é ignorado. Um fator corrige a estimativa, porque o slicer só conta o preço da bobine — não os portes do fornecedor nem o desperdício.

**Retificação pós-impressão.** Depois de imprimires, metes os valores reais. Ele mostra o desvio e, se for grande, oferece guardá-lo como desvio típico das próximas estimativas. É isto que impede a calculadora de envelhecer.

**A mesa como unidade de trabalho.** Base fixa e minutos de preparação por mesa — fatiar, preparar a base, arrancar peças. Não dependem de quantas peças lá cabem, e é por isso que encher a mesa compensa. O indicador de densidade quantifica exatamente quanto.

**Posicionamento de mercado.** Três réguas: taxa horária de máquina, preço por peça e preço por mesa. Os valores de referência foram recolhidos em agosto de 2026 e envelhecem sozinhos aplicando a inflação prevista pelo Banco de Portugal. Podes ainda colar orçamentos de concorrentes para o mesmo trabalho, e registar o histórico do que os teus clientes aceitaram ou recusaram.

**Portes reais.** 16 serviços com preços atuais: CTT Correio Registado, Encomenda Postal T1/T2 com e sem entrega ao domicílio, aéreo para Madeira e Açores, InPost Locker nacional e InPost para oito países europeus. O peso da embalagem entra no escalão, que é o que a transportadora pesa.

**Base de impressoras.** 17 modelos com preço, consumo médio e vida útil. Podes marcar favoritas, adicionar as tuas e editar tudo.

**Várias impressoras no mesmo trabalho.** Cada mesa escolhe a sua máquina. O custo horário é o dessa máquina e o total sai da média ponderada pelo tempo de cada mesa. Se retificares o tempo real, todas as mesas escalam na mesma proporção — regra de três simples. O painel mostra o €/h de cada máquina e a média resultante.

**Orçamento do cliente.** Vista limpa e imprimível, com logo mini do Fatia, ficha técnica e sem uma única margem à vista. Opcionalmente:

- **as impressoras usadas** — interruptor geral, e um visto por mesa para escolher quais aparecem;
- **a tua marca** — logótipo, nome de quem fatura, NIF, contactos, morada, slogan em itálico e uma mensagem destacada ao cliente;
- **imposto de faturação** — presets para Portugal IVA 23%, 13% e 6%, Espanha IVA 21%, França TVA 20%, Alemanha MwSt. 19%, Itália IVA 22%, Países Baixos btw 21%, Reino Unido VAT 20%, ou uma taxa personalizada/geral. O total do cliente mantém-se igual e o orçamento separa subtotal antes de imposto e imposto incluído;
- **QR codes** — desligados por omissão. O QR é gerado do endereço que escreveres, sem rede nem serviços externos, e qualquer um pode ser substituído por uma imagem tua (PNG/JPEG).

**Presets e memória.** Guarda configurações com nome, exporta e importa em JSON. Tudo entra no template: impressoras por mesa, logótipo, textos e QR codes. Ele lembra-se de onde ficaste.

**Modo simples.** Esconde tudo o que não estás a usar. Clica nos títulos dos painéis para os dobrar.

## Como usar

Abre o `index.html` no browser. É tudo.

**Instalar como aplicação.** Servido por `http(s)` — no GitHub Pages ou num servidor local — o Fatia é uma PWA: aparece um botão **⤓ Instalar app**, ou usas o menu do browser (Chrome/Edge: ⋮ → *Instalar Fatia*; telemóvel: partilhar → *Adicionar ao ecrã principal*). Passa a abrir em janela própria, com ícone, e funciona sem rede.

Duas coisas só funcionam quando a página é servida por `http(s)` — a atualização automática do preço de mercado da eletricidade e a verificação de atualizações dos dados. Aberto do disco com `file://`, o browser bloqueia qualquer pedido para fora, e não há volta a dar. Usa o GitHub Pages, ou um servidor local:

```bash
python3 -m http.server 8000     # depois abre http://localhost:8000
```

Para uso permanente com memória partilhada, corre antes o servidor incluído:

```bash
python3 server.py --host 0.0.0.0 --port 8098
```

Continua a servir a mesma PWA, mas acrescenta `/api/*` para login e memória por utilizador em SQLite. Por defeito, o primeiro utilizador só pode ser criado pela LAN/Meshnet; usa `FATIA_ALLOW_SIGNUP=1` apenas se quiseres permitir auto-registo.

## Fontes dos dados de referência

| O quê | Fonte | Data |
| --- | --- | --- |
| Taxas horárias de máquina e mão de obra | [LayerMath](https://layermath.com/blog/3d-printing-hourly-rate) | jun 2026 |
| Preço por peça em Portugal | [Zaask](https://www.zaask.pt/quanto-custa/impressao-3d) | 2026 |
| Previsão de inflação | [Banco de Portugal](https://www.bportugal.pt/comunicado/comunicado-do-banco-de-portugal-sobre-o-boletim-economico-de-junho-de-2026) | jun 2026 |
| Portes CTT | [CTT](https://www.ctt.pt/particulares/enviar/para-portugal/encomenda-postal) | ago 2026 |
| Portes InPost | [InPost](https://www.inpost.pt/faz-um-envio/nossas-tarifas-de-envio) | ago 2026 |
| Preço de mercado da eletricidade | [energy-charts.info](https://api.energy-charts.info/) (OMIE / zona PT) | ao vivo |
| Presets de IVA / imposto | [Your Europe](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm) e [GOV.UK](https://www.gov.uk/vat-rates) | jul 2026 |

Estes valores são **estimativas informativas**, não cotações. Confirma-os antes de os usares num orçamento real.

## Licença

**Uso pessoal — livre e gratuito.** Usa, copia e modifica à vontade para projetos pessoais, aprendizagem e trabalhos sem fins comerciais.

**Uso comercial — sob consulta prévia.** Se usares o Fatia para orçamentar trabalho que vendes:

| Faturação mensal | Mensalidade |
| --- | --- |
| Até 10 000 € | 10 €/mês |
| Acima de 10 000 € | 100 €/mês |

Contacta **hubertkenobi@gmail.com** antes de começares. Termos completos em [`LICENCA.md`](LICENCA.md) (PT) e [`LICENSE`](LICENSE) (EN, versão que prevalece).

---

<p align="center">
  <i>Fatia — powered by <b>DL X</b></i><br>
  <sub><i>DL X é a divisão de investigação e produto da <b>DungenLabs</b>, laboratório de engenharia em Lisboa —
  a metade do laboratório que constrói para si própria: protótipos experimentais, produtos próprios
  fabricados em casa (extrusão FDM, filamento reforçado com fibra e fundição em resina), parcerias e
  tecnologia à procura de uso.</i></sub><br>
  <sub><a href="https://dlx.dungenlabs.com">dlx.dungenlabs.com</a> · <a href="https://dungenlabs.com">dungenlabs.com</a></sub>
</p>
