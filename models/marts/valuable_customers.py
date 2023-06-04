{{
    config(
        materialized='table'
    )
}}

SELECT * FROM {{ref(customers)}} where count_lifetime_orders > 5
