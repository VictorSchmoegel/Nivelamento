create table 1T2022 (
    data DATE, REG_ANS VARCHAR(255), CD_CONTA_CONTABIL VARCHAR(255), DESCRICAO VARCHAR(255), VL_SALDO_INICIAL DECIMAL(20, 2), VL_SALDO_FINAL DECIMAL(20, 2)
);

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\1T2022.csv" INTO
TABLE `1t2022` CHARACTER SET latin1 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 rows (
    @data, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @vl_saldo_inicial, @vl_saldo_final
)
SET
    VL_SALDO_INICIAL =
REPLACE (@vl_saldo_inicial, ',', '.'),
    VL_SALDO_FINAL =
REPLACE (@vl_saldo_final, ',', '.'),
    data = STR_TO_DATE(@data, '%d/%m/%Y');