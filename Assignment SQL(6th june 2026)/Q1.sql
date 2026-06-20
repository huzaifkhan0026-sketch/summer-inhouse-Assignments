USE data_bank;

--------------------------------------------------
-- View Tables
--------------------------------------------------
SELECT * FROM customer_transactions;
SELECT * FROM customer_nodes;
SELECT * FROM regions;

--------------------------------------------------
-- 1. How many unique nodes are there on the Data Bank system?
--------------------------------------------------
SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM customer_nodes;

--------------------------------------------------
-- 2. What is the number of nodes per region?
--------------------------------------------------
SELECT
    r.region_name,
    COUNT(DISTINCT cn.node_id) AS nodes_per_region
FROM customer_nodes cn
JOIN regions r
    ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY r.region_name;

--------------------------------------------------
-- 3. How many customers are allocated to each region?
--------------------------------------------------
SELECT
    r.region_name,
    COUNT(DISTINCT cn.customer_id) AS customers_per_region
FROM customer_nodes cn
JOIN regions r
    ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY r.region_name;

--------------------------------------------------
-- 4. How many days on average are customers
--    reallocated to a different node?
--------------------------------------------------
SELECT
    AVG(CAST(DATEDIFF(DAY, start_date, end_date) AS FLOAT))
        AS avg_reallocation_days
FROM customer_nodes
WHERE end_date <> '9999-12-31';

--------------------------------------------------
-- 5. Median, 80th and 95th percentile
--    reallocation days for each region
--------------------------------------------------
SELECT DISTINCT
    r.region_name,

    PERCENTILE_CONT(0.50)
    WITHIN GROUP (
        ORDER BY DATEDIFF(DAY, cn.start_date, cn.end_date)
    ) OVER (
        PARTITION BY r.region_name
    ) AS median_days,

    PERCENTILE_CONT(0.80)
    WITHIN GROUP (
        ORDER BY DATEDIFF(DAY, cn.start_date, cn.end_date)
    ) OVER (
        PARTITION BY r.region_name
    ) AS percentile_80,

    PERCENTILE_CONT(0.95)
    WITHIN GROUP (
        ORDER BY DATEDIFF(DAY, cn.start_date, cn.end_date)
    ) OVER (
        PARTITION BY r.region_name
    ) AS percentile_95

FROM customer_nodes cn
JOIN regions r
    ON cn.region_id = r.region_id
WHERE cn.end_date <> '9999-12-31'
ORDER BY r.region_name;

--------------------------------------------------
-- 6. What is the unique count and total amount
--    for each transaction type?
--------------------------------------------------
SELECT
    txn_type,
    COUNT(*) AS transaction_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type
ORDER BY txn_type;

--------------------------------------------------
-- 7. Average total historical deposit
--    counts and amounts for all customers
--------------------------------------------------
SELECT
    AVG(CAST(deposit_count AS FLOAT))
        AS avg_deposit_count,
    AVG(CAST(deposit_amount AS FLOAT))
        AS avg_deposit_amount
FROM
(
    SELECT
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS deposit_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
) d;

--------------------------------------------------
-- 8. For each month, how many customers make
--    >1 deposit and either 1 purchase or 1 withdrawal?
--------------------------------------------------
WITH monthly_transactions AS
(
    SELECT
        customer_id,
        MONTH(txn_date) AS month_num,

        SUM(CASE
                WHEN txn_type = 'deposit'
                THEN 1 ELSE 0
            END) AS deposit_count,

        SUM(CASE
                WHEN txn_type = 'purchase'
                THEN 1 ELSE 0
            END) AS purchase_count,

        SUM(CASE
                WHEN txn_type = 'withdrawal'
                THEN 1 ELSE 0
            END) AS withdrawal_count

    FROM customer_transactions
    GROUP BY
        customer_id,
        MONTH(txn_date)
)

SELECT
    month_num,
    COUNT(*) AS customer_count
FROM monthly_transactions
WHERE deposit_count > 1
AND (
        purchase_count >= 1
        OR withdrawal_count >= 1
    )
GROUP BY month_num
ORDER BY month_num;