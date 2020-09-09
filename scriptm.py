#!/usr/bin/python
# Este script contém as predefinições para serem subtituídas em artigos, discussões e etc..
# Para inciar o bot, eu usarei o "python pwb.py replace -fix:checksubst -catr:!Páginas com predefinições que deveriam ser substituídas -always"
# -*- coding: utf-8  -*-
"""
@ Autor: [[Usuário:Juan90264]]
@ Licença: GNU General Public License 2.0 (GPLv2)
"""

if 'fixes' not in globals(): fixes = {}

fixes['checksubst'] = {
    'regex': True,
    'msg': {
        '_default': 'Bot: adicionando [[WP:SUBST|SUBST]] numa predefinição',
    },
    'replacements': [
    (r'\{\{[Aa]eronave futra', r'{{SUBST:Aeronave futra'),
    (r'\{\{Wikipedia:Projetos/[Aa]eroportos do Brasil/Convite', r'{{SUBST:Wikipedia:Projetos/[Aa]eroportos do Brasil/Convite'),
    (r'\{\{[Áá]lbuns/Convite', r'{{SUBST:[Áá]lbuns/Convite'),
    (r'\{\{[Aa]lerta', r'{{SUBST:Alerta'),
    (r'\{\{[Aa]lerta de sock', r'{{SUBST:Alerta de sock'),
    (r'\{\{[Aa]mbiente/Convite', r'{{SUBST:Ambiente/Convite'),
    (r'\{\{[Aa]mei', r'{{SUBST:Amei'),
    (r'\{\{[Aa]mor', r'{{SUBST:Amor'),
    (r'\{\{[Aa]nfíbios e répteis/Convite', r'{{SUBST:Anfíbios e répteis/Convite'),
    (r'\{\{[Aa]nimangá/Convite', r'{{SUBST:Animangá/Convite'),
    (r'\{\{[Aa]njo', r'{{SUBST:Anjo'),
    (r'\{\{[Aa]pagar', r'{{SUBST:Apagar'),
    (r'\{\{[Aa]plauso', r'{{SUBST:Aplauso'),
    (r'\{\{[Aa]provada', r'{{SUBST:Aprovada'),
    (r'\{\{[Aa]provado', r'{{SUBST:Aprovado'),
    (r'\{\{[Aa]provo', r'{{SUBST:Aprovo'),
    (r'\{\{[Aa]rqueologia/Convite', r'{{SUBST:Arqueologia/Convite'),
    (r'\{\{[Aa]rte/Convite', r'{{SUBST:Arte/Convite'),
    (r'\{\{[Áá]sia/Convite', r'{{SUBST:[Áá]sia/Convite'),
    (r'\{\{[Aa]ssobiar', r'{{SUBST:Assobiar'),
    (r'\{\{[Aa]tlético Mineiro/Convite', r'{{SUBST:Atlético Mineiro/Convite'),
    (r'\{\{[Aa]v-Bpv', r'{{SUBST:Av-Bpv'),
    (r'\{\{[Aa]v-censra', r'{{SUBST:Av-censra'),
    (r'\{\{[Aa]v-fonte', r'{{SUBST:Av-fonte'),
    (r'\{\{[Aa]v-layout', r'{{SUBST:Av-layout'),
    (r'\{\{[Aa]v-namespace', r'{{SUBST:Av-namespace'),
    (r'\{\{[Aa]v-npi', r'{{SUBST:Av-npi'),
    (r'\{\{[Aa]v-npov', r'{{SUBST:Av-npov'),
    (r'\{\{[Aa]v-página de usuário', r'{{SUBST:Av-página de usuário'),
    (r'\{\{[Aa]v-página pessoal', r'{{SUBST:Av-página pessoal'),
    (r'\{\{[Aa]v-pub', r'{{SUBST:Av-pub'),
    (r'\{\{[Aa]v-redirect', r'{{SUBST:Av-redirect'),
    (r'\{\{[Aa]v-Remoção', r'{{SUBST:Av-Remoção'),
    (r'\{\{[Aa]v-Spam', r'{{SUBST:Av-Spam'),
    (r'\{\{[Aa]v-teste', r'{{SUBST:Av-teste'),
    (r'\{\{[Aa]vaí/Convite', r'{{SUBST:Avaí/Convite'),
    (r'\{\{[Aa]vermelhar', r'{{SUBST:Avermelhar'),
    (r'\{\{[Aa]viação/Boas-vindas', r'{{SUBST:Aviação/Boas-vindas'),
    (r'\{\{[Aa]viação/Convite', r'{{SUBST:Aviação/Convite'),
    (r'\{\{[Aa]viação/Volte ao projecto', r'{{SUBST:Aviação/Volte ao projecto'),
    (r'\{\{[Aa]viso', r'{{SUBST:Aviso'),
    (r'\{\{[Aa]viso-animal', r'{{SUBST:Aviso-animal'),
    (r'\{\{[Aa]viso-assinatra', r'{{SUBST:Aviso-assinatra'),
    (r'\{\{[Aa]viso-assinatra não permitida', r'{{SUBST:Aviso-assinatra não permitida'),
    (r'\{\{[Aa]viso-assinatra-ER', r'{{SUBST:Aviso-assinatra-ER'),
    (r'\{\{[Aa]viso-assine', r'{{SUBST:Aviso-assine'),
    (r'\{\{[Aa]viso-bloqueado-conta imprópria', r'{{SUBST:Aviso-bloqueado-conta imprópria'),
    (r'\{\{[Aa]viso-bpv1', r'{{SUBST:Aviso-bpv1'),
    (r'\{\{[Aa]viso-bpv2', r'{{SUBST:Aviso-bpv2'),
    (r'\{\{[Aa]viso-bpv3', r'{{SUBST:Aviso-bpv3'),
    (r'\{\{[Aa]viso-bpv4', r'{{SUBST:Aviso-bpv4'),
    (r'\{\{[Aa]viso-categoria', r'{{SUBST:Aviso-categoria'),
    (r'\{\{[Aa]viso-cite fonte', r'{{SUBST:Aviso-cite fonte'),
    (r'\{\{[Aa]viso-comentários', r'{{SUBST:Aviso-comentários'),
    (r'\{\{[Aa]viso-conflito de interesses', r'{{SUBST:Aviso-conflito de interesses'),
    (r'\{\{[Aa]viso-cópia', r'{{SUBST:Aviso-cópia'),
    (r'\{\{[Aa]viso-criação', r'{{SUBST:Aviso-criação'),
    (r'\{\{[Aa]viso-ER', r'{{SUBST:Aviso-ER'),
    (r'\{\{[Aa]viso-facebook', r'{{SUBST:Aviso-facebook'),
    (r'\{\{[Aa]viso-GE', r'{{SUBST:Aviso-GE'),
    (r'\{\{[Aa]viso-genérico', r'{{SUBST:Aviso-genérico'),
    (r'\{\{[Aa]viso-imagem externa', r'{{SUBST:Aviso-imagem externa'),
    (r'\{\{[Aa]viso-interwiki', r'{{SUBST:Aviso-interwiki'),
    (r'\{\{[Aa]viso-justificar', r'{{SUBST:Aviso-justificar'),
    (r'\{\{[Aa]viso-LD-movido', r'{{SUBST:Aviso-LD-movido'),
    (r'\{\{[Aa]viso-LD-removido', r'{{SUBST:Aviso-LD-removido'),
    (r'\{\{[Aa]viso-ligações internas', r'{{SUBST:Aviso-ligações internas'),
    (r'\{\{[Aa]viso-linguagem incorreta', r'{{SUBST:Aviso-linguagem incorreta'),
    (r'\{\{[Aa]viso-med', r'{{SUBST:Aviso-med'),
    (r'\{\{[Aa]viso-moção', r'{{SUBST:Aviso-moção'),
    (r'\{\{[Aa]viso-não remova', r'{{SUBST:Aviso-não remova'),
    (r'\{\{[Aa]viso-ortografia', r'{{SUBST:Aviso-ortografia'),
    (r'\{\{[Aa]viso-PE-novato', r'{{SUBST:Aviso-PE-novato'),
    (r'\{\{[Aa]viso-propaganda', r'{{SUBST:Aviso-propaganda'),
    (r'\{\{[Aa]viso-revertida', r'{{SUBST:Aviso-revertida'),
    (r'\{\{[Aa]viso-suspeito', r'{{SUBST:Aviso-suspeito'),
    (r'\{\{[Aa]viso-tag', r'{{SUBST:Aviso-tag'),
    (r'\{\{[Aa]viso-vandalismo', r'{{SUBST:Aviso-vandalismo'),
    (r'\{\{[Aa]viso-voto', r'{{SUBST:Aviso-voto'),
    (r'\{\{[Aa]viso2', r'{{SUBST:Aviso2'),
    (r'\{\{[Aa]viso3', r'{{SUBST:Aviso3'),
    (r'\{\{[Bb]anda Desenhada/Convite', r'{{SUBST:Banda Desenhada/Convite'),
    (r'\{\{[Bb]andas/Convite', r'{{SUBST:Bandas/Convite'),
    (r'\{\{[Bb]asquetebol/Convite', r'{{SUBST:Basquetebol/Convite'),
    (r'\{\{[Bb]D', r'{{SUBST:BD'),
    (r'\{\{[Bb]D/Boas-vindas', r'{{SUBST:BD/Boas-vindas'),
    (r'\{\{[Bb]eijo', r'{{SUBST:Beijo'),
    (r'\{\{[Bb]em-vindo(a)', r'{{SUBST:Bem-vindo(a)'),
    (r'\{\{[Bb]ibliografia', r'{{SUBST:Bibliografia'),
    (r'\{\{[Bb]iografias/Convite', r'{{SUBST:Biografias/Convite'),
    (r'\{\{[Bb]ioquímica/Convite', r'{{SUBST:Bioquímica/Convite'),
    (r'\{\{[Bb]loqueado', r'{{SUBST:Bloqueado'),
    (r'\{\{[Bb]loqueado parcial', r'{{SUBST:Bloqueado parcial'),
    (r'\{\{[Bb]loqueado-CPV', r'{{SUBST:Bloqueado-CPV'),
    (r'\{\{[Bb]loqueado-disc', r'{{SUBST:Bloqueado-disc'),
    (r'\{\{[Bb]lues/Convite', r'{{SUBST:Blues/Convite'),
    (r'\{\{[Bb]oas', r'{{SUBST:Boas'),
    (r'\{\{[Bb]ola de cristal', r'{{SUBST:Bola de cristal'),
    (r'\{\{[Bb]om dia', r'{{SUBST:Bom dia'),
    (r'\{\{[Bb]ossa Nova/Convite', r'{{SUBST:Bossa Nova/Convite'),
    (r'\{\{[Bb]otão de edição/aviso1', r'{{SUBST:Botão de edição/aviso1'),
    (r'\{\{[Bb]otão de edição/bv', r'{{SUBST:Botão de edição/bv'),
    (r'\{\{[Bb]otão de edição/bv-ip', r'{{SUBST:Botão de edição/bv-ip'),
    (r'\{\{[Bb]otão de edição/bv-av', r'{{SUBST:Botão de edição/bv-av'),
    (r'\{\{[Bb]otão de edição/CaixaSucessao', r'{{SUBST:Botão de edição/CaixaSucessao'),
    (r'\{\{[Bb]otão de edição/categoria', r'{{SUBST:Botão de edição/categoria'),
    (r'\{\{[Bb]otão de edição/correlatos', r'{{SUBST:Botão de edição/correlatos'),
    (r'\{\{[Bb]otão de edição/Disambig', r'{{SUBST:Botão de edição/Disambig'),
    (r'\{\{[Bb]otão de edição/fim', r'{{SUBST:Botão de edição/fim'),
    (r'\{\{[Bb]otão de edição/impróprio', r'{{SUBST:Botão de edição/impróprio'),
    (r'\{\{[Bb]otão de edição/inicio', r'{{SUBST:Botão de edição/inicio'),
    (r'\{\{[Bb]otão de edição/matrad', r'{{SUBST:Botão de edição/matrad'),
    (r'\{\{[Bb]otão de edição/NowCommonsThis', r'{{SUBST:Botão de edição/NowCommonsThis'),
    (r'\{\{[Bb]otão de edição/predef', r'{{SUBST:Botão de edição/predef'),
    (r'\{\{[Bb]otão de edição/redirect', r'{{SUBST:Botão de edição/redirect'),
    (r'\{\{[Bb]otão de edição/small', r'{{SUBST:Botão de edição/small'),
    (r'\{\{[Bb]otão de edição/strike', r'{{SUBST:Botão de edição/strike'),
    (r'\{\{[Bb]otão de edição/suspeito', r'{{SUBST:Botão de edição/suspeito'),
    (r'\{\{[Bb]otão de edição/Tabela', r'{{SUBST:Botão de edição/Tabela'),
    (r'\{\{[Bb]otão de edição/VD[Aa]', r'{{SUBST:Botão de edição/VD[Aa]'),
    (r'\{\{[Bb]ranqueio', r'{{SUBST:Branqueio'),
    (r'\{\{[Bb]rasil/Convite', r'{{SUBST:Brasil/Convite'),
    (r'\{\{udismo/Convite', r'{{SUBST:Budismo/Convite'),
    (r'\{\{[Bb]v-av', r'{{SUBST:Bv-av'),
    (r'\{\{[Bb]v-av-registrado/Testes', r'{{SUBST:Bv-av-registrado/Testes'),
    (r'\{\{[Bb]v-rand', r'{{SUBST:Bv-rand'),
    (r'\{\{[Bb]v-tutoria', r'{{SUBST:Bv-tutoria'),
    (r'\{\{[Cc]alado', r'{{SUBST:Calado'),
    (r'\{\{[Cc]ancelada', r'{{SUBST:Cancelada'),
    (r'\{\{[Cc]ancelado', r'{{SUBST:Cancelado'),
    (r'\{\{[Cc]andidatar', r'{{SUBST:Candidatar'),
    (r'\{\{[Cc]arnaval/Convite', r'{{SUBST:Carnaval/Convite'),
    (r'\{\{[Cc]artoon Network/Convite', r'{{SUBST:Cartoon Network/Convite'),
    (r'\{\{[Cc]atolicismo/Convite', r'{{SUBST:Catolicismo/Convite'),
    (r'\{\{[Cc]horo', r'{{SUBST:Choro'),
    (r'\{\{[Cc]iclismo/Convite', r'{{SUBST:Ciclismo/Convite'),
    (r'\{\{[Cc]iência da Computação/Convite', r'{{SUBST:Ciência da Computação/Convite'),
    (r'\{\{[Cc]iências sociais/Convite', r'{{SUBST:Ciências sociais/Convite'),
    (r'\{\{[Cc]inema/Convite', r'{{SUBST:Cinema/Convite'),
    (r'\{\{[Cc]itação', r'{{SUBST:Citação'),
    (r'\{\{[Cc]omentário', r'{{SUBST:Comentário'),
    (r'\{\{[Cc]oncluído', r'{{SUBST:Concluído'),
    (r'\{\{[Cc]oncordo', r'{{SUBST:Concordo'),
    (r'\{\{[Cc]onfirmada', r'{{SUBST:Confirmada'),
    (r'\{\{[Cc]onfirmado', r'{{SUBST:Confirmado'),
    (r'\{\{[Cc]onfirmado-sc', r'{{SUBST:Confirmado-sc'),
    (r'\{\{[Cc]onfirmo', r'{{SUBST:Confirmo'),
    (r'\{\{[Cc]onstrução atual', r'{{SUBST:Construção atual'),
    (r'\{\{[Cc]onstrução futra', r'{{SUBST:Construção futra'),
    (r'\{\{[Cc]ontra', r'{{SUBST:Contra'),
    (r'\{\{[Cc]onvite', r'{{SUBST:Convite'),
    (r'\{\{[Cc]onvite ceticismo', r'{{SUBST:Convite ceticismo'),
    (r'\{\{[Cc]onvite destaque', r'{{SUBST:Convite destaque'),
    (r'\{\{[Cc]onvite vdl', r'{{SUBST:Convite vdl'),
    (r'\{\{[Cc]onvite wikiclube', r'{{SUBST:Convite wikiclube'),
    (r'\{\{[Cc]onvite WP[Aa]mb', r'{{SUBST:Convite WP[Aa]mb'),
    (r'\{\{[Cc]onvite-antropologia', r'{{SUBST:Convite-antropologia'),
    (r'\{\{[Cc]onvite-artes marciais', r'{{SUBST:Convite-artes marciais'),
    (r'\{\{[Cc]onvite-astronomia', r'{{SUBST:Convite-astronomia'),
    (r'\{\{[Cc]onvite-[Aa]utomobilismo', r'{{SUBST:Convite-[Aa]utomobilismo'),
    (r'\{\{[Cc]onvite-autorrevisor', r'{{SUBST:Convite-autorrevisor'),
    (r'\{\{[Cc]onvite-biologia', r'{{SUBSTConvite-biologia'),
    (r'\{\{[Cc]onvite-biologia celular', r'{{SUBST:Convite-biologia celular'),
    (r'\{\{[Cc]onvite-cantatasbach', r'{{SUBST:Convite-cantatasbach'),
    (r'\{\{[Cc]onvite-capitais', r'{{SUBST:Convite-capitais'),
    (r'\{\{[Cc]onvite-cidades', r'{{SUBST:Convite-cidades'),
    (r'\{\{[Cc]onvite-cinema', r'{{SUBST:Convite-cinema'),
    (r'\{\{[Cc]onvite-desporto', r'{{SUBST:Convite-desporto'),
    (r'\{\{[Cc]onvite-dramatrgia', r'{{SUBST:Convite-dramatrgia'),
    (r'\{\{[Cc]onvite-eliminador', r'{{SUBST:Convite-eliminador'),
    (r'\{\{[Cc]onvite-entretenimento', r'{{SUBST:Convite-entretenimento'),
    (r'\{\{[Cc]onvite-eventos multiesportivos', r'{{SUBST:Convite-eventos multiesportivos'),
    (r'\{\{[Cc]onvite-filosofia', r'{{SUBST:Convite-filosofia'),
    (r'\{\{[Cc]onvite-física', r'{{SUBST:Convite-física'),
    (r'\{\{[Cc]onvite-Galizaplus', r'{{SUBST:Convite-Galizaplus'),
    (r'\{\{[Cc]onvite-Goiana', r'{{SUBST:Convite-Goiana'),
    (r'\{\{[Cc]onvite-grandelisboa', r'{{SUBST:Convite-grandelisboa'),
    (r'\{\{[Cc]onvite-H[Aa]P', r'{{SUBST:Convite-H[Aa]P'),
    (r'\{\{[Cc]onvite-Madeira', r'{{SUBST:Convite-Madeira'),
    (r'\{\{[Cc]onvite-matemática', r'{{SUBST:onvite-matemática'),
    (r'\{\{[Cc]onvite-maw', r'{{SUBST:Convite-maw'),
    (r'\{\{[Cc]onvite-música', r'{{SUBST:Convite-música'),
    (r'\{\{[Cc]onvite-reversor', r'{{SUBST:Convite-reversor'),
    (r'\{\{[Cc]onvite-saúde', r'{{SUBST:Convite-saúde'),
    (r'\{\{[Cc]-wikigeografia', r'{{SUBST:Convite-wikigeografia'),
    (r'\{\{[Cc]onvite-Wikinotícias', r'{{SUBST:Convite-Wikinotícias'),
    (r'\{\{[Cc]onvite-WikiRio', r'{{SUBST:Convite-WikiRio'),
    (r'\{\{[Cc]onvite-WikiSampa', r'{{SUBST:Convite-WikiSampa'),
    (r'\{\{[Cc]ore', r'{{SUBST:Core'),
    (r'\{\{[Cc]orinthians/Convite', r'{{SUBST:Corinthians/Convite'),
    (r'\{\{[Cc]orrigido', r'{{SUBST:Corrigido'),
    (r'\{\{[Cc]orrtks', r'{{SUBST:Corrtks'),
    (r'\{\{[Cc]P', r'{{SUBST:CP'),
    (r'\{\{[Cc]QD', r'{{SUBST:CQD'),
    (r'\{\{[Cc]riar PU', r'{{SUBST:Criar PU'),
    (r'\{\{[Cc]ultra livre/Convite', r'{{SUBST:Cultra livre/Convite'),
    (r'\{\{[Cc]rti', r'{{SUBST:Crti'),
    (r'\{\{[Cc]WpPa', r'{{SUBST:CWpPa'),
    (r'\{\{[Dd]esaprovado', r'{{SUBST:Desaprovado'),
    (r'\{\{[Dd]esaprovo', r'{{SUBST:Desaprovo'),
    (r'\{\{[Dd]esnecessário', r'{{SUBST:Desnecessário'),
    (r'\{\{[Dd]esporto atual', r'{{SUBST:Desporto atual'),
    (r'\{\{[Dd]esporto futro', r'{{SUBST:Desporto futro'),
    (r'\{\{[Dd]estaquei', r'{{SUBST:Destaquei'),
    (r'\{\{[Dd]igimon/Convite', r'{{SUBST:Digimon/Convite'),
    (r'\{\{[Dd]ireito ao voto', r'{{SUBST:Direito ao voto'),
    (r'\{\{[Dd]ireito/Convite', r'{{SUBST:Direito/Convite'),
    (r'\{\{[Dd]ireitos animais/Convite', r'{{SUBST:Direitos animais/Convite'),
    (r'\{\{[Dd]ireitos animais/Convite interesse', r'{{SUBST:Direitos animais/Convite interesse'),
    (r'\{\{[Dd]iscordo', r'{{SUBST:Discordo'),
    (r'\{\{[Dd]iscussão de bloqueio', r'{{SUBST:Discussão de bloqueio'),
    (r'\{\{[Dd]isney/Convite', r'{{SUBST:Disney/Convite'),
    (r'\{\{[Dd]oente', r'{{SUBST:Doente'),
    (r'\{\{[Dd]oeu', r'{{SUBST:Doeu'),
    (r'\{\{[Dd]oing', r'{{SUBST:Doing'),
    (r'\{\{[Dd]one', r'{{SUBST:Done'),
    (r'\{\{[Dd]ormente', r'{{SUBST:ormente'),
    (r'\{\{[Dd]tag', r'{{SUBST:Dtag'),
    (r'\{\{[Dd]úvida', r'{{SUBST:Dúvida'),
    (r'\{\{[Ee]ca', r'{{SUBST:Eca'),
    (r'\{\{[Ee]conomia/Convite', r'{{SUBST:Economia/Convite'),
    (r'\{\{[Ee]leição futra', r'{{SUBST:leição futra'),
    (r'\{\{[Ee]liminar', r'{{SUBST:Eliminar'),
    (r'\{\{[Ee]m análise', r'{{SUBST:Em análise'),
    (r'\{\{[Ee]m espera', r'{{SUBST:Em espera'),
    (r'\{\{[Ee]m espera2', r'{{SUBST:Em espera2'),
    (r'\{\{[Ee]m exibição', r'{{SUBST:Em exibição'),
    (r'\{\{[Ee]m progresso', r'{{SUBST:Em progresso'),
    (r'\{\{[Ee]mbaraçado', r'{{SUBST:Embaraçado'),
    (r'\{\{[Ee]ndosso', r'{{SUBST:Endosso'),
    (r'\{\{[Ee]ntretenimento/Convite', r'{{SUBST:Entretenimento/Convite'),
    (r'\{\{[Ee]sperando', r'{{SUBST:Esperando'),
    (r'\{\{[Ee]SR', r'{{SUBST:ESR'),
    (r'\{\{[Ee]SR-banda', r'{{SUBST:ESR-banda'),
    (r'\{\{[Ee]SR-bio', r'{{SUBST:ESR-bio'),
    (r'\{\{[Ee]SR-ficheiro', r'{{SUBST:ESR-ficheiro'),
    (r'\{\{[Ee]SR-matrad', r'{{SUBST:ESR-matrad'),
    (r'\{\{[Ee]SR-organização', r'{{SUBST:ESR-organização'),
    (r'\{\{[Ee]rovisão/Convite', r'{{SUBST:Erovisão/Convite'),
    (r'\{\{[Ee]v-atual', r'{{SUBST:Ev-atual'),
    (r'\{\{[Ee]vento musical futro', r'{{SUBST:Evento musical futro'),
    (r'\{\{[Ee]xtinto', r'{{SUBST:Extinto'), 
    (r'\{\{[Ff]-de', r'{{SUBST:F-de'), 
    (r'\{\{[Ff]acepalm', r'{{SUBST:Facepalm'), 
    (r'\{\{[Ff]antochada', r'{{SUBST:Fantochada'), 
    (r'\{\{[Ff]eita', r'{{SUBST:Feita'), 
    (r'\{\{[Ff]eito', r'{{SUBST:Feito'), 
    (r'\{\{[Ff]errovipédia/Convite', r'{{SUBST:Ferrovipédia/Convite'), 
    (r'\{\{[Ff]ilme futro', r'{{SUBST:Filme futro'), 
    (r'\{\{[Ff]iltrado', r'{{SUBST:Filtrado'), 
    (r'\{\{[Ff]im-tutoria', r'{{SUBST:Fim-tutoria'), 
    (r'\{\{[Ff]inalFantasy/Convite', r'{{SUBST:FinalFantasy/Convite'), 
    (r'\{\{[Ff]mtn', r'{{SUBST:Fmtn'),
    (r'\{\{[Ff]mtnx', r'{{SUBST:Fmtnx'), 
    (r'\{\{[Ff]ne', r'{{SUBST:Fne'), 
    (r'\{\{[Ff]orças [Aa]rmadas/Convite', r'{{SUBSTForças [Aa]rmadas/Convite'), 
    (r'\{\{[Ff]órmula 1/Convite', r'{{SUBST:Fórmula 1/Convite'), 
    (r'\{\{[Ff]undir', r'{{SUBST:Fundir'), 
    (r'\{\{[Ff]utebol/Convite', r'{{SUBST:Futebol/Convite'), 
    (r'\{\{[Ff]utra exploração espacial', r'{{SUBST:Futra exploração espacial'), 
    (r'\{\{[Ff]utramente', r'{{SUBST:Futramente'),
    (r'\{\{[Ff]utro álbum', r'{{SUBST:Futro álbum'),
    (r'\{\{[Ff]utro quadrinhos', r'{{SUBST:Futro quadrinhos'),
    (r'\{\{[Gg]ames/Convite', r'{{SUBST:Games/Convite'),
    (r'\{\{[Gg]eografia/Convite', r'{{SUBST:Geografia/Convite'),
    (r'\{\{[Gg]inástica/Convite', r'{{SUBST:Ginástica/Convite'),
    (r'\{\{[Gg]oiânia/Convite', r'{{SUBST:Goiânia/Convite'),
    (r'\{\{[Gg]ospel/Convite', r'{{SUBST:Gospel/Convite'),
    (r'\{\{[Gg]rr', r'{{SUBST:Grr'),
    (r'\{\{[Gg]rr2', r'{{SUBST:Grr2'),
    (r'\{\{[Gg]uerra atual', r'{{SUBST:Guerra atual'),
    (r'\{\{[Gg]uerras Médicas/Convite', r'{{SUBST:Guerras Médicas/Convite'),
    (r'\{\{[Gg]uitarra/Convite', r'{{SUBST:Guitarra/Convite'),
    (r'\{\{[Hh]A', r'{{SUBST:HA'),
    (r'\{\{[Hh]CUE', r'{{SUBST:HCUE'),
    (r'\{\{[Hh]ip hop/Convite', r'{{SUBST:Hip hop/Convite'),
    (r'\{\{[Hh]istória e sociedade/Convite', r'{{SUBST:História e sociedade/Convite'),
    (r'\{\{[Hh]istória militar/Convite', r'{{SUBST:História militar/Convite'),
    (r'\{\{[Hh]um', r'{{SUBST:Hum'),
    (r'\{\{[Ii] GP Wikimedia Brasil/Convite', r'{{SUBST:I GP Wikimedia Brasil/Convite'),
    (r'\{\{[Ii]*', r'{{SUBST:I*'),
    (r'\{\{[Ii]deia', r'{{SUBST:Ideia'),
    (r'\{\{[Ii]mpraticável', r'{{SUBST:Impraticável'),
    (r'\{\{[Ii]nadequado', r'{{SUBST:Inadequado'),
    (r'\{\{[Ii]nconclusiva', r'{{SUBST:Inconclusiva'),
    (r'\{\{[Ii]nconclusivo', r'{{SUBST:Inconclusivo'),
    (r'\{\{[Ii]ndicação', r'{{SUBST:Indicação'),
    (r'\{\{[Ii]nfo/Campeonato de wrestling', r'{{SUBST:Info/Campeonato de wrestling'),
    (r'\{\{[Ii]nfo/Empresa-en', r'{{SUBST:Info/Empresa-en'),
    (r'\{\{[Ii]nfo/Wrestler', r'{{SUBST:Info/Wrestler'),
    (r'\{\{[Ii]nfo/Wrestling event', r'{{SUBST:Info/Wrestling event'),
    (r'\{\{[Ii]nfo/Wrestling team', r'{{SUBST:Info/Wrestling team'),
    (r'\{\{[Ii]nfobox album', r'{{SUBST:Infobox album'),
    (r'\{\{[Ii]nfobox tool', r'{{SUBST:Infobox tool'),
    (r'\{\{[Ii]nfobox VG', r'{{SUBST:Infobox VG'),
    (r'\{\{[Ii]nformação2', r'{{SUBST:Informação2'),
    (r'\{\{[Ii]nternetquelle', r'{{SUBST:Internetquelle'),
    (r'\{\{[Ii]nvertebrados/Convite', r'{{SUBST:Invertebrados/Convite'),
    (r'\{\{[Ii]W', r'{{SUBST:IW'),
    (r'\{\{[Jj]á parou', r'{{SUBST:Já parou'),
    (r'\{\{[Jj]azz/Convite', r'{{SUBST:Jazz/Convite'),
    (r'\{\{[Jj]ogo futro', r'{{SUBST:Jogo futro'),
    (r'\{\{[Jj]ornalismo/Convite', r'{{SUBST:Jornalismo/Convite'),
    (r'\{\{[Ll]âmpada', r'{{SUBST:Lâmpada'),
    (r'\{\{[Ll]e', r'{{SUBST:Le'),
    (r'\{\{[Ll]Esp/Convite', r'{{SUBST:LEsp/Convite'),
    (r'\{\{[Ll]GBT Convite', r'{{SUBST:LGBT Convite'),
    (r'\{\{[Ll]igação externa', r'{{SUBST:Ligação externa'),
    (r'\{\{[Ll]igações externas', r'{{SUBST:Ligações externas'),
    (r'\{\{[Ll]ike', r'{{SUBST:Like'),
    (r'\{\{[Ll]íngua fora', r'{{SUBST:Língua fora'),
    (r'\{\{[Ll]ink externo', r'{{SUBST:Link externo'),
    (r'\{\{[Ll]inks', r'{{SUBST:Links'),
    (r'\{\{[Ll]inks externos', r'{{SUBST:Links externos'),
    (r'\{\{[Ll]inks para o exterior', r'{{SUBST:Links para o exterior'),
    (r'\{\{[Ll]iteratra/Convite', r'{{SUBST:Literatra/Convite'),
    (r'\{\{[Ll]ivro futro', r'{{SUBST:Livro futro'),
    (r'\{\{[Ll]lp', r'{{SUBST:Llp'),
    (r'\{\{[Ll]mf', r'{{SUBST:Lmf'),
    (r'\{\{[Ll]ol', r'{{SUBST:Lol'),
    (r'\{\{[Ll]ost/Convite', r'{{SUBST:Lost/Convite'),
    (r'\{\{[Ll]ouco', r'{{SUBST:Louco'),
    (r'\{\{[Ll]X', r'{{SUBST:LX'),
    (r'\{\{[Mm]-fontes', r'{{SUBST:M-fontes'),
    (r'\{\{[Mm]-recente', r'{{SUBST:M-recente'),
    (r'\{\{[Mm]ais info', r'{{SUBST:Mais info'),
    (r'\{\{[Mm]aligno', r'{{SUBST:Maligno'),
    (r'\{\{[Mm]amíferos/Convite', r'{{SUBST:Mamíferos/Convite'),
    (r'\{\{[Mm]anter', r'{{SUBST:Manter'),
    (r'\{\{[Mm]edicina/Convite', r'{{SUBST:Medicina/Convite'),
    (r'\{\{[Mm]etal/Convite', r'{{SUBST:Metal/Convite'),
    (r'\{\{[Mm]issão espacial atual', r'{{SUBST:Missão espacial atual'),
    (r'\{\{[Mm]MA/Convite', r'{{SUBST:MMA/Convite'),
    (r'\{\{[Mm]MO/Convite', r'{{SUBST:MMO/Convite'),
    (r'\{\{[Mm]oção pedida', r'{{SUBST:Moção pedida'),
    (r'\{\{[Mm]order', r'{{SUBST:Morder'),
    (r'\{\{[Mm]orte recente', r'{{SUBST:Morte recente'),
    (r'\{\{[Mm]ostrar previsão', r'{{SUBST:Mostrar previsão'),
    (r'\{\{[Mm]over', r'{{SUBST:Mover'),
    (r'\{\{[Mm]tag', r'{{SUBST:Mtag'),
    (r'\{\{[Mm]udar', r'{{SUBST:Mudar'),
    (r'\{\{[Mm]uito bom', r'{{SUBST:Muito bom'),
    (r'\{\{[Mm]úsica portuguesa/Convite', r'{{SUBST:Música portuguesa/Convite'),
    (r'\{\{[Mm]úsica/Convite', r'{{SUBST:Música/Convite'),
    (r'\{\{[Nn]ão apoio', r'{{SUBST:Não apoio'),
    (r'\{\{[Nn]ão assinou', r'{{SUBST:Não assinou'),
    (r'\{\{[Nn]ão excluímos conta', r'{{SUBST:Não excluímos conta'),
    (r'\{\{[Nn]ão há erro', r'{{SUBST:Não há erro'),
    (r'\{\{[Nn]ão responda', r'{{SUBST:Não responda'),
    (r'\{\{[Nn]ão.', r'{{SUBST:Não.'),
    (r'\{\{[Nn]ão1', r'{{SUBST:Não1'),
    (r'\{\{[Nn]atação/Convite', r'{{SUBST:Natação/Convite'),
    (r'\{\{[Nn]aval/Convite', r'{{SUBST:Naval/Convite'),
    (r'\{\{[Nn]egado', r'{{SUBST:Negado'),
    (r'\{\{[Nn]egativo', r'{{SUBST:Negativo'),
    (r'\{\{[Nn]egteste', r'{{SUBST:Negteste'),
    (r'\{\{[Nn]ervoso', r'{{SUBST:Nervoso'),
    (r'\{\{[Nn]eutra', r'{{SUBST:Neutra'),
    (r'\{\{[Nn]eutral', r'{{SUBST:Neutral'),
    (r'\{\{[Nn]eutro', r'{{SUBST:Neutro'),
    (r'\{\{[Nn]FL roster', r'{{SUBST:NFL roster'),
    (r'\{\{[Nn]im', r'{{SUBST:Nim'),
    (r'\{\{[Nn]ordeste/Convite', r'{{SUBST:Nordeste/Convite'),
    (r'\{\{[Nn]ot done', r'{{SUBST:Not done'),
    (r'\{\{[Nn]ota-adm', r'{{SUBST:Nota-adm'),
    (r'\{\{[Nn]ovapredef', r'{{SUBST:Novapredef'),
    (r'\{\{[Nn]ovo administrador', r'{{SUBST:Novo administrador'),
    (r'\{\{[Nn]ovo autorrevisor', r'{{SUBST:Novo autorrevisor'),
    (r'\{\{[Nn]ovo burocrata', r'{{SUBST:Novo burocrata'),
    (r'\{\{[Nn]ovo eliminador', r'{{SUBST:Novo eliminador'),
    (r'\{\{[Nn]ovo reversor', r'{{SUBST:Novo reversor'),
    (r'\{\{[Oo]brigado', r'{{SUBST:Obrigado'),
    (r'\{\{[Oo]brigado2', r'{{SUBST:Obrigado2'),
    (r'\{\{[Oo]bs', r'{{SUBST:Obs'),
    (r'\{\{[Oo]bservação', r'{{SUBST:Observação'),
    (r'\{\{[Oo]i!', r'{{SUBST:Oi!'),
    (r'\{\{[Oo]lhos', r'{{SUBST:Olhos'),
    (r'\{\{[Oo]pinião', r'{{SUBST:Opinião'),
    (r'\{\{[Oo]rgulho', r'{{SUBST:Orgulho'),
    (r'\{\{[Pp]ab', r'{{SUBST:Pab'),
    (r'\{\{[Pp]acman', r'{{SUBST:Pacman'),
    (r'\{\{[Pp]áginas externas', r'{{SUBST:Páginas externas'),
    (r'\{\{[Pp]arabénsSQ', r'{{SUBST:ParabénsSQ'),
    (r'\{\{[Pp]arou', r'{{SUBST:Parou'),
    (r'\{\{[Pp]ato', r'{{SUBST:Pato'),
    (r'\{\{[Pp]ato com megafone', r'{{SUBST:Pato com megafone'),
    (r'\{\{[Pp]atrimónio Mundial da UNESCO/Convite', r'{{SUBST:Património Mundial da UNESCO/Convite'),
    (r'\{\{[Pp]E inconclusiva', r'{{SUBST:PE inconclusiva'),
    (r'\{\{[Pp]E-privacidade', r'{{SUBST:PE-privacidade'),
    (r'\{\{[Pp]edido atendido', r'{{SUBST:Pedido atendido'),
    (r'\{\{[Pp]endlg', r'{{SUBST:Pendlg'),
    (r'\{\{[Pp]erfeito', r'{{SUBST:Perfeito'),
    (r'\{\{[Pp]ergunta', r'{{SUBST:Pergunta'),
    (r'\{\{[Pp]esca', r'{{SUBST:Pesca'),
    (r'\{\{[Pp]essoa atual', r'{{SUBST:Pessoa atual'),
    (r'\{\{[Pp]iscada', r'{{SUBST:Piscada'),
    (r'\{\{[Pp]lantas/Convite', r'{{SUBST:Plantas/Convite'),
    (r'\{\{[Pp]lnk2', r'{{SUBST:Plnk2'),
    (r'\{\{[Pp]oem', r'{{SUBST:Poem'),
    (r'\{\{[Pp]okémon/Convite', r'{{SUBST:Pokémon/Convite'),
    (r'\{\{[Pp]orco', r'{{SUBST:Porco'),
    (r'\{\{[Pp]ortais/Convite', r'{{SUBST:Portais/Convite'),
    (r'\{\{[Pp]ositivo', r'{{SUBST:Positivo'),
    (r'\{\{[Pp]ossivável', r'{{SUBST:Possivável'),
    (r'\{\{[Pp]ossível', r'{{SUBST:Possível'),
    (r'\{\{[Pp]rod', r'{{SUBST:Prod'),
    (r'\{\{[Pp]rodutos futuros', r'{{SUBST:Produtos futuros'),
    (r'\{\{[Pp]rograma de televisão futuro', r'{{SUBST:Programa de televisão futuro'),
    (r'\{\{[Pp]rovável', r'{{SUBST:Provável'),
    (r'\{\{[Qq]uadrocitação', r'{{SUBST:Quadrocitação'),
    (r'\{\{[Qq]uase favorável', r'{{SUBST:Quase favorável'),
    (r'\{\{[Qq]uase feito', r'{{SUBST:Quase feito'),
    (r'\{\{[Qq]uímica/Convite', r'{{SUBST:Química/Convite'),
    (r'\{\{[Rr]&B/Convite', r'{{SUBST:R&B/Convite'),
    (r'\{\{[Rr]eaberto', r'{{SUBST:Reaberto'),
    (r'\{\{[Rr]ealeza e Nobreza/Convite', r'{{SUBST:Realeza e Nobreza/Convite'),
    (r'\{\{[Rr]ecusado', r'{{SUBST:Recusado'),
    (r'\{\{[Rr]edirecionar', r'{{SUBST:Redirecionar'),
    (r'\{\{[Rr]eferências externas', r'{{SUBST:Referências externas'),
    (r'\{\{[Rr]ejeitada', r'{{SUBST:Rejeitada'),
    (r'\{\{[Rr]ejeitado', r'{{SUBST:Rejeitado'),
    (r'\{\{[Rr]elações internacionais/Convite', r'{{SUBST:Relações internacionais/Convite'),
    (r'\{\{[Rr]emover', r'{{SUBST:Remover'),
    (r'\{\{[Rr]enomeação feita', r'{{SUBST:Renomeação feita'),
    (r'\{\{[Rr]enomeação negada', r'{{SUBST:Renomeação negada'),
    (r'\{\{[Rr]eprovado', r'{{SUBST:Reprovado'),
    (r'\{\{[Rr]espondido/desnecessário', r'{{SUBST:Respondido/desnecessário'),
    (r'\{\{[Rr]espondido/feito', r'{{SUBST:Respondido/feito'),
    (r'\{\{[Rr]espondido/neg', r'{{SUBST:Respondido/neg'),
    (r'\{\{[Rr]espondido/prot', r'{{SUBST:Respondido/prot'),
    (r'\{\{[Rr]eticência', r'{{SUBST:Reticência'),
    (r'\{\{[Rr]evisão de bloqueio', r'{{SUBST:Revisão de bloqueio'),
    (r'\{\{[Rr]ock/Convite', r'{{SUBST:Rock/Convite'),
    (r'\{\{[Ss]-cat', r'{{SUBST:S-cat'),
    (r'\{\{[Ss]atélite futuro', r'{{SUBST:Satélite futuro'),
    (r'\{\{[Ss]egunda Guerra Mundial/Convite', r'{{SUBST:Segunda Guerra Mundial/Convite'),
    (r'\{\{[Ss]em comentário IP', r'{{SUBST:Sem comentário IP'),
    (r'\{\{[Ss]em relação', r'{{SUBST:Sem relação'),
    (r'\{\{[Ss]érie atual', r'{{SUBST:Série atual'),
    (r'\{\{[Ss]érie futura', r'{{SUBST:Série futura'),
    (r'\{\{[Ss]éries/Convite', r'{{SUBST:Séries/Convite'),
    (r'\{\{[Ss]impsons/Convite', r'{{SUBST:Simpsons/Convite'),
    (r'\{\{[Ss]kate/Convite', r'{{SUBST:Skate/Convite'),
    (r'\{\{[Ss]oftware futuro', r'{{SUBST:Software futuro'),
    (r'\{\{[Ss]olicitação', r'{{SUBST:Solicitação'),
    (r'\{\{[Ss]olicitado', r'{{SUBST:Solicitado'),
    (r'\{\{[Ss]olução intermediária', r'{{SUBST:Solução intermediária'),
    (r'\{\{[Ss]orriso', r'{{SUBST:Sorriso'),
    (r'\{\{[Ss]ubscrição-Correio', r'{{SUBST:Subscrição-Correio'),
    (r'\{\{[Ss]ugestão', r'{{SUBST:Sugestão'),
    (r'\{\{[Ss]uspensão', r'{{SUBST:Suspensão'),
    (r'\{\{[Ss]uspenso', r'{{SUBST:Suspenso'),
    (r'\{\{[Ss]usto', r'{{SUBST:Susto'),
    (r'\{\{[Tt]+', r'{{SUBST:T+'),
    (r'\{\{[Tt]abela bonita', r'{{SUBST:Tabela bonita'),
    (r'\{\{[Tt]elenovela atual', r'{{SUBST:Telenovela atual'),
    (r'\{\{[Tt]elenovela futura', r'{{SUBST:Telenovela futura'),
    (r'\{\{[Tt]elevisão/Convite', r'{{SUBST:Televisão/Convite'),
    (r'\{\{[Tt]ênis/Convite', r'{{SUBST:Tênis/Convite'),
    (r'\{\{[Tt]eologia/Convite', r'{{SUBST:Teologia/Convite'),
    (r'\{\{[Tt]rabalhando nisso', r'{{SUBST:Trabalhando nisso'),
    (r'\{\{[Tt]rack listing', r'{{SUBST:Track listing'),
    (r'\{\{[Tt]radução/Convite', r'{{SUBST:Tradução/Convite'),
    (r'\{\{[Tt]ravesso', r'{{SUBST:Travesso'),
    (r'\{\{[Tt]rierweiller', r'{{SUBST:Trierweiller'),
    (r'\{\{[Tt]riste', r'{{SUBST:Triste'),
    (r'\{\{[Tt]utoria/Convite', r'{{SUBST:Tutoria/Convite'),
    (r'\{\{[Uu]fologia/Convite', r'{{SUBST:Ufologia/Convite'),
    (r'\{\{[Uu]ps', r'{{SUBST:Ups'),
    (r'\{\{[Uu]ser-uaa', r'{{SUBST:User-uaa'),
    (r'\{\{[Vv]aleu', r'{{SUBST:Valeu'),
    (r'\{\{[Vv]eja também', r'{{SUBST:Veja também'),
    (r'\{\{[Vv]er também', r'{{SUBST:Ver também'),
    (r'\{\{[Vv]er Também', r'{{SUBST:Ver Também'),
    (r'\{\{[Vv]ergonha', r'{{SUBST:Vergonha'),
    (r'\{\{[Vv]erificado', r'{{SUBST:Verificado'),
    (r'\{\{[Vv]otos a favor', r'{{SUBST:Votos a favor'),
    (r'\{\{[Ww]AM 2016/aval', r'{{SUBST:WAM 2016/aval'),
    (r'\{\{[Ww]AM 2016/IP', r'{{SUBST:WAM 2016/IP'),
    (r'\{\{[Ww]AM/bv', r'{{SUBST:WAM/bv'),
    (r'\{\{[Ww]AM/bv-org', r'{{SUBST:WAM/bv-org'),
    (r'\{\{[Ww]AM/bv-org2017', r'{{SUBST:WAM/bv-org2017'),
    (r'\{\{[Ww]AM/bv-org2018', r'{{SUBST:WAM/bv-org2018'),
    (r'\{\{[Ww]AM/bv2017', r'{{SUBST:WAM/bv2017'),
    (r'\{\{[Ww]AM/bv2018', r'{{SUBST:WAM/bv2018'),
    (r'\{\{[Ww]AM/convite', r'{{SUBST:WAM/convite'),
    (r'\{\{[Ww]AM/convite-org', r'{{SUBST:WAM/convite-org'),
    (r'\{\{[Ww]AM/convite-org2017', r'{{SUBST:WAM/convite-org2017'),
    (r'\{\{[Ww]AM/convite2017', r'{{SUBST:WAM/convite2017'),
    (r'\{\{[Ww]AM/convite2019', r'{{SUBST:WAM/convite2019'),
    (r'\{\{[Ww]ikipedia/CA/Aviso envolvido', r'{{SUBST:Wikipedia/CA/Aviso envolvido'),
    (r'\{\{[Ww]ma', r'{{SUBST:Wma'),
    (r'\{\{[Ww]mfx', r'{{SUBST:Wmfx'),
    (r'\{\{[Ww]mfx2', r'{{SUBST:Wmfx2'),
    (r'\{\{[Ww]mv', r'{{SUBST:Wmv'),
    (r'\{\{[Ww]mw', r'{{SUBST:Wmw'),
    (r'\{\{[Ww]mw1', r'{{SUBST:Wmw1'),
    (r'\{\{[Ww]mwb', r'{{SUBST:Wmwb'),
    (r'\{\{[Ww]mwc', r'{{SUBST:Wmwc'),
    (r'\{\{[Ww]mwl', r'{{SUBST:Wmwl'),
    (r'\{\{[Ww]mwm', r'{{SUBST:Wmwm'),
    (r'\{\{[Ww]mwp', r'{{SUBST:Wmwp'),
    (r'\{\{[Ww]mwrx', r'{{SUBST:Wmwrx'),
    (r'\{\{[Ww]mws', r'{{SUBST:Wmws'),
    (r'\{\{[Ww]restling/Convite', r'{{SUBST:Wrestling/Convite'),
    (r'\{\{[Ww]restling/Inativo', r'{{SUBSTWrestling/Inativo'),
    (r'\{\{[Ww]U Concluído', r'{{SUBST:WU Concluído'),
    (r'\{\{[Ww]U Não concluído', r'{{SUBST:WU Não concluído'),
    (r'\{\{[Xx]', r'{{SUBST:X'),
    (r'\{\{[Xx]adrez/Convite', r'{{SUBST:Xadrez/Convite'),
    (r'\{\{[Xx]D', r'{{SUBST:XD'),
    (r'\{\{[Xx]P', r'{{SUBST:XP'),
    (r'\{\{[Zz]Z', r'{{SUBST:ZZ')
    ]
}


    
