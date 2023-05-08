CREATE TABLE
    IF NOT EXISTS IS601_Products(
        id int AUTO_INCREMENT PRIMARY KEY,
        name varchar(30) UNIQUE,
        -- alternatively you'd have a SKU that's unique
        description text,
        category VARCHAR(30),
        stock int DEFAULT 0,
        -- my cost is int because I don't have regular currency; shop people may want to record it as pennies
        image text,
        -- this col type can't have a default value; this isn't required for any project, I chose to add it for mine
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        unit_price int DEFAULT 99999,
        visibility BOOLEAN,
        check (stock >= 0),
        -- don't allow negative stock; I don't allow backorders
        check (unit_price >= 0) -- don't allow negative costs
    )