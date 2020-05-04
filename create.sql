-- Generated by Oracle SQL Developer Data Modeler 19.4.0.350.1424
--   at:        2020-05-04 10:56:47 EEST
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g



CREATE TABLE brand (
    brand_name VARCHAR2(30) NOT NULL
);

ALTER TABLE brand ADD CONSTRAINT brand_pk PRIMARY KEY ( brand_name );

CREATE TABLE city (
    city_name             VARCHAR2(30) NOT NULL,
    country_country_name  VARCHAR2(10) NOT NULL
);

ALTER TABLE city ADD CONSTRAINT city_pk PRIMARY KEY ( city_name );

CREATE TABLE country (
    country_name VARCHAR2(10) NOT NULL
);

ALTER TABLE country ADD CONSTRAINT country_pk PRIMARY KEY ( country_name );

CREATE TABLE ownership (
    owner_ship VARCHAR2(30) NOT NULL
);

ALTER TABLE ownership ADD CONSTRAINT ownership_pk PRIMARY KEY ( owner_ship );

CREATE TABLE store (
    store_number          VARCHAR2(30) NOT NULL,
    store_name            VARCHAR2(10) NOT NULL,
    longitude             FLOAT(2) NOT NULL,
    latitude              FLOAT(2) NOT NULL,
    brand_brand_name      VARCHAR2(30) NOT NULL,
    ownership_owner_ship  VARCHAR2(30) NOT NULL,
    city_city_name        VARCHAR2(30) NOT NULL
);

ALTER TABLE store ADD CONSTRAINT store_pk PRIMARY KEY ( store_number );

ALTER TABLE city
    ADD CONSTRAINT city_country_fk FOREIGN KEY ( country_country_name )
        REFERENCES country ( country_name );

ALTER TABLE store
    ADD CONSTRAINT store_brand_fk FOREIGN KEY ( brand_brand_name )
        REFERENCES brand ( brand_name );

ALTER TABLE store
    ADD CONSTRAINT store_city_fk FOREIGN KEY ( city_city_name )
        REFERENCES city ( city_name );

ALTER TABLE store
    ADD CONSTRAINT store_ownership_fk FOREIGN KEY ( ownership_owner_ship )
        REFERENCES ownership ( owner_ship );
