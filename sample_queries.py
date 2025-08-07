queries = {
    "Unoptimized: No WHERE": "SELECT * FROM employees",
    "Unoptimized: No index filter": "SELECT * FROM employees WHERE employee_id > 100",
    "Optimized: Indexed Column": "SELECT * FROM employees WHERE employee_id = 100",
    "Aggregated Query": "SELECT Department, COUNT(*) FROM employees GROUP BY Department"
    }