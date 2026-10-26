# HEERA — Luxury Minimal v2 (prévia)

## Objetivo e público
Showroom digital de beleza profissional para nail designers, manicures e salões. Priorizar a percepção de curadoria e a navegação de produtos, sem preços e sem checkout. Os pedidos são enviados ao WhatsApp.

## Referências
- Skill Momentto Design: `skills://plugins/momentto-design/design-directions`.
- Snapshot das referências Apple e Shopify (DESIGN.md da biblioteca Momentto). Apple contribui fotografia como protagonista e baixa densidade; Shopify contribui narrativa comercial e contraste entre superfícies. Esta adaptação não reproduz identidade visual dessas empresas.

## Identidade e atmosfera
Editorial, sofisticada, artesanal, técnica. Preservar o chocolate e os neutros rosados da HEERA, evitando padrões genéricos de marketplace. O monograma HE na hero é uma exploração visual, ainda sujeito à aprovação da marca.

## Cores
- Chocolate principal: `#4A2D20` — CTAs, textos fortes e faixa editorial.
- Nude metálico: `#A88370` — detalhes e contornos.
- Rosé claro: `#EAD9CF` — painéis e superfícies.
- Creme: `#FAF6F1` — base principal.
- Texto secundário: `#806C5E`.

## Tipografia
- Headlines: Georgia/serif, regular, de 37 a 79 px, entrelinha próxima a 1.1.
- UI: system-ui/Segoe UI, 12 a 16 px; mínimos de legibilidade no mobile. Não incluir fontes pagas.

## Layout
- Área máxima ~1320 px.
- Hero dividido em narrativa e composição de três fotografias reais de produtos, com monograma HE decorativo.
- Quatro universos de marcas em blocos visuais com filtro único sincronizado com o seletor.
- Catálogo em 4 colunas desktop, 3 em tablet, 2 no mobile; manter busca, ordenação, categorias, detalhes e sacola.

## Componentes e estados
- CTA preenchido chocolate, outline neutro, estados hover/active/focus visíveis.
- Card discreto, foto em fundo rosado, nome serifado, informação secundária e ações distintas.
- Filtros ativos demonstrados visualmente e aria-pressed, sem duplicar lógica.
- Sacola lateral com alteração de quantidades e pedido sem preços.

## Mobile e acessibilidade
- Até 680px hero empilhado, coleção em duas colunas, produtos em duas colunas.
- Interações por toque, foco de teclado, rótulos de busca e selects, reduced-motion.
- Pendência: executar testes reais de Safari iOS e contraste antes de aprovação definitiva.

## Fazer / evitar
- Fotografias autênticas verificadas, nunca substituir por imagens inventadas.
- Não adicionar preços nem checkout.
- Não alegar que todas as 71 imagens estão disponíveis (nove recuperadas; 62 faltando).
- Não atualizar `index.html` sem aprovação explícita.
- Não considerar o fundo do logo resolvido somente por `mix-blend-mode`: providenciar exportação original PNG/WebP com canal alpha ou SVG da identidade.

## Aceite
1. Preview independente carrega e preserva 71 produtos.
2. Busca, filtros de marca/categoria, detalhes, ordenação e sacola funcionam em desktop/Android/iOS.
3. Mensagem WhatsApp contém apenas descrição e quantidade.
4. Todas as fotos existentes permanecem visíveis.
5. Logo transparente verdadeiro e monograma aprovados antes da promoção a produção.
