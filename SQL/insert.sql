--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

-- Data for Name: regiao; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.regiao (pk_regiao, nome) VALUES (1, 'Sudeste');
INSERT INTO public.regiao (pk_regiao, nome) VALUES (2, 'Sul');
INSERT INTO public.regiao (pk_regiao, nome) VALUES (3, 'Nordeste');
INSERT INTO public.regiao (pk_regiao, nome) VALUES (4, 'Norte');
INSERT INTO public.regiao (pk_regiao, nome) VALUES (5, 'Centro-oeste');



-- Data for Name: operadora; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (1, 'EQUATORIAL PARÁ', 9.44, 4);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (2, 'CERON ENERGISA - CENTRAIS ELÉTRICAS DE RONDÔNIA', 22.11, 4);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (3, 'ETO - ENERGISA TOCANTINS', 13.97, 4);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (4, 'ELETROACRE ENERGISA', 10.8, 4);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (5, 'BOA VISTA ENERGIA - RORAIMA', 20.01, 4);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (6, 'CEA - COMPANHIA DE ELETRECIDADE DO AMAPÁ', 2.75, 4);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (7, 'COPEL - COMPANHIA PARAENSE DE ENERGIA', 26.41, 2);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (8, 'CELESC - CENTRAIS ELÉTRICAS DE SANTA CATARINA', 15.7, 2);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (9, 'RGE SUL - DISTRIBUIDORA GAÚCHA DE ENERGIA', 22.59, 2);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (10, 'CEEE - COMPANHIA ESTADUAL DE ENERGIA ELÉTRICA', 22.95, 2);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (11, 'ENEL DISTRIBUIÇÃO SÃO PAULO - ELETROPAULO', 24.72, 1);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (12, 'CEMIG - COMPANHIA ENERGÉTICA DE MINAS GERAIS', 21.75, 1);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (13, 'LIGHT - LIGHT SERVIÇOS DE ELETRICIDADE', 23.72, 1);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (14, 'CPFL PAULISTA - COMPANHIA PAULISTA DE FORÇA E LUZ', 25.99, 1);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (15, 'ENEL DISTRIBUIÇÃO RIO - AMPLA', 18.51, 1);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (16, 'ELEKTRO - ELEKTRO ELETRICIDADE E SERVIÇOS', 23.01, 1);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (17, 'EDP SÃO PAULO - BANDEIRANTE', 19.63, 1);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (18, 'EDP ESPÍRITO SANTO - ESCELSA', 22.9, 1);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (19, 'CPFL PIRATININGA', 22.93, 1);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (20, 'CELG - ENEL DISTRIBUIÇÃO GOIÁS', 19.88, 5);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (21, 'EMT - ENERGISA MATO GROSSO', 20.31, 5);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (22, 'E MS - ENERGISA MATO GROSSO DO SUL', 19.18, 5);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (23, 'NEONERGIA - BRASÍLIA', 20.36, 5);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (24, 'COELBA - COMPANHIA DE ELETRICIDADE DO ESTADO DA BAHIA', 14.51, 3);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (25, 'CELPE - COMPANHIA ENERGÉTICA DE PERNAMBUCO', 21.86, 3);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (26, 'COELCE - ENEL DISTRIBUIÇÃO CEARÁ', 20.23, 3);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (27, 'CEMAR - COMPANHIA ENERGÉTICA DO MARANHÃO', 15.62, 3);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (28, 'COSERN - COMPANHIA ENERGÉTICA DO RIO GRANDE DO NORTE', 19.33, 3);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (29, 'CEPISA - EQUATORIAL ENERGIA PIAUÍ', 19.47, 3);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (30, 'CEAL - EQUATORIAL ENERGIA ALAGOAS ', 15.19, 3);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (31, 'EPB - ENERGISA PARAÍBA', 19.75, 3);
INSERT INTO public.operadora (pk_operadora, nome, percentual_reducao, id_regiao) VALUES (32, 'ESE - ENERGISA SERGIPE', 16.87, 3);


-- Data for Name: consulta; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.consulta (pk_consulta, nome, nome_uniform, celular, gasto_atual, percentual_economia, gasto_simulado, data_insercao, id_operadora) VALUES (220, 'usuario 2', 'usuario 2', '99222222222', 4567.89, 22.95, 3519.5592450000004, '2023-12-11 10:37:39.887019', 10);
INSERT INTO public.consulta (pk_consulta, nome, nome_uniform, celular, gasto_atual, percentual_economia, gasto_simulado, data_insercao, id_operadora) VALUES (221, 'Usuario 1', 'usuario 1', '99111111111', 1234.56, 24.72, 929.376768, '2023-12-11 10:37:39.887019', 11);
INSERT INTO public.consulta (pk_consulta, nome, nome_uniform, celular, gasto_atual, percentual_economia, gasto_simulado, data_insercao, id_operadora) VALUES (222, 'Usuario 3', 'usuario 3', '99333333333', 483.48, 14.51, 413.327052, '2023-12-11 10:37:39.887019', 24);
INSERT INTO public.consulta (pk_consulta, nome, nome_uniform, celular, gasto_atual, percentual_economia, gasto_simulado, data_insercao, id_operadora) VALUES (223, 'Usuario 4', 'usuario 4', '99444444444', 5678.9, 9.44, 5142.811839999999, '2023-12-11 10:37:39.887019', 1);
INSERT INTO public.consulta (pk_consulta, nome, nome_uniform, celular, gasto_atual, percentual_economia, gasto_simulado, data_insercao, id_operadora) VALUES (224, 'Usuario 5', 'usuario 5', '99555555555', 2598, 19.88, 2081.5176, '2023-12-11 10:37:39.887019', 20);

--
-- PostgreSQL database dump complete
--
