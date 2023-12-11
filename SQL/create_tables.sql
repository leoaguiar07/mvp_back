--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

-- Started on 2023-12-11 12:39:15

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 41228)
-- Name: consulta; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.consulta (
    pk_consulta integer NOT NULL,
    nome character varying(140) NOT NULL,
    nome_uniform character varying(140) NOT NULL,
    celular character varying(11),
    gasto_atual double precision NOT NULL,
    percentual_economia double precision NOT NULL,
    gasto_simulado double precision NOT NULL,
    data_insercao timestamp without time zone,
    id_operadora integer NOT NULL
);


ALTER TABLE public.consulta OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 41227)
-- Name: consulta_pk_consulta_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.consulta_pk_consulta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.consulta_pk_consulta_seq OWNER TO postgres;

--
-- TOC entry 4809 (class 0 OID 0)
-- Dependencies: 219
-- Name: consulta_pk_consulta_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.consulta_pk_consulta_seq OWNED BY public.consulta.pk_consulta;


--
-- TOC entry 218 (class 1259 OID 41156)
-- Name: operadora; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.operadora (
    pk_operadora integer NOT NULL,
    nome character varying(140) NOT NULL,
    percentual_reducao double precision NOT NULL,
    id_regiao integer NOT NULL
);


ALTER TABLE public.operadora OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 41155)
-- Name: operadora_pk_operadora_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.operadora_pk_operadora_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.operadora_pk_operadora_seq OWNER TO postgres;

--
-- TOC entry 4810 (class 0 OID 0)
-- Dependencies: 217
-- Name: operadora_pk_operadora_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.operadora_pk_operadora_seq OWNED BY public.operadora.pk_operadora;


--
-- TOC entry 216 (class 1259 OID 41147)
-- Name: regiao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.regiao (
    pk_regiao integer NOT NULL,
    nome character varying(140) NOT NULL
);


ALTER TABLE public.regiao OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 41146)
-- Name: regiao_pk_regiao_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.regiao_pk_regiao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.regiao_pk_regiao_seq OWNER TO postgres;

--
-- TOC entry 4811 (class 0 OID 0)
-- Dependencies: 215
-- Name: regiao_pk_regiao_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.regiao_pk_regiao_seq OWNED BY public.regiao.pk_regiao;


--
-- TOC entry 4646 (class 2604 OID 41231)
-- Name: consulta pk_consulta; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consulta ALTER COLUMN pk_consulta SET DEFAULT nextval('public.consulta_pk_consulta_seq'::regclass);


--
-- TOC entry 4645 (class 2604 OID 41159)
-- Name: operadora pk_operadora; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operadora ALTER COLUMN pk_operadora SET DEFAULT nextval('public.operadora_pk_operadora_seq'::regclass);


--
-- TOC entry 4644 (class 2604 OID 41150)
-- Name: regiao pk_regiao; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.regiao ALTER COLUMN pk_regiao SET DEFAULT nextval('public.regiao_pk_regiao_seq'::regclass);


--
-- TOC entry 4656 (class 2606 OID 41235)
-- Name: consulta consulta_celular_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consulta
    ADD CONSTRAINT consulta_celular_key UNIQUE (celular);


--
-- TOC entry 4658 (class 2606 OID 41233)
-- Name: consulta consulta_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consulta
    ADD CONSTRAINT consulta_pkey PRIMARY KEY (pk_consulta);


--
-- TOC entry 4652 (class 2606 OID 41163)
-- Name: operadora operadora_nome_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operadora
    ADD CONSTRAINT operadora_nome_key UNIQUE (nome);


--
-- TOC entry 4654 (class 2606 OID 41161)
-- Name: operadora operadora_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operadora
    ADD CONSTRAINT operadora_pkey PRIMARY KEY (pk_operadora);


--
-- TOC entry 4648 (class 2606 OID 41154)
-- Name: regiao regiao_nome_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.regiao
    ADD CONSTRAINT regiao_nome_key UNIQUE (nome);


--
-- TOC entry 4650 (class 2606 OID 41152)
-- Name: regiao regiao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.regiao
    ADD CONSTRAINT regiao_pkey PRIMARY KEY (pk_regiao);


--
-- TOC entry 4660 (class 2606 OID 41236)
-- Name: consulta consulta_id_operadora_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consulta
    ADD CONSTRAINT consulta_id_operadora_fkey FOREIGN KEY (id_operadora) REFERENCES public.operadora(pk_operadora);


--
-- TOC entry 4659 (class 2606 OID 41164)
-- Name: operadora operadora_id_regiao_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operadora
    ADD CONSTRAINT operadora_id_regiao_fkey FOREIGN KEY (id_regiao) REFERENCES public.regiao(pk_regiao);


-- Completed on 2023-12-11 12:39:16

--
-- PostgreSQL database dump complete
--

