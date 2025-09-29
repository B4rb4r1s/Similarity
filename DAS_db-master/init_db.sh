#!/bin/bash
psql -U happy_user -d happy_db <<-EOSQL
    BEGIN;
        CREATE TABLE DOCUMENTS(
            ID SERIAL PRIMARY KEY,
            filename VARCHAR,
            content TEXT,
            text_tesseract TEXT,
            text_dedoc TEXT
            big_summary TEXT,
            summary TEXT,
            upload_time TIMESTAMP,
            doc_format TEXT,
        );
        CREATE TABLE NAMED_ENTITIES(
            ID SERIAL PRIMARY KEY,
            doc_id INTEGER,
            entity VARCHAR,
            value VARCHAR
        );
        CREATE TABLE METADATA(
            ID SERIAL PRIMARY KEY,
            doc_id INTEGER,
            format VARCHAR,
            author VARCHAR,
            creator VARCHAR,
            title VARCHAR,
            subject VARCHAR,
            keywords VARCHAR,
            creation_date TIMESTAMP,
            producer VARCHAR
        );
        CREATE TABLE TABLES(
            ID SERIAL PRIMARY KEY,
            doc_id INTEGER REFERENCES DOCUMENTS,
            header TEXT[], 
            rows TEXT[]
        );

        CREATE TABLE elibrary_dataset (
            ID SERIAL PRIMARY KEY,
            filename character varying,
            text_dedoc text,
            tag character varying,
            target_summary text,
            lingvo_summary text,
            mt5_summary text,
            mbart_summary text,
            rut5_summary text,
            t5_summary text,
        );

        CREATE TABLE similarity_metrics (
            ID SERIAL PRIMARY KEY,
            doc_id integer NOT NULL,
            text_source text,
            text_target text,
            cointegrated_rubert_tiny2 double precision,
            sergeyzh_labse_ru_sts double precision,
            uaritm_multilingual_en_uk_pl_ru double precision,
            deeppavlov_rubert_base_cased_sentence double precision,
        );

    COMMIT;
EOSQL