--Tìm tất cả các khách hàng mà đã đặt nhiều hơn hoặc bằng hai đơn hàng trong năm 2018.
-- Tìm tất cả khách hàng đã đặt >= 2 đơn hàng trong năm 2018
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS SoDonHang
FROM sales.customers c
JOIN sales.orders o 
    ON c.customer_id = o.customer_id
WHERE YEAR(o.order_date) = 2018
GROUP BY c.customer_id, c.first_name, c.last_name
-- Tìm sản phẩm bán chạy nhất năm 2017.  
SELECT TOP 1
    p.product_name,
    SUM(oi.quantity) AS TongBan
FROM production.products p
JOIN sales.order_items oi 
    ON p.product_id = oi.product_id
JOIN sales.orders o 
    ON oi.order_id = o.order_id
WHERE YEAR(o.order_date) = 2017
GROUP BY p.product_name
ORDER BY TongBan DESC;
--Tìm tên cửa hàng có nhiều đơn đặt hàng nhất năm 2017.
-- Tìm cửa hàng có nhiều đơn đặt hàng nhất năm 2017
SELECT TOP 1
    s.store_name,
    COUNT(o.order_id) AS SoDonHang
FROM sales.stores s
JOIN sales.orders o 
    ON s.store_id = o.store_id
WHERE YEAR(o.order_date) = 2017
GROUP BY s.store_name
ORDER BY SoDonHang DESC;
