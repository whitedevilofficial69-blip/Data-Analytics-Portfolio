-- 1. Create Tables
CREATE TABLE Customers (CustomerID INT, Name VARCHAR(50));
CREATE TABLE Orders (OrderID INT, CustomerID INT, Amount DECIMAL(10,2));

-- 2. Insert Dummy Data
INSERT INTO Customers VALUES (1, 'Ravi'), (2, 'Sneha'), (3, 'Vikram');
INSERT INTO Orders VALUES (101, 1, 5000.00), (102, 1, 2500.00), (103, 2, 8000.00);

-- 3. Advanced Query: Find Total Spent by Each Customer (Using JOIN & GROUP BY)
SELECT 
    c.Name AS CustomerName, 
    SUM(o.Amount) AS TotalSpent,
    COUNT(o.OrderID) AS NumberOfOrders
FROM 
    Customers c
JOIN 
    Orders o ON c.CustomerID = o.CustomerID
GROUP BY 
    c.Name
ORDER BY 
    TotalSpent DESC;
