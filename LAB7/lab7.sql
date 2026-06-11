DELETE FROM sales.customers_oakland
WHERE first_name LIKE 'Ka%';

UPDATE sales.customers_oakland
SET first_name = 'Peter'
WHERE first_name = 'Philip';

-- Bước 1: Xóa toàn bộ dữ liệu trong bảng
DELETE FROM sales.customers_oakland;

-- Bước 2: Insert 10 khách hàng mới
INSERT INTO sales.customers_oakland (first_name, last_name, phone, email, street, city, state, zip_code)
VALUES
    ('James',     'Anderson',  '(415) 123-4567', 'james.anderson@gmail.com',   '101 Oak Street',        'Oakland', 'CA', '94601'),
    ('Emily',     'Johnson',   '(415) 234-5678', 'emily.johnson@yahoo.com',    '202 Maple Avenue',      'Oakland', 'CA', '94602'),
    ('Michael',   'Williams',  '(415) 345-6789', 'michael.williams@msn.com',   '303 Pine Road',         'Oakland', 'CA', '94603'),
    ('Sarah',     'Brown',     '(415) 456-7890', 'sarah.brown@hotmail.com',    '404 Cedar Lane',        'Oakland', 'CA', '94604'),
    ('David',     'Jones',     '(415) 567-8901', 'david.jones@gmail.com',      '505 Birch Boulevard',   'Oakland', 'CA', '94605'),
    ('Jessica',   'Garcia',    '(415) 678-9012', 'jessica.garcia@aol.com',     '606 Elm Street',        'Oakland', 'CA', '94606'),
    ('Daniel',    'Martinez',  '(415) 789-0123', 'daniel.martinez@gmail.com',  '707 Walnut Drive',      'Oakland', 'CA', '94607'),
    ('Ashley',    'Davis',     '(415) 890-1234', 'ashley.davis@yahoo.com',     '808 Chestnut Court',    'Oakland', 'CA', '94608'),
    ('Matthew',   'Wilson',    '(415) 901-2345', 'matthew.wilson@msn.com',     '909 Spruce Way',        'Oakland', 'CA', '94609'),
    ('Amanda',    'Taylor',    '(415) 012-3456', 'amanda.taylor@hotmail.com',  '110 Redwood Place',     'Oakland', 'CA', '94610');

-- Bước 3: Kiểm tra kết quả
SELECT * FROM sales.customers_oakland;