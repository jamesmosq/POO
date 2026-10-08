-- =============================================================================
-- NORTHWIND TRADERS - BASE DE DATOS MEJORADA (MySQL)
-- Basada en: https://en.wikiversity.org/wiki/Database_Examples/Northwind/MySQL
-- Mejoras aplicadas sobre la versión simplificada de Wikiversity
-- =============================================================================

CREATE DATABASE IF NOT EXISTS NorthwindMejorado
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE NorthwindMejorado;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS OrderDetails;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Shippers;
DROP TABLE IF EXISTS Suppliers;

SET FOREIGN_KEY_CHECKS = 1;

-- =============================================================================
-- TABLA: Categories
-- Sin cambios estructurales — estaba correcta en la versión original
-- =============================================================================
CREATE TABLE Categories (
  CategoryID   INTEGER      NOT NULL AUTO_INCREMENT,
  CategoryName VARCHAR(25)  NOT NULL,
  Description  VARCHAR(255) NULL,
  PRIMARY KEY (CategoryID)
) ENGINE=InnoDB;

-- =============================================================================
-- TABLA: Suppliers
-- MEJORA: Se agrega columna Fax (existía en el original de MS Access)
-- =============================================================================
CREATE TABLE Suppliers (
  SupplierID   INTEGER     NOT NULL AUTO_INCREMENT,
  SupplierName VARCHAR(50) NOT NULL,
  ContactName  VARCHAR(50) NULL,
  Address      VARCHAR(50) NULL,
  City         VARCHAR(20) NULL,
  PostalCode   VARCHAR(10) NULL,
  Country      VARCHAR(15) NULL,
  Phone        VARCHAR(15) NULL,
  Fax          VARCHAR(15) NULL,   -- ← NUEVO: fax del proveedor (original MS Access lo tenía)
  PRIMARY KEY (SupplierID)
) ENGINE=InnoDB;

-- =============================================================================
-- TABLA: Shippers
-- Sin cambios — estaba correcta
-- =============================================================================
CREATE TABLE Shippers (
  ShipperID   INTEGER     NOT NULL AUTO_INCREMENT,
  ShipperName VARCHAR(25) NOT NULL,
  Phone       VARCHAR(15) NULL,
  PRIMARY KEY (ShipperID)
) ENGINE=InnoDB;

-- =============================================================================
-- TABLA: Employees
-- MEJORAS:
--   Title          → cargo del empleado (ej: "Sales Representative")
--   HireDate       → fecha de contratación (permite analizar antigüedad)
--   Address/City/Region/PostalCode/Country/HomePhone → datos de contacto completos
--   ReportsTo      → FK hacia EmployeeID del supervisor (jerarquía organizacional)
--   Notes ya existía, se mantiene
-- =============================================================================
CREATE TABLE Employees (
  EmployeeID  INTEGER       NOT NULL AUTO_INCREMENT,
  LastName    VARCHAR(20)   NOT NULL,
  FirstName   VARCHAR(20)   NOT NULL,
  Title       VARCHAR(30)   NULL,           -- ← NUEVO
  BirthDate   DATE          NULL,           -- Cambiado DATETIME → DATE (solo fecha)
  HireDate    DATE          NULL,           -- ← NUEVO
  Address     VARCHAR(60)   NULL,           -- ← NUEVO
  City        VARCHAR(15)   NULL,           -- ← NUEVO
  Region      VARCHAR(15)   NULL,           -- ← NUEVO
  PostalCode  VARCHAR(10)   NULL,           -- ← NUEVO
  Country     VARCHAR(15)   NULL,           -- ← NUEVO
  HomePhone   VARCHAR(24)   NULL,           -- ← NUEVO
  Photo       VARCHAR(25)   NULL,
  Notes       VARCHAR(1024) NULL,
  ReportsTo   INTEGER       NULL,           -- ← NUEVO: FK al jefe directo
  PRIMARY KEY (EmployeeID),
  CONSTRAINT FK_Employees_ReportsTo
    FOREIGN KEY (ReportsTo) REFERENCES Employees (EmployeeID)
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =============================================================================
-- TABLA: Customers
-- MEJORAS:
--   Region → algunos clientes tienen estado/región (EE.UU., Canadá)
--   Phone  → teléfono del contacto
--   Fax    → fax del cliente
-- =============================================================================
CREATE TABLE Customers (
  CustomerID   INTEGER     NOT NULL AUTO_INCREMENT,
  CustomerName VARCHAR(50) NOT NULL,
  ContactName  VARCHAR(50) NULL,
  Address      VARCHAR(50) NULL,
  City         VARCHAR(20) NULL,
  Region       VARCHAR(15) NULL,            -- ← NUEVO: estado/provincia
  PostalCode   VARCHAR(10) NULL,
  Country      VARCHAR(15) NULL,
  Phone        VARCHAR(24) NULL,            -- ← NUEVO
  Fax          VARCHAR(24) NULL,            -- ← NUEVO
  PRIMARY KEY (CustomerID)
) ENGINE=InnoDB;

-- =============================================================================
-- TABLA: Products
-- MEJORAS:
--   Unit → renombrado a QuantityPerUnit (nombre original MS Access)
--   Price → renombrado a UnitPrice (nombre original y estándar)
--   UnitsInStock   → inventario actual (CLAVE para análisis de stock)
--   UnitsOnOrder   → unidades en pedido a proveedor
--   ReorderLevel   → nivel mínimo antes de reabastecer
--   Discontinued   → indica si el producto está descontinuado (TINYINT 0/1)
-- =============================================================================
CREATE TABLE Products (
  ProductID       INTEGER      NOT NULL AUTO_INCREMENT,
  ProductName     VARCHAR(50)  NOT NULL,
  SupplierID      INTEGER      NULL,
  CategoryID      INTEGER      NULL,
  QuantityPerUnit VARCHAR(25)  NULL,         -- renombrado desde Unit
  UnitPrice       DECIMAL(10,2) NOT NULL DEFAULT 0.00,  -- renombrado desde Price
  UnitsInStock    SMALLINT     NOT NULL DEFAULT 0,      -- ← NUEVO
  UnitsOnOrder    SMALLINT     NOT NULL DEFAULT 0,      -- ← NUEVO
  ReorderLevel    SMALLINT     NOT NULL DEFAULT 0,      -- ← NUEVO
  Discontinued    TINYINT(1)   NOT NULL DEFAULT 0,      -- ← NUEVO (0=activo, 1=descontinuado)
  PRIMARY KEY (ProductID),
  CONSTRAINT FK_Products_Categories
    FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
    ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT FK_Products_Suppliers
    FOREIGN KEY (SupplierID) REFERENCES Suppliers (SupplierID)
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =============================================================================
-- TABLA: Orders
-- MEJORAS:
--   RequiredDate    → fecha comprometida de entrega
--   ShippedDate     → fecha real de despacho (permite calcular retrasos)
--   Freight         → costo del flete (DECIMAL)
--   ShipName/Address/City/Region/PostalCode/ShipCountry → destino real del envío
--                     (puede diferir de la dirección del cliente)
--   ShipperID renombrado a ShipVia (nombre original estándar)
-- =============================================================================
CREATE TABLE Orders (
  OrderID        INTEGER        NOT NULL AUTO_INCREMENT,
  CustomerID     INTEGER        NULL,
  EmployeeID     INTEGER        NULL,
  OrderDate      DATE           NOT NULL,
  RequiredDate   DATE           NULL,        -- ← NUEVO
  ShippedDate    DATE           NULL,        -- ← NUEVO (puede ser NULL si aún no se envió)
  ShipVia        INTEGER        NULL,        -- renombrado desde ShipperID
  Freight        DECIMAL(10,2)  NOT NULL DEFAULT 0.00,  -- ← NUEVO
  ShipName       VARCHAR(40)    NULL,        -- ← NUEVO (nombre del destinatario)
  ShipAddress    VARCHAR(60)    NULL,        -- ← NUEVO
  ShipCity       VARCHAR(15)    NULL,        -- ← NUEVO
  ShipRegion     VARCHAR(15)    NULL,        -- ← NUEVO
  ShipPostalCode VARCHAR(10)    NULL,        -- ← NUEVO
  ShipCountry    VARCHAR(15)    NULL,        -- ← NUEVO
  PRIMARY KEY (OrderID),
  CONSTRAINT FK_Orders_Customers
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
    ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT FK_Orders_Employees
    FOREIGN KEY (EmployeeID) REFERENCES Employees (EmployeeID)
    ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT FK_Orders_Shippers
    FOREIGN KEY (ShipVia) REFERENCES Shippers (ShipperID)
    ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =============================================================================
-- TABLA: OrderDetails
-- MEJORAS:
--   Se ELIMINA OrderDetailID como PK autoincremental (no existía en el original)
--   PK compuesta (OrderID, ProductID) — correcto según el diseño de MS Access
--   UnitPrice  → precio AL MOMENTO de la venta (puede diferir del precio actual del producto)
--   Discount   → descuento aplicado a esta línea (0.00 a 1.00, ej: 0.05 = 5%)
-- Esta es la corrección de normalización más importante:
-- El precio histórico de venta se guarda en la línea del pedido, no solo en Products
-- =============================================================================
CREATE TABLE OrderDetails (
  OrderID    INTEGER        NOT NULL,
  ProductID  INTEGER        NOT NULL,
  UnitPrice  DECIMAL(10,2)  NOT NULL DEFAULT 0.00,   -- ← NUEVO: precio histórico
  Quantity   SMALLINT       NOT NULL DEFAULT 1,
  Discount   FLOAT          NOT NULL DEFAULT 0,      -- ← NUEVO: descuento (0 a 1)
  PRIMARY KEY (OrderID, ProductID),                  -- PK compuesta — sin autoincrement
  CONSTRAINT FK_OrderDetails_Orders
    FOREIGN KEY (OrderID) REFERENCES Orders (OrderID)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT FK_OrderDetails_Products
    FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT CK_OrderDetails_Discount
    CHECK (Discount >= 0 AND Discount <= 1),
  CONSTRAINT CK_OrderDetails_Quantity
    CHECK (Quantity > 0)
) ENGINE=InnoDB;

-- =============================================================================
-- ÍNDICES para mejorar rendimiento en consultas frecuentes
-- =============================================================================
CREATE INDEX IX_Orders_CustomerID   ON Orders (CustomerID);
CREATE INDEX IX_Orders_EmployeeID   ON Orders (EmployeeID);
CREATE INDEX IX_Orders_OrderDate    ON Orders (OrderDate);
CREATE INDEX IX_Orders_ShippedDate  ON Orders (ShippedDate);
CREATE INDEX IX_Products_CategoryID ON Products (CategoryID);
CREATE INDEX IX_Products_SupplierID ON Products (SupplierID);
CREATE INDEX IX_OrderDetails_ProductID ON OrderDetails (ProductID);

-- =============================================================================
-- VISTA: v_OrderSummary — Revenue real por pedido con descuento
-- =============================================================================
CREATE OR REPLACE VIEW v_OrderSummary AS
SELECT
  o.OrderID,
  o.OrderDate,
  o.ShippedDate,
  o.RequiredDate,
  DATEDIFF(o.ShippedDate, o.OrderDate)     AS DaysToShip,
  DATEDIFF(o.RequiredDate, o.ShippedDate)  AS DaysEarlyOrLate,
  CASE
    WHEN o.ShippedDate IS NULL            THEN 'Pendiente'
    WHEN o.ShippedDate > o.RequiredDate   THEN 'Tarde'
    ELSE 'A tiempo'
  END                                      AS ShipStatus,
  o.Freight,
  c.CustomerName,
  c.Country                                AS CustomerCountry,
  CONCAT(e.FirstName, ' ', e.LastName)    AS EmployeeName,
  s.ShipperName,
  o.ShipCity,
  o.ShipCountry,
  COUNT(od.ProductID)                      AS TotalLineItems,
  SUM(od.Quantity)                         AS TotalUnits,
  SUM(od.UnitPrice * od.Quantity)          AS GrossAmount,
  SUM(od.UnitPrice * od.Quantity * od.Discount) AS TotalDiscount,
  SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS NetRevenue
FROM Orders o
LEFT JOIN Customers  c  ON o.CustomerID = c.CustomerID
LEFT JOIN Employees  e  ON o.EmployeeID = e.EmployeeID
LEFT JOIN Shippers   s  ON o.ShipVia    = s.ShipperID
LEFT JOIN OrderDetails od ON o.OrderID  = od.OrderID
GROUP BY
  o.OrderID, o.OrderDate, o.ShippedDate, o.RequiredDate,
  o.Freight, c.CustomerName, c.Country,
  e.FirstName, e.LastName, s.ShipperName,
  o.ShipCity, o.ShipCountry;

-- =============================================================================
-- VISTA: v_ProductInventory — Estado actual de inventario
-- =============================================================================
CREATE OR REPLACE VIEW v_ProductInventory AS
SELECT
  p.ProductID,
  p.ProductName,
  c.CategoryName,
  s.SupplierName,
  p.QuantityPerUnit,
  p.UnitPrice,
  p.UnitsInStock,
  p.UnitsOnOrder,
  p.ReorderLevel,
  p.Discontinued,
  CASE
    WHEN p.Discontinued = 1             THEN 'Descontinuado'
    WHEN p.UnitsInStock = 0             THEN 'Sin Stock'
    WHEN (p.UnitsInStock + p.UnitsOnOrder) <= p.ReorderLevel THEN 'Reabastecer Ya'
    WHEN p.UnitsInStock <= p.ReorderLevel THEN 'Stock Bajo'
    ELSE 'OK'
  END AS InventoryStatus
FROM Products p
LEFT JOIN Categories c ON p.CategoryID = c.CategoryID
LEFT JOIN Suppliers  s ON p.SupplierID = s.SupplierID;

-- =============================================================================
-- VISTA: v_EmployeePerformance — Desempeño por empleado
-- =============================================================================
CREATE OR REPLACE VIEW v_EmployeePerformance AS
SELECT
  e.EmployeeID,
  CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
  e.Title,
  CONCAT(m.FirstName, ' ', m.LastName) AS ManagerName,
  COUNT(DISTINCT o.OrderID)            AS TotalOrders,
  COUNT(DISTINCT o.CustomerID)         AS UniqueCustomers,
  SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS TotalRevenue,
  AVG(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS AvgOrderRevenue,
  AVG(DATEDIFF(o.ShippedDate, o.OrderDate)) AS AvgDaysToShip
FROM Employees e
LEFT JOIN Employees m  ON e.ReportsTo   = m.EmployeeID
LEFT JOIN Orders    o  ON e.EmployeeID  = o.EmployeeID
LEFT JOIN OrderDetails od ON o.OrderID = od.OrderID
GROUP BY e.EmployeeID, e.FirstName, e.LastName, e.Title, m.FirstName, m.LastName;

-- =============================================================================
-- DATOS: Categories
-- =============================================================================
INSERT INTO Categories (CategoryID, CategoryName, Description) VALUES
(1, 'Beverages',    'Soft drinks, coffees, teas, beers, and ales'),
(2, 'Condiments',   'Sweet and savory sauces, relishes, spreads, and seasonings'),
(3, 'Confections',  'Desserts, candies, and sweet breads'),
(4, 'Dairy Products', 'Cheeses'),
(5, 'Grains/Cereals', 'Breads, crackers, pasta, and cereal'),
(6, 'Meat/Poultry', 'Prepared meats'),
(7, 'Produce',      'Dried fruit and bean curd'),
(8, 'Seafood',      'Seaweed and fish');

-- =============================================================================
-- DATOS: Shippers
-- =============================================================================
INSERT INTO Shippers (ShipperID, ShipperName, Phone) VALUES
(1, 'Speedy Express', '(503) 555-9831'),
(2, 'United Package', '(503) 555-3199'),
(3, 'Federal Shipping', '(503) 555-9931');

-- =============================================================================
-- DATOS: Suppliers (29 proveedores, con Fax donde aplica)
-- =============================================================================
INSERT INTO Suppliers (SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone, Fax) VALUES
(1,  'Exotic Liquid',                    'Charlotte Cooper',  '49 Gilbert St.',          'London',         'EC1 4SD',  'UK',           '(171) 555-2222', NULL),
(2,  'New Orleans Cajun Delights',        'Shelley Burke',     'P.O. Box 78934',          'New Orleans',    '70117',    'USA',          '(100) 555-4822', NULL),
(3,  'Grandma Kelly\'s Homestead',        'Regina Murphy',     '707 Oxford Rd.',          'Ann Arbor',      '48104',    'USA',          '(313) 555-5735', '(313) 555-3349'),
(4,  'Tokyo Traders',                    'Yoshi Nagase',      '9-8 Sekimai',             'Tokyo',          '100',      'Japan',        '(03) 3555-5011', NULL),
(5,  'Cooperativa de Quesos Las Cabras', 'Antonio del Valle', 'Calle del Rosal 4',       'Oviedo',         '33007',    'Spain',        '(98) 598 76 54', NULL),
(6,  'Mayumi\'s',                        'Mayumi Ohno',       '92 Setsuko Chuo-ku',      'Osaka',          '545',      'Japan',        '06-431-7877',    NULL),
(7,  'Pavlova, Ltd.',                    'Ian Devling',       '74 Rose St. Moonie Ponds','Melbourne',      '3058',     'Australia',    '(03) 444-2343',  '(03) 444-6588'),
(8,  'Specialty Biscuits, Ltd.',         'Peter Wilson',      '29 King\'s Way',          'Manchester',     'M14 GSD',  'UK',           '(161) 555-4448', NULL),
(9,  'PB Knäckebröd AB',                 'Lars Peterson',     'Kaloadagatan 13',         'Gothenburg',     'S-345 67', 'Sweden',       '031-987 65 43',  '031-987 65 91'),
(10, 'Refrescos Americanas LTDA',        'Carlos Diaz',       'Av. das Americanas 12.890','Sao Paulo',     '5442',     'Brazil',       '(11) 555 4640',  NULL),
(11, 'Heli Süßwaren GmbH & Co. KG',      'Petra Winkler',     'Tiergartenstraße 5',      'Berlin',         '10785',    'Germany',      '(010) 9984510',  NULL),
(12, 'Plutzer Lebensmittelgroßmärkte AG','Martin Bein',       'Bogenallee 51',           'Frankfurt',      '60439',    'Germany',      '(069) 992755',   '(069) 992761'),
(13, 'Nord-Ost-Fisch Handelsgesellschaft mbH','Sven Petersen','Frahmredder 112a',        'Cuxhaven',       '27478',    'Germany',      '(04721) 8713',   '(04721) 8714'),
(14, 'Formaggi Fortini s.r.l.',          'Elio Rossi',        'Viale Dante, 75',         'Ravenna',        '48100',    'Italy',        '(0544) 60323',   '(0544) 60603'),
(15, 'Norske Meierier',                  'Beate Vileid',      'Hatlevegen 5',            'Sandvika',       '1320',     'Norway',       '(0)2-953010',    NULL),
(16, 'Bigfoot Breweries',                'Cheryl Saylor',     '3400 - 8th Avenue Suite 210','Bend',        '97101',    'USA',          '(503) 555-9931', NULL),
(17, 'Svensk Sjöföda AB',               'Michael Björn',     'Brovallavägen 231',       'Stockholm',      'S-123 45', 'Sweden',       '08-123 45 67',   NULL),
(18, 'Aux joyeux ecclésiastiques',       'Guylène Nodier',    '203, Rue des Francs-Bourgeois','Paris',     '75004',    'France',       '(1) 03.83.00.68','(1) 03.83.00.62'),
(19, 'New England Seafood Cannery',      'Robb Merchant',     'Order Processing Dept. 2100 Paul Revere Blvd.','Boston','02134','USA', '(617) 555-3267', '(617) 555-3389'),
(20, 'Leka Trading',                     'Chandra Leka',      '471 Serangoon Loop, Suite #402','Singapore', '0512',    'Singapore',    '555-8787',       NULL),
(21, 'Zaanse Snoepfabriek',             'Dirk Luchte',       'Verkoop Rijnweg 22',       'Zaandam',       '9999 ZZ',  'Netherlands',  '(12345) 1212',   '(12345) 1210'),
(22, 'Karkki Oy',                        'Anne Heikkonen',    'Valtakatu 12',            'Lappeenranta',   '53120',    'Finland',      '(953) 10956',    NULL),
(23, 'G\'day, Mate',                     'Wendy Mackenzie',   '170 Prince Edward Parade Hunter\'s Hill','Sydney','2042','Australia',   '(02) 555-5914',  '(02) 555-4873'),
(24, 'Ma Maison',                        'Jean-Guy Lauzon',   '2960 Rue St. Laurent',    'Montréal',       'H1J 1C3',  'Canada',       '(514) 555-9022', '(514) 555-5587'),
(25, 'Pasta Buttini s.r.l.',             'Giovanni Giudici',  'Via dei Gelsomini, 153',  'Salerno',        '84100',    'Italy',        '(089) 6547665',  '(089) 6547667'),
(26, 'Escargots Nouveaux',               'Marie Delamare',    '22, rue H. Voiron',       'Montceau',       '71300',    'France',       '85.57.00.07',    NULL),
(27, 'Gai pâturage',                     'Eliane Noz',        'Bat. B 3, rue des Alpes', 'Annecy',         '74000',    'France',       '38.76.98.06',    '38.76.98.58'),
(28, 'Forêts d\'érables',               'Chantal Goulet',    '148 rue Chasseur',        'Ste-Hyacinthe',  'J2S 7S8',  'Canada',       '(514) 555-2955', '(514) 555-2921'),
(29, 'Baltica A/S',                      'Marianne Mikkelsen','Adelgade 12',             'Copenhagen',     '1450',     'Denmark',      '70 12 34 56',    NULL);

-- =============================================================================
-- DATOS: Employees (9 empleados con campos completos)
-- =============================================================================
INSERT INTO Employees (EmployeeID, LastName, FirstName, Title, BirthDate, HireDate, Address, City, Region, PostalCode, Country, HomePhone, Photo, Notes, ReportsTo) VALUES
(1, 'Davolio',   'Nancy',   'Sales Representative',       '1968-12-08', '1992-05-01', '507 - 20th Ave. E. Apt. 2A', 'Seattle',   'WA', '98122', 'USA', '(206) 555-9857', 'EmpID1.pic', 'Education includes a BA in psychology from Colorado State University. She also completed The Art of the Cold Call. Nancy is a member of Toastmasters International.', 2),
(2, 'Fuller',    'Andrew',  'Vice President, Sales',      '1952-02-19', '1992-08-14', '908 W. Capital Way',          'Tacoma',    'WA', '98401', 'USA', '(206) 555-9482', 'EmpID2.pic', 'Andrew received his BTS commercial and a Ph.D. in international marketing from the University of Dallas. He is fluent in French and Italian. Andrew is a member of the Sales Management Roundtable.', NULL),
(3, 'Leverling', 'Janet',   'Sales Representative',       '1963-08-30', '1992-04-01', '722 Moss Bay Blvd.',          'Kirkland',  'WA', '98033', 'USA', '(206) 555-3412', 'EmpID3.pic', 'Janet has a BS degree in chemistry from Boston College. She has also completed a certificate program in food retailing management. Janet was hired as a sales associate and was promoted to sales representative.', 2),
(4, 'Peacock',   'Margaret','Sales Representative',       '1958-09-19', '1993-05-03', '4110 Old Redmond Rd.',         'Redmond',   'WA', '98052', 'USA', '(206) 555-8122', 'EmpID4.pic', 'Margaret holds a BA in English literature from Concordia College and an MA from the University of Washington. She was employee of the month six times.', 2),
(5, 'Buchanan',  'Steven',  'Sales Manager',              '1955-03-04', '1993-10-17', '14 Garrett Hill',              'London',    NULL, 'SW1 8JR','UK',  '(71) 555-4848',  'EmpID5.pic', 'Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree. Upon joining the company as a sales representative, he spent 6 months in an orientation program and was promoted to sales manager.', 2),
(6, 'Suyama',    'Michael', 'Sales Representative',       '1963-07-02', '1993-10-17', 'Coventry House Miner Rd.',     'London',    NULL, 'EC2 7JR','UK',  '(71) 555-7773',  'EmpID6.pic', 'Michael is a graduate of Sussex University (MA, economics) and UCLA (MBA, marketing). He is fluent in Japanese and can read and write French, Portuguese, and Spanish.', 5),
(7, 'King',      'Robert',  'Sales Representative',       '1960-05-29', '1994-01-02', 'Edgeham Hollow Winchester Way','London',    NULL, 'RG1 9SP','UK',  '(71) 555-5598',  'EmpID7.pic', 'Robert King served in the Peace Corps and traveled extensively before completing his degree in English at the University of Michigan.', 5),
(8, 'Callahan',  'Laura',   'Inside Sales Coordinator',   '1958-01-09', '1994-03-05', '4726 - 11th Ave. N.E.',        'Seattle',   'WA', '98105', 'USA', '(206) 555-1189', 'EmpID8.pic', 'Laura received a BA in psychology from the University of Washington. She has also completed a course in business French. She reads and writes French.', 2),
(9, 'Dodsworth', 'Anne',    'Sales Representative',       '1969-07-02', '1994-11-15', '7 Houndstooth Rd.',            'London',    NULL, 'WG2 7LT','UK',  '(71) 555-4444',  'EmpID9.pic', 'Anne has a BA degree in English from St. Lawrence College. She is fluent in French and German.', 5);

-- =============================================================================
-- DATOS: Customers (91 clientes con Region, Phone y Fax)
-- =============================================================================
INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, Region, PostalCode, Country, Phone, Fax) VALUES
(1,  'Alfreds Futterkiste',               'Maria Anders',         'Obere Str. 57',                      'Berlin',          NULL,  '12209',    'Germany',      '030-0074321',     '030-0076545'),
(2,  'Ana Trujillo Emparedados y helados','Ana Trujillo',         'Avda. de la Constitución 2222',       'México D.F.',     NULL,  '05021',    'Mexico',       '(5) 555-4729',    '(5) 555-3745'),
(3,  'Antonio Moreno Taquería',           'Antonio Moreno',       'Mataderos  2312',                    'México D.F.',     NULL,  '05023',    'Mexico',       '(5) 555-3932',    NULL),
(4,  'Around the Horn',                   'Thomas Hardy',         '120 Hanover Sq.',                    'London',          NULL,  'WA1 1DP',  'UK',           '(171) 555-7788',  '(171) 555-6750'),
(5,  'Berglunds snabbköp',               'Christina Berglund',   'Berguvsvägen  8',                    'Luleå',           NULL,  'S-958 22', 'Sweden',       '0921-12 34 65',   '0921-12 34 67'),
(6,  'Blauer See Delikatessen',           'Hanna Moos',           'Forsterstr. 57',                     'Mannheim',        NULL,  '68306',    'Germany',      '0621-08460',      '0621-08924'),
(7,  'Blondesddsl père et fils',         'Frédérique Citeaux',  '24, place Kléber',                   'Strasbourg',      NULL,  '67000',    'France',       '88.60.15.31',     '88.60.15.32'),
(8,  'Bólido Comidas preparadas',        'Martín Sommer',        'C/ Araquil, 67',                     'Madrid',          NULL,  '28023',    'Spain',        '(91) 555 22 82',  '(91) 555 91 99'),
(9,  'Bon app',                           'Laurence Lebihan',     '12, rue des Bouchers',               'Marseille',       NULL,  '13008',    'France',       '91.24.45.40',     '91.24.45.41'),
(10, 'Bottom-Dollar Marketss',            'Elizabeth Lincoln',    '23 Tsawassen Blvd.',                 'Tsawassen',       'BC',  'T2F 8M4',  'Canada',       '(604) 555-4729',  '(604) 555-3745'),
(11, 'B\'s Beverages',                   'Victoria Ashworth',    'Fauntleroy Circus',                  'London',          NULL,  'EC2 5NT',  'UK',           '(171) 555-1212',  NULL),
(12, 'Cactus Comidas para llevar',        'Patricio Simpson',     'Cerrito 333',                        'Buenos Aires',    NULL,  '1010',     'Argentina',    '(1) 135-5555',    '(1) 135-4892'),
(13, 'Centro comercial Moctezuma',        'Francisco Chang',      'Sierras de Granada 9993',            'México D.F.',     NULL,  '05022',    'Mexico',       '(5) 555-3392',    '(5) 555-7293'),
(14, 'Chop-suey Chinese',                 'Yang Wang',            'Hauptstr. 29',                       'Bern',            NULL,  '3012',     'Switzerland',  '0452-076545',     NULL),
(15, 'Comércio Mineiro',                 'Pedro Afonso',         'Av. dos Lusíadas, 23',               'Sao Paulo',       'SP',  '05432-043','Brazil',       '(11) 555-7647',   NULL),
(16, 'Consolidated Holdings',             'Elizabeth Brown',      'Berkeley Gardens 12 Brewery ',       'London',          NULL,  'WX1 6LT',  'UK',           '(171) 555-2282',  '(171) 555-9199'),
(17, 'Drachenblut Delikatessenn',         'Sven Ottlieb',         'Walserweg 21',                       'Aachen',          NULL,  '52066',    'Germany',      '0241-039123',     '0241-059428'),
(18, 'Du monde entier',                   'Janine Labrune',       '67, rue des Cinquante Otages',       'Nantes',          NULL,  '44000',    'France',       '40.67.88.88',     '40.67.89.89'),
(19, 'Eastern Connection',                'Ann Devon',            '35 King George',                     'London',          NULL,  'WX3 6FW',  'UK',           '(171) 555-0297',  '(171) 555-3373'),
(20, 'Ernst Handel',                      'Roland Mendel',        'Kirchgasse 6',                       'Graz',            NULL,  '8010',     'Austria',      '7675-3425',       '7675-3426'),
(21, 'Familia Arquibaldo',                'Aria Cruz',            'Rua Orós, 92',                       'Sao Paulo',       'SP',  '05442-030','Brazil',       '(11) 555-9857',   NULL),
(22, 'FISSA Fabrica Inter. Salchichas S.A.','Diego Roel',         'C/ Moralzarzal, 86',                 'Madrid',          NULL,  '28034',    'Spain',        '(91) 555 94 44',  '(91) 555 55 93'),
(23, 'Folies gourmandes',                 'Martine Rancé',       '184, chaussée de Tournai',           'Lille',           NULL,  '59000',    'France',       '20.16.10.16',     '20.16.10.17'),
(24, 'Folk och fä HB',                    'Maria Larsson',        'Åkergatan 24',                      'Bräcke',          NULL,  'S-844 67', 'Sweden',       '0695-34 67 21',   NULL),
(25, 'Frankenversand',                    'Peter Franken',        'Berliner Platz 43',                  'München',         NULL,  '80805',    'Germany',      '089-0877310',     '089-0877451'),
(26, 'France restauration',               'Carine Schmitt',       '54, rue Royale',                     'Nantes',          NULL,  '44000',    'France',       '40.32.21.21',     '40.32.21.20'),
(27, 'Franchi S.p.A.',                   'Paolo Accorti',        'Via Monte Bianco 34',                'Torino',          NULL,  '10100',    'Italy',        '011-4988260',     '011-4988261'),
(28, 'Furia Bacalhau e Frutos do Mar',    'Lino Rodriguez',       'Jardim das rosas n. 32',             'Lisboa',          NULL,  '1675',     'Portugal',     '(1) 354-2534',    '(1) 354-2535'),
(29, 'Galería del gastrónomo',           'Eduardo Saavedra',     'Rambla de Cataluña, 23',             'Barcelona',       NULL,  '8022',     'Spain',        '(93) 203 4560',   '(93) 203 4561'),
(30, 'Godos Cocina Típica',             'José Pedro Freyre',    'C/ Romero, 33',                      'Sevilla',         NULL,  '41101',    'Spain',        '(95) 555 82 82',  NULL),
(31, 'Gourmet Lanchonetes',              'André Fonseca',        'Av. Brasil, 442',                    'Campinas',        'SP',  '04876-786','Brazil',       '(11) 555-9482',   NULL),
(32, 'Great Lakes Food Market',           'Howard Snyder',        '2732 Baker Blvd.',                   'Eugene',          'OR',  '97403',    'USA',          '(503) 555-7555',  NULL),
(33, 'GROSELLA-Restaurante',             'Manuel Pereira',       '5ª Ave. Los Palos Grandes',          'Caracas',         'DF',  '1081',     'Venezuela',    '(2) 283-2951',    '(2) 283-3397'),
(34, 'Hanari Carnes',                    'Mario Pontes',         'Rua do Paço, 67',                    'Rio de Janeiro',  'RJ',  '05454-876','Brazil',       '(21) 555-0091',   '(21) 555-8765'),
(35, 'HILARION-Abastos',                 'Carlos Hernández',    'Carrera 22 con Ave. Carlos Soublette #8-35','San Cristóbal','Táchira','5022','Venezuela', '(5) 555-1340',    '(5) 555-1948'),
(36, 'Hungry Coyote Import Store',        'Yoshi Latimer',        'City Center Plaza 516 Main St.',     'Elgin',           'OR',  '97827',    'USA',          '(503) 555-6874',  '(503) 555-2376'),
(37, 'Hungry Owl All-Night Grocers',      'Patricia McKenna',     '8 Johnstown Road',                   'Cork',            NULL,  NULL,       'Ireland',      '2967 542',        '2967 3333'),
(38, 'Island Trading',                    'Helen Bennett',        'Garden House Crowther Way',          'Cowes',           NULL,  'PO31 7PJ', 'UK',           '(198) 555-8888',  NULL),
(39, 'Königlich Essen',                  'Philip Cramer',        'Maubelstr. 90',                      'Brandenburg',     NULL,  '14776',    'Germany',      '0555-09876',      NULL),
(40, 'La corne d\'abondance',            'Daniel Tonini',        '67, avenue de l\'Europe',            'Versailles',      NULL,  '78000',    'France',       '30.59.84.10',     '30.59.85.11'),
(41, 'La maison d\'Asie',               'Annette Roulet',       '1 rue Alsace-Lorraine',              'Toulouse',        NULL,  '31000',    'France',       '61.77.61.10',     '61.77.61.11'),
(42, 'Laughing Bacchus Wine Cellars',     'Yoshi Tannamuri',      '1900 Oak St.',                       'Vancouver',       'BC',  'V3F 2K1',  'Canada',       '(604) 555-3392',  '(604) 555-7293'),
(43, 'Lazy K Kountry Store',              'John Steel',           '12 Orchestra Terrace',               'Walla Walla',     'WA',  '99362',    'USA',          '(509) 555-7969',  '(509) 555-6221'),
(44, 'Lehmanns Marktstand',              'Renate Messner',       'Magazinweg 7',                       'Frankfurt a.M.', NULL,  '60528',    'Germany',      '069-0245984',     '069-0245874'),
(45, 'Let\'s Stop N Shop',               'Jaime Yorres',         '87 Polk St. Suite 5',                'San Francisco',   'CA',  '94117',    'USA',          '(415) 555-5938',  NULL),
(46, 'LILA-Supermercado',                'Carlos González',      'Carrera 52 con Ave. Bolívar #65-98 Llano Largo','Barquisimeto','Lara','3508','Venezuela','(9) 331-6954','(9) 331-7256'),
(47, 'LINO-Delicateses',                 'Felipe Izquierdo',     'Ave. 5 de Mayo Porlamar',            'I. de Margarita', 'Nueva Esparta','4980','Venezuela','(8) 34-56-12','(8) 34-93-93'),
(48, 'Lonesome Pine Restaurant',          'Fran Wilson',          '89 Chiaroscuro Rd.',                 'Portland',        'OR',  '97219',    'USA',          '(503) 555-9573',  '(503) 555-9646'),
(49, 'Magazzini Alimentari Riuniti',      'Giovanni Rovelli',     'Via Ludovico il Moro 22',            'Bergamo',         NULL,  '24100',    'Italy',        '035-640230',      '035-640231'),
(50, 'Maison Dewey',                      'Catherine Dewey',      'Rue Joseph-Bens 532',                'Bruxelles',       NULL,  'B-1180',   'Belgium',      '(02) 201 24 67',  '(02) 201 24 68'),
(51, 'Mère Paillarde',                  'Jean-François Portelance','43 rue St. Laurent',              'Montréal',        'Québec','H1J 1C3','Canada',       '(514) 555-8054',  NULL),
(52, 'Morgenstern Gesundkost',            'Alexander Feuer',      'Heerstr. 22',                        'Leipzig',         NULL,  '04179',    'Germany',      '0342-023176',     NULL),
(53, 'North/South',                       'Simon Crowther',       'South House 300 Queensbridge',       'London',          NULL,  'SW7 1RZ',  'UK',           '(171) 555-7733',  '(171) 555-2444'),
(54, 'Océano Atlántico Ltda.',           'Yvonne Moncada',       'Ing. Gustavo Moncada 8585 Piso 20-A','Buenos Aires',   NULL,  '1010',     'Argentina',    '(1) 135-5333',    '(1) 135-5535'),
(55, 'Old World Delicatessen',            'Rene Phillips',        '2743 Bering St.',                    'Anchorage',       'AK',  '99508',    'USA',          '(907) 555-7584',  '(907) 555-2880'),
(56, 'Ottilies Käseladen',              'Henriette Pfalzheim',  'Mehrheimerstr. 369',                 'Köln',           NULL,  '50739',    'Germany',      '0221-0644327',    '0221-0765721'),
(57, 'Paris spécialités',               'Marie Bertrand',       '265, boulevard Charonne',            'Paris',           NULL,  '75012',    'France',       '(1) 42.34.22.66', '(1) 42.34.22.77'),
(58, 'Pericles Comidas clásicas',        'Guillermo Fernández', 'Calle Dr. Jorge Cash 321',           'México D.F.',     NULL,  '05033',    'Mexico',       '(5) 552-3745',    '(5) 545-3745'),
(59, 'Piccolo und mehr',                  'Georg Pipps',          'Geislweg 14',                        'Salzburg',        NULL,  '5020',     'Austria',      '6562-9722',       '6562-9723'),
(60, 'Princesa Isabel Vinhoss',          'Isabel de Castro',     'Estrada da saúde n. 58',             'Lisboa',          NULL,  '1756',     'Portugal',     '(1) 356-5634',    NULL),
(61, 'Que Delícia',                     'Bernardo Batista',     'Rua da Panificadora, 12',            'Rio de Janeiro',  'RJ',  '02389-673','Brazil',       '(21) 555-4252',   '(21) 555-4545'),
(62, 'Queen Cozinha',                    'Lúcia Carvalho',      'Alameda dos Canàrios, 891',          'Sao Paulo',       'SP',  '05487-020','Brazil',       '(11) 555-1189',   NULL),
(63, 'QUICK-Stop',                        'Horst Kloss',          'Taucherstraße 10',                  'Cunewalde',       NULL,  '01307',    'Germany',      '0372-035188',     NULL),
(64, 'Rancho grande',                    'Sergio Gutiérrez',    'Av. del Libertador 900',             'Buenos Aires',    NULL,  '1010',     'Argentina',    '(1) 123-5555',    '(1) 123-5556'),
(65, 'Rattlesnake Canyon Grocery',        'Paula Wilson',         '2817 Milton Dr.',                    'Albuquerque',     'NM',  '87110',    'USA',          '(505) 555-5939',  '(505) 555-3620'),
(66, 'Reggiani Caseifici',               'Maurizio Moroni',      'Strada Provinciale 124',             'Reggio Emilia',   NULL,  '42100',    'Italy',        '0522-556721',     '0522-556722'),
(67, 'Ricardo Adocicados',               'Janete Limeira',       'Av. Copacabana, 267',               'Rio de Janeiro',  'RJ',  '02389-890','Brazil',       '(21) 555-3412',   NULL),
(68, 'Richter Supermarkt',               'Michael Holz',         'Grenzacherweg 237',                  'Genève',          NULL,  '1203',     'Switzerland',  '0897-034214',     NULL),
(69, 'Romero y tomillo',                 'Alejandra Camino',     'Gran Vía, 1',                        'Madrid',          NULL,  '28001',    'Spain',        '(91) 745 6200',   '(91) 745 6210'),
(70, 'Santé Gourmet',                   'Jonas Bergulfsen',     'Erling Skakkes gate 78',             'Stavern',         NULL,  '4110',     'Norway',       '07-98 92 35',     '07-98 92 47'),
(71, 'Save-a-lot Markets',               'Jose Pavarotti',       '187 Suffolk Ln.',                    'Boise',           'ID',  '83720',    'USA',          '(208) 555-8097',  NULL),
(72, 'Seven Seas Imports',               'Hari Kumar',           '90 Wadhurst Rd.',                    'London',          NULL,  'OX15 4NB', 'UK',           '(171) 555-1717',  '(171) 555-5646'),
(73, 'Simons bistro',                    'Jytte Petersen',       'Vinbæltet 34',                      'Kobenhavn',       NULL,  '1734',     'Denmark',      '31 12 34 56',     '31 13 35 57'),
(74, 'Spécialités du monde',            'Dominique Perrier',    '25, rue Lauriston',                  'Paris',           NULL,  '75016',    'France',       '(1) 47.55.60.10', '(1) 47.55.60.20'),
(75, 'Split Rail Beer & Ale',            'Art Braunschweiger',   'P.O. Box 555',                       'Lander',          'WY',  '82520',    'USA',          '(307) 555-5340',  '(307) 555-6525'),
(76, 'Suprêmes délices',               'Pascale Cartrain',     'Boulevard Tirou, 255',               'Charleroi',       NULL,  'B-6000',   'Belgium',      '(071) 23 67 22 20','(071) 23 67 22 21'),
(77, 'The Big Cheese',                   'Liz Nixon',            '89 Jefferson Way Suite 2',           'Portland',        'OR',  '97201',    'USA',          '(503) 555-3612',  NULL),
(78, 'The Cracker Box',                  'Liu Wong',             '55 Grizzly Peak Rd.',                'Butte',           'MT',  '59801',    'USA',          '(406) 555-5834',  '(406) 555-8083'),
(79, 'Toms Spezialitäten',             'Karin Josephs',        'Luisenstr. 48',                      'Münster',        NULL,  '44087',    'Germany',      '0251-031259',     '0251-035695'),
(80, 'Tortuga Restaurante',              'Miguel Angel Paolino', 'Avda. Azteca 123',                   'México D.F.',     NULL,  '05033',    'Mexico',       '(5) 555-2933',    NULL),
(81, 'Tradição Hipermercados',          'Anabela Domingues',    'Av. Inês de Castro, 414',            'Sao Paulo',       'SP',  '05634-030','Brazil',       '(11) 555-2167',   '(11) 555-2168'),
(82, 'Trail\'s Head Gourmet Provisioners','Helvetius Nagy',     '722 DaVinci Blvd.',                  'Kirkland',        'WA',  '98034',    'USA',          '(206) 555-8257',  '(206) 555-2174'),
(83, 'Vaffeljernet',                     'Palle Ibsen',          'Smagsloget 45',                      'Århus',          NULL,  '8200',     'Denmark',      '86 21 32 43',     '86 22 33 44'),
(84, 'Victuailles en stock',             'Mary Saveley',         '2, rue du Commerce',                 'Lyon',            NULL,  '69004',    'France',       '78.32.54.86',     '78.32.54.87'),
(85, 'Vins et alcools Chevalier',        'Paul Henriot',         '59 rue de l\'Abbaye',               'Reims',           NULL,  '51100',    'France',       '26.47.15.10',     '26.47.15.11'),
(86, 'Die Wandernde Kuh',               'Rita Müller',          'Adenauerallee 900',                  'Stuttgart',       NULL,  '70563',    'Germany',      '0711-020361',     '0711-035428'),
(87, 'Wartian Herkku',                   'Pirkko Koskitalo',     'Torikatu 38',                        'Oulu',            NULL,  '90110',    'Finland',      '981-443655',      '981-443655'),
(88, 'Wellington Importadora',           'Paula Parente',        'Rua do Mercado, 12',                 'Resende',         'SP',  '08737-363','Brazil',       '(14) 555-8122',   NULL),
(89, 'White Clover Markets',             'Karl Jablonski',       '305 - 14th Ave. S. Suite 3B',        'Seattle',         'WA',  '98128',    'USA',          '(206) 555-4112',  '(206) 555-4115'),
(90, 'Wilman Kala',                      'Matti Karttunen',      'Keskuskatu 45',                      'Helsinki',        NULL,  '21240',    'Finland',      '90-224 8858',     '90-224 8858'),
(91, 'Wolski',                            'Zbyszek Piestrzeniewicz','ul. Filtrowa 68',                 'Warszawa',        NULL,  '01-012',   'Poland',       '(26) 642-7012',   '(26) 642-7012');

-- =============================================================================
-- DATOS: Products (77 productos con campos de inventario completos)
-- =============================================================================
INSERT INTO Products (ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued) VALUES
(1,  'Chai',                              1,  1, '10 boxes x 20 bags',     18.00,  39,   0,  10, 0),
(2,  'Chang',                             1,  1, '24 - 12 oz bottles',     19.00,  17,  40,  25, 0),
(3,  'Aniseed Syrup',                     1,  2, '12 - 550 ml bottles',    10.00,  13,  70,  25, 0),
(4,  'Chef Anton\'s Cajun Seasoning',     2,  2, '48 - 6 oz jars',         22.00,  53,   0,   0, 0),
(5,  'Chef Anton\'s Gumbo Mix',           2,  2, '36 boxes',               21.35,   0,   0,   0, 1),
(6,  'Grandma\'s Boysenberry Spread',     3,  2, '12 - 8 oz jars',         25.00, 120,   0,  25, 0),
(7,  'Uncle Bob\'s Organic Dried Pears',  3,  7, '12 - 1 lb pkgs.',        30.00,  15,   0,  10, 0),
(8,  'Northwoods Cranberry Sauce',        3,  2, '12 - 12 oz jars',        40.00,   6,   0,   0, 0),
(9,  'Mishi Kobe Niku',                   4,  6, '18 - 500 g pkgs.',        97.00,  29,   0,   0, 1),
(10, 'Ikura',                             4,  8, '12 - 200 ml jars',        31.00,  31,   0,   0, 0),
(11, 'Queso Cabrales',                    5,  4, '1 kg pkg.',               21.00,  22,  30,  30, 0),
(12, 'Queso Manchego La Pastora',         5,  4, '10 - 500 g pkgs.',        38.00,  86,   0,   0, 0),
(13, 'Konbu',                             6,  8, '2 kg box',                 6.00,  24,   0,   5, 0),
(14, 'Tofu',                              6,  7, '40 - 100 g pkgs.',        23.25,  35,   0,   0, 0),
(15, 'Genen Shouyu',                      6,  2, '24 - 250 ml bottles',     15.50,  39,   0,   5, 0),
(16, 'Pavlova',                           7,  3, '32 - 500 g boxes',        17.45, 29,    0,  10, 0),
(17, 'Alice Mutton',                      7,  6, '20 - 1 kg tins',          39.00,   0,   0,   0, 1),
(18, 'Carnarvon Tigers',                  7,  8, '16 kg pkg.',              62.50,  42,   0,   0, 0),
(19, 'Teatime Chocolate Biscuits',        8,  3, '10 boxes x 12 pieces',     9.20,  25,   0,   5, 0),
(20, 'Sir Rodney\'s Marmalade',           8,  3, '30 gift boxes',           81.00,  40,   0,   0, 0),
(21, 'Sir Rodney\'s Scones',             8,  3, '24 pkgs. x 4 pieces',     10.00,   3,  40,   5, 0),
(22, 'Gustaf\'s Knäckebröd',            9,  5, '24 - 500 g pkgs.',        21.00,  104,  0,  25, 0),
(23, 'Tunnbröd',                         9,  5, '12 - 250 g pkgs.',          9.00,  61,   0,  25, 0),
(24, 'Guaraná Fantástica',             10,  1, '12 - 355 ml cans',          4.50,  20,   0,   0, 1),
(25, 'NuNuCa Nuß-Nougat-Creme',        11,  3, '20 - 450 g glasses',       14.00,  76,   0,  30, 0),
(26, 'Gumbär Gummibärchen',           11,  3, '100 - 250 g bags',         31.23,  15,   0,   0, 0),
(27, 'Schoggi Schokolade',              11,  3, '100 - 100 g pieces',       43.90,  49,   0,  30, 0),
(28, 'Rössle Sauerkraut',              12,  7, '25 - 825 g cans',          45.60,  26,   0,   0, 1),
(29, 'Thüringer Rostbratwurst',        12,  6, '50 bags x 30 sausgs.',    123.79,   0,   0,   0, 1),
(30, 'Nord-Ost Matjeshering',           13,  8, '10 - 200 g glasses',       25.89,  10,   0,  15, 0),
(31, 'Gorgonzola Telino',               14,  4, '12 - 100 g pkgs',          12.50, 0,    70,  20, 0),
(32, 'Mascarpone Fabioli',              14,  4, '24 - 200 g pkgs.',         32.00,   9,  40,  25, 0),
(33, 'Geitost',                         15,  4, '500 g',                     2.50, 112,   0,  20, 0),
(34, 'Sasquatch Ale',                   16,  1, '24 - 12 oz bottles',       14.00,  111,  0,  15, 0),
(35, 'Steeleye Stout',                  16,  1, '24 - 12 oz bottles',       18.00,  20,   0,  15, 0),
(36, 'Inlagd Sill',                     17,  8, '24 - 250 g  jars',         19.00, 112,   0,  20, 0),
(37, 'Gravad lax',                      17,  8, '12 - 500 g pkgs.',         26.00,  11,  50,  25, 0),
(38, 'Côte de Blaye',                   18,  1, '12 - 75 cl bottles',      263.50,  17,   0,  15, 0),
(39, 'Chartreuse verte',               18,  1, '750 cc per bottle',         18.00,  69,   0,   5, 0),
(40, 'Boston Crab Meat',                19,  8, '24 - 4 oz tins',           18.40, 123,   0,  30, 0),
(41, 'Jack\'s New England Clam Chowder',19,  8, '12 - 12 oz cans',          9.65, 85,    0,  10, 0),
(42, 'Singaporean Hokkien Fried Mee',   20,  5, '32 - 1 kg pkgs.',         14.00,  26,   0,   0, 1),
(43, 'Ipoh Coffee',                     20,  1, '16 - 500 g tins',          46.00,  17,  10,  25, 0),
(44, 'Gula Malacca',                    20,  2, '20 - 2 kg bags',           19.45,  27,   0,  15, 0),
(45, 'Røgede sild',                    21,  8, '1k pkg.',                   9.50, 5,    70,  15, 0),
(46, 'Spegesild',                       21,  8, '4 - 450 g glasses',        12.00, 95,    0,   0, 0),
(47, 'Zaanse koeken',                   22,  3, '10 - 4 oz boxes',           9.50, 36,    0,   0, 0),
(48, 'Chocolade',                       22,  3, '10 pkgs.',                 12.75,  15,  70,  25, 0),
(49, 'Maxilaku',                        23,  3, '24 - 50 g pkgs.',          20.00,  10,  60,  15, 0),
(50, 'Valkoinen suklaa',               23,  3, '12 - 100 g bars',          16.25,  65,   0,  30, 0),
(51, 'Manjimup Dried Apples',           24,  7, '50 - 300 g pkgs.',         53.00,  20,   0,  10, 0),
(52, 'Filo Mix',                        24,  5, '16 - 2 kg boxes',          7.00,  38,   0,  25, 0),
(53, 'Perth Pasties',                   24,  6, '48 pieces',                32.80,   0,   0,   0, 1),
(54, 'Tourtière',                      25,  6, '16 pies',                  7.45,  21,   0,  10, 0),
(55, 'Pâté chinois',                  25,  6, '24 boxes x 2 pies',        24.00, 115,   0,  20, 0),
(56, 'Gnocchi di nonna Alice',          26,  5, '24 - 250 g pkgs.',         38.00, 21,   10,  30, 0),
(57, 'Ravioli Angelo',                  26,  5, '24 - 250 g pkgs.',         19.50,  36,   0,  20, 0),
(58, 'Escargots de Bourgogne',         27,  8, '24 pieces',                13.25,  62,   0,  20, 0),
(59, 'Raclette Courdavault',           28,  4, '5 kg pkg.',                55.00,  79,   0,   0, 0),
(60, 'Camembert Pierrot',              28,  4, '15 - 300 g rounds',        34.00,  19,   0,   0, 0),
(61, 'Sirop d\'érable',               29,  2, '24 - 500 ml bottles',      28.50, 113,   0,  25, 0),
(62, 'Tarte au sucre',                 29,  3, '48 pies',                  49.30,  17,  80,  25, 0),
(63, 'Vegie-spread',                    7,  2, '15 - 625 g jars',          43.90,  24,   0,   5, 0),
(64, 'Wimmers gute Semmelknödel',      12,  5, '20 bags x 4 pieces',       33.25,  22,  80,  30, 0),
(65, 'Louisiana Fiery Hot Pepper Sauce', 2, 2, '32 - 8 oz bottles',        21.05,  76,   0,   0, 0),
(66, 'Louisiana Hot Spiced Okra',       2,  2, '24 - 8 oz jars',           17.00,   4, 100,  20, 0),
(67, 'Laughing Lumberjack Lager',      16,  1, '24 - 12 oz bottles',       14.00,  52,   0,  10, 0),
(68, 'Scottish Longbreads',             8,  3, '10 boxes x 8 pieces',      12.50,   6,  10,  15, 0),
(69, 'Gudbrandsdalsost',               15,  4, '10 kg pkg.',               36.00,  26,   0,  15, 0),
(70, 'Outback Lager',                   7,  1, '24 - 355 ml bottles',      15.00,  15,  10,  30, 0),
(71, 'Flotemysost',                    15,  4, '10 - 500 g pkgs.',         21.50,  26,   0,   0, 0),
(72, 'Mozzarella di Giovanni',         14,  4, '24 - 200 g pkgs.',         34.80,  14,   0,   0, 0),
(73, 'Röd Kaviar',                     17,  8, '24 - 150 g jars',          15.00,  101,  0,   5, 0),
(74, 'Longlife Tofu',                   4,  7, '5 kg pkg.',                10.00,   4,  20,   5, 0),
(75, 'Rhönbräu Klosterbier',           12,  1, '24 - 0.5 l bottles',       7.75, 125,   0,  25, 0),
(76, 'Lakkalikööri',                   23,  1, '500 ml',                   18.00,  57,   0,  20, 0),
(77, 'Original Frankfurter grüne Soße',12, 2, '12 boxes',                  13.00,  32,   0,  15, 0);

-- =============================================================================
-- DATOS: Orders (830 pedidos con todos los campos completos)
-- Nota: ShippedDate puede ser NULL para pedidos pendientes
-- RequiredDate = OrderDate + 14 días (estándar Northwind)
-- ShipName/Address/City/Country = datos del cliente (simplificado)
-- =============================================================================
START TRANSACTION;
INSERT INTO Orders (OrderID,CustomerID,EmployeeID,OrderDate,RequiredDate,ShippedDate,ShipVia,Freight,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry) VALUES
(10248,90,5,'1996-07-04','1996-08-01','1996-07-16',3,32.38,'Wilman Kala','Keskuskatu 45','Helsinki',NULL,'21240','Finland'),
(10249,81,6,'1996-07-05','1996-08-16','1996-07-10',1,11.61,'Tradição Hipermercados','Av. Inês de Castro, 414','Sao Paulo','SP','05634-030','Brazil'),
(10250,34,4,'1996-07-08','1996-08-05','1996-07-12',2,65.83,'Hanari Carnes','Rua do Paço, 67','Rio de Janeiro','RJ','05454-876','Brazil'),
(10251,84,3,'1996-07-08','1996-08-05','1996-07-15',1,41.34,'Victuailles en stock','2, rue du Commerce','Lyon',NULL,'69004','France'),
(10252,76,4,'1996-07-09','1996-08-06','1996-07-11',2,51.30,'Suprêmes délices','Boulevard Tirou, 255','Charleroi',NULL,'B-6000','Belgium'),
(10253,34,3,'1996-07-10','1996-07-24','1996-07-16',2,58.17,'Hanari Carnes','Rua do Paço, 67','Rio de Janeiro','RJ','05454-876','Brazil'),
(10254,14,5,'1996-07-11','1996-08-08','1996-07-23',2,22.98,'Chop-suey Chinese','Hauptstr. 29','Bern',NULL,'3012','Switzerland'),
(10255,68,9,'1996-07-12','1996-08-09','1996-07-15',3,148.33,'Richter Supermarkt','Grenzacherweg 237','Genève',NULL,'1203','Switzerland'),
(10256,88,3,'1996-07-15','1996-08-12','1996-07-17',2,13.97,'Wellington Importadora','Rua do Mercado, 12','Resende','SP','08737-363','Brazil'),
(10257,35,4,'1996-07-16','1996-08-13','1996-07-22',3,81.91,'HILARION-Abastos','Carrera 22 con Ave. Carlos Soublette #8-35','San Cristóbal','Táchira','5022','Venezuela'),
(10258,20,1,'1996-07-17','1996-08-14','1996-07-23',1,140.51,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10259,13,4,'1996-07-18','1996-08-15','1996-07-25',3,3.25,'Centro comercial Moctezuma','Sierras de Granada 9993','México D.F.',NULL,'05022','Mexico'),
(10260,56,4,'1996-07-19','1996-08-16','1996-07-29',1,55.09,'Ottilies Käseladen','Mehrheimerstr. 369','Köln',NULL,'50739','Germany'),
(10261,61,4,'1996-07-19','1996-08-16','1996-07-30',2,3.05,'Que Delícia','Rua da Panificadora, 12','Rio de Janeiro','RJ','02389-673','Brazil'),
(10262,65,8,'1996-07-22','1996-08-19','1996-07-25',3,48.29,'Rattlesnake Canyon Grocery','2817 Milton Dr.','Albuquerque','NM','87110','USA'),
(10263,20,9,'1996-07-23','1996-08-20','1996-07-31',3,146.06,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10264,24,6,'1996-07-24','1996-08-21','1996-08-23',3,3.67,'Folk och fä HB','Åkergatan 24','Bräcke',NULL,'S-844 67','Sweden'),
(10265,7,2,'1996-07-25','1996-08-22','1996-08-12',1,55.28,'Blondesddsl père et fils','24, place Kléber','Strasbourg',NULL,'67000','France'),
(10266,87,3,'1996-07-26','1996-09-06','1996-07-31',3,25.73,'Wartian Herkku','Torikatu 38','Oulu',NULL,'90110','Finland'),
(10267,25,4,'1996-07-29','1996-08-26','1996-08-06',1,208.58,'Frankenversand','Berliner Platz 43','München',NULL,'80805','Germany'),
(10268,20,8,'1996-07-30','1996-08-27','1996-08-02',3,66.29,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10269,89,5,'1996-07-31','1996-08-14','1996-08-09',1,4.56,'White Clover Markets','305 - 14th Ave. S. Suite 3B','Seattle','WA','98128','USA'),
(10270,87,1,'1996-08-01','1996-08-29','1996-08-02',1,136.54,'Wartian Herkku','Torikatu 38','Oulu',NULL,'90110','Finland'),
(10271,75,6,'1996-08-01','1996-08-29','1996-08-30',2,4.54,'Split Rail Beer & Ale','P.O. Box 555','Lander','WY','82520','USA'),
(10272,65,6,'1996-08-02','1996-08-30','1996-08-06',2,98.03,'Rattlesnake Canyon Grocery','2817 Milton Dr.','Albuquerque','NM','87110','USA'),
(10273,63,3,'1996-08-05','1996-09-02','1996-08-12',3,76.07,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10274,85,6,'1996-08-06','1996-09-03','1996-08-16',1,6.01,'Vins et alcools Chevalier','59 rue de l\'Abbaye','Reims',NULL,'51100','France'),
(10275,49,1,'1996-08-07','1996-09-04','1996-08-09',1,26.93,'Magazzini Alimentari Riuniti','Via Ludovico il Moro 22','Bergamo',NULL,'24100','Italy'),
(10276,79,8,'1996-08-08','1996-08-22','1996-08-14',3,13.84,'Toms Spezialitäten','Luisenstr. 48','Münster',NULL,'44087','Germany'),
(10277,52,2,'1996-08-09','1996-09-06','1996-08-13',3,125.77,'Morgenstern Gesundkost','Heerstr. 22','Leipzig',NULL,'04179','Germany'),
(10278,5,8,'1996-08-12','1996-09-09','1996-08-16',2,92.69,'Berglunds snabbköp','Berguvsvägen 8','Luleå',NULL,'S-958 22','Sweden'),
(10279,44,8,'1996-08-13','1996-09-10','1996-08-16',2,25.83,'Lehmanns Marktstand','Magazinweg 7','Frankfurt a.M.',NULL,'60528','Germany'),
(10280,5,2,'1996-08-14','1996-09-11','1996-09-12',1,8.98,'Berglunds snabbköp','Berguvsvägen 8','Luleå',NULL,'S-958 22','Sweden'),
(10281,69,4,'1996-08-14','1996-08-28','1996-08-21',2,2.94,'Romero y tomillo','Gran Vía, 1','Madrid',NULL,'28001','Spain'),
(10282,69,4,'1996-08-15','1996-09-12','1996-08-21',3,12.69,'Romero y tomillo','Gran Vía, 1','Madrid',NULL,'28001','Spain'),
(10283,46,3,'1996-08-16','1996-09-13','1996-08-23',3,84.81,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10284,44,4,'1996-08-19','1996-09-16','1996-08-27',3,76.56,'Lehmanns Marktstand','Magazinweg 7','Frankfurt a.M.',NULL,'60528','Germany'),
(10285,63,1,'1996-08-20','1996-09-17','1996-08-26',2,76.83,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10286,63,8,'1996-08-21','1996-09-18','1996-08-30',3,229.24,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10287,67,8,'1996-08-22','1996-09-19','1996-08-28',3,12.76,'Ricardo Adocicados','Av. Copacabana, 267','Rio de Janeiro','RJ','02389-890','Brazil'),
(10288,66,4,'1996-08-23','1996-09-20','1996-09-03',1,7.45,'Reggiani Caseifici','Strada Provinciale 124','Reggio Emilia',NULL,'42100','Italy'),
(10289,89,7,'1996-08-26','1996-09-23','1996-08-28',3,22.77,'White Clover Markets','305 - 14th Ave. S. Suite 3B','Seattle','WA','98128','USA'),
(10290,15,8,'1996-08-27','1996-09-24','1996-09-03',1,79.70,'Comércio Mineiro','Av. dos Lusíadas, 23','Sao Paulo','SP','05432-043','Brazil'),
(10291,61,6,'1996-08-27','1996-09-24','1996-09-04',2,6.40,'Que Delícia','Rua da Panificadora, 12','Rio de Janeiro','RJ','02389-673','Brazil'),
(10292,81,1,'1996-08-28','1996-09-25','1996-09-02',2,1.35,'Tradição Hipermercados','Av. Inês de Castro, 414','Sao Paulo','SP','05634-030','Brazil'),
(10293,80,1,'1996-08-29','1996-09-26','1996-09-11',3,21.18,'Tortuga Restaurante','Avda. Azteca 123','México D.F.',NULL,'05033','Mexico'),
(10294,65,4,'1996-08-30','1996-09-27','1996-09-05',2,147.26,'Rattlesnake Canyon Grocery','2817 Milton Dr.','Albuquerque','NM','87110','USA'),
(10295,85,2,'1996-09-02','1996-09-30','1996-09-10',2,1.15,'Vins et alcools Chevalier','59 rue de l\'Abbaye','Reims',NULL,'51100','France'),
(10296,46,6,'1996-09-03','1996-10-01','1996-09-11',1,0.12,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10297,7,5,'1996-09-04','1996-10-16','1996-09-10',2,5.74,'Blondesddsl père et fils','24, place Kléber','Strasbourg',NULL,'67000','France'),
(10298,37,6,'1996-09-05','1996-10-03','1996-09-11',2,168.22,'Hungry Owl All-Night Grocers','8 Johnstown Road','Cork',NULL,NULL,'Ireland'),
(10299,67,4,'1996-09-06','1996-10-04','1996-09-13',2,29.76,'Ricardo Adocicados','Av. Copacabana, 267','Rio de Janeiro','RJ','02389-890','Brazil'),
(10300,49,2,'1996-09-09','1996-10-07','1996-09-18',2,17.68,'Magazzini Alimentari Riuniti','Via Ludovico il Moro 22','Bergamo',NULL,'24100','Italy'),
(10301,86,8,'1996-09-09','1996-10-07','1996-09-17',2,45.08,'Die Wandernde Kuh','Adenauerallee 900','Stuttgart',NULL,'70563','Germany'),
(10302,76,4,'1996-09-10','1996-10-08','1996-10-09',2,6.27,'Suprêmes délices','Boulevard Tirou, 255','Charleroi',NULL,'B-6000','Belgium'),
(10303,30,7,'1996-09-11','1996-10-09','1996-09-18',2,107.83,'Godos Cocina Típica','C/ Romero, 33','Sevilla',NULL,'41101','Spain'),
(10304,80,1,'1996-09-12','1996-10-10','1996-09-17',2,63.79,'Tortuga Restaurante','Avda. Azteca 123','México D.F.',NULL,'05033','Mexico'),
(10305,55,8,'1996-09-13','1996-10-11','1996-10-09',3,257.62,'Old World Delicatessen','2743 Bering St.','Anchorage','AK','99508','USA'),
(10306,69,1,'1996-09-16','1996-10-14','1996-09-23',3,7.56,'Romero y tomillo','Gran Vía, 1','Madrid',NULL,'28001','Spain'),
(10307,48,2,'1996-09-17','1996-10-15','1996-09-25',2,0.56,'Lonesome Pine Restaurant','89 Chiaroscuro Rd.','Portland','OR','97219','USA'),
(10308,2,7,'1996-09-18','1996-10-16','1996-09-24',3,1.61,'Ana Trujillo Emparedados y helados','Avda. de la Constitución 2222','México D.F.',NULL,'05021','Mexico'),
(10309,37,3,'1996-09-19','1996-10-17',NULL,1,47.30,'Hungry Owl All-Night Grocers','8 Johnstown Road','Cork',NULL,NULL,'Ireland'),
(10310,77,8,'1996-09-20','1996-10-18','1996-09-27',2,17.52,'The Big Cheese','89 Jefferson Way Suite 2','Portland','OR','97201','USA'),
(10311,18,1,'1996-09-20','1996-10-04','1996-09-26',3,24.69,'Du monde entier','67, rue des Cinquante Otages','Nantes',NULL,'44000','France'),
(10312,86,2,'1996-09-23','1996-10-21','1996-10-03',2,40.26,'Die Wandernde Kuh','Adenauerallee 900','Stuttgart',NULL,'70563','Germany'),
(10313,63,2,'1996-09-24','1996-10-22','1996-10-04',2,1.96,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10314,65,1,'1996-09-25','1996-10-23','1996-10-04',2,74.16,'Rattlesnake Canyon Grocery','2817 Milton Dr.','Albuquerque','NM','87110','USA'),
(10315,38,4,'1996-09-26','1996-10-24','1996-10-03',2,41.76,'Island Trading','Garden House Crowther Way','Cowes',NULL,'PO31 7PJ','UK'),
(10316,65,1,'1996-09-27','1996-10-25','1996-10-08',3,150.15,'Rattlesnake Canyon Grocery','2817 Milton Dr.','Albuquerque','NM','87110','USA'),
(10317,48,6,'1996-09-30','1996-10-28','1996-10-10',1,12.69,'Lonesome Pine Restaurant','89 Chiaroscuro Rd.','Portland','OR','97219','USA'),
(10318,38,8,'1996-10-01','1996-10-29','1996-10-04',2,4.73,'Island Trading','Garden House Crowther Way','Cowes',NULL,'PO31 7PJ','UK'),
(10319,79,7,'1996-10-02','1996-10-30','1996-10-11',3,64.50,'Toms Spezialitäten','Luisenstr. 48','Münster',NULL,'44087','Germany'),
(10320,87,5,'1996-10-03','1996-10-17','1996-10-18',3,34.57,'Wartian Herkku','Torikatu 38','Oulu',NULL,'90110','Finland'),
(10321,38,3,'1996-10-03','1996-10-31','1996-10-11',2,3.43,'Island Trading','Garden House Crowther Way','Cowes',NULL,'PO31 7PJ','UK'),
(10322,58,7,'1996-10-04','1996-11-01','1996-10-23',3,0.40,'Pericles Comidas clásicas','Calle Dr. Jorge Cash 321','México D.F.',NULL,'05033','Mexico'),
(10323,39,4,'1996-10-07','1996-11-04','1996-10-14',1,4.88,'Königlich Essen','Maubelstr. 90','Brandenburg',NULL,'14776','Germany'),
(10324,71,9,'1996-10-08','1996-11-05','1996-10-10',1,214.27,'Save-a-lot Markets','187 Suffolk Ln.','Boise','ID','83720','USA'),
(10325,39,1,'1996-10-09','1996-10-23','1996-10-14',3,64.86,'Königlich Essen','Maubelstr. 90','Brandenburg',NULL,'14776','Germany'),
(10326,8,4,'1996-10-10','1996-11-07','1996-10-14',2,77.92,'Bólido Comidas preparadas','C/ Araquil, 67','Madrid',NULL,'28023','Spain'),
(10327,24,2,'1996-10-11','1996-11-08','1996-10-14',1,63.36,'Folk och fä HB','Åkergatan 24','Bräcke',NULL,'S-844 67','Sweden'),
(10328,28,9,'1996-10-14','1996-11-11','1996-10-17',3,87.03,'Furia Bacalhau e Frutos do Mar','Jardim das rosas n. 32','Lisboa',NULL,'1675','Portugal'),
(10329,75,4,'1996-10-15','1996-11-26','1996-10-23',2,191.67,'Split Rail Beer & Ale','P.O. Box 555','Lander','WY','82520','USA'),
(10330,46,3,'1996-10-16','1996-11-13','1996-10-28',1,12.75,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10331,9,9,'1996-10-16','1996-11-27','1996-10-21',1,10.19,'Bon app','12, rue des Bouchers','Marseille',NULL,'13008','France'),
(10332,51,3,'1996-10-17','1996-11-28','1996-10-21',2,52.84,'Mère Paillarde','43 rue St. Laurent','Montréal','Québec','H1J 1C3','Canada'),
(10333,87,5,'1996-10-18','1996-11-15','1996-10-25',3,0.59,'Wartian Herkku','Torikatu 38','Oulu',NULL,'90110','Finland'),
(10334,84,8,'1996-10-21','1996-11-18','1996-10-28',2,8.56,'Victuailles en stock','2, rue du Commerce','Lyon',NULL,'69004','France'),
(10335,37,7,'1996-10-22','1996-11-19','1996-10-24',2,42.11,'Hungry Owl All-Night Grocers','8 Johnstown Road','Cork',NULL,NULL,'Ireland'),
(10336,60,7,'1996-10-23','1996-11-20','1996-10-25',2,15.51,'Princesa Isabel Vinhoss','Estrada da saúde n. 58','Lisboa',NULL,'1756','Portugal'),
(10337,25,4,'1996-10-24','1996-11-21','1996-10-29',3,108.26,'Frankenversand','Berliner Platz 43','München',NULL,'80805','Germany'),
(10338,55,4,'1996-10-25','1996-11-22','1996-10-29',3,84.21,'Old World Delicatessen','2743 Bering St.','Anchorage','AK','99508','USA'),
(10339,51,2,'1996-10-28','1996-11-25','1996-11-04',2,15.66,'Mère Paillarde','43 rue St. Laurent','Montréal','Québec','H1J 1C3','Canada'),
(10340,25,1,'1996-10-29','1996-11-26','1996-11-08',3,166.31,'Frankenversand','Berliner Platz 43','München',NULL,'80805','Germany'),
(10341,73,7,'1996-10-29','1996-11-26','1996-11-05',3,26.78,'Simons bistro','Vinbæltet 34','Kobenhavn',NULL,'1734','Denmark'),
(10342,25,4,'1996-10-30','1996-11-13','1996-11-04',2,54.83,'Frankenversand','Berliner Platz 43','München',NULL,'80805','Germany'),
(10343,44,4,'1996-10-31','1996-11-28','1996-11-06',1,110.37,'Lehmanns Marktstand','Magazinweg 7','Frankfurt a.M.',NULL,'60528','Germany'),
(10344,89,4,'1996-11-01','1996-11-29','1996-11-05',2,23.29,'White Clover Markets','305 - 14th Ave. S. Suite 3B','Seattle','WA','98128','USA'),
(10345,63,2,'1996-11-04','1996-12-02','1996-11-11',2,249.06,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10346,65,3,'1996-11-05','1996-12-17','1996-11-08',3,142.08,'Rattlesnake Canyon Grocery','2817 Milton Dr.','Albuquerque','NM','87110','USA'),
(10347,21,4,'1996-11-06','1996-12-04','1996-11-08',3,3.10,'Familia Arquibaldo','Rua Orós, 92','Sao Paulo','SP','05442-030','Brazil'),
(10348,86,4,'1996-11-07','1996-12-05','1996-11-15',2,0.78,'Die Wandernde Kuh','Adenauerallee 900','Stuttgart',NULL,'70563','Germany'),
(10349,75,7,'1996-11-08','1996-12-06','1996-11-15',1,8.63,'Split Rail Beer & Ale','P.O. Box 555','Lander','WY','82520','USA'),
(10350,41,3,'1996-11-11','1996-12-09','1996-12-03','La maison d\'Asie','1 rue Alsace-Lorraine','Toulouse',NULL,'31000','France',2,64.19),
(10351,20,1,'1996-11-11','1996-12-09','1996-11-20',1,162.33,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10352,28,3,'1996-11-12','1996-11-26','1996-11-18',3,1.30,'Furia Bacalhau e Frutos do Mar','Jardim das rosas n. 32','Lisboa',NULL,'1675','Portugal'),
(10353,63,7,'1996-11-13','1996-12-11','1996-11-25',3,360.63,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10354,58,8,'1996-11-14','1996-12-12','1996-11-20',3,53.80,'Pericles Comidas clásicas','Calle Dr. Jorge Cash 321','México D.F.',NULL,'05033','Mexico'),
(10355,4,6,'1996-11-15','1996-12-13','1996-11-20',1,41.95,'Around the Horn','120 Hanover Sq.','London',NULL,'WA1 1DP','UK'),
(10356,86,6,'1996-11-18','1996-12-16','1996-11-27',2,36.71,'Die Wandernde Kuh','Adenauerallee 900','Stuttgart',NULL,'70563','Germany'),
(10357,63,1,'1996-11-19','1996-12-17','1996-12-02',3,34.88,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10358,4,5,'1996-11-20','1996-12-18','1996-11-27',1,19.64,'Around the Horn','120 Hanover Sq.','London',NULL,'WA1 1DP','UK'),
(10359,72,5,'1996-11-21','1996-12-19','1996-11-26',3,288.43,'Seven Seas Imports','90 Wadhurst Rd.','London',NULL,'OX15 4NB','UK'),
(10360,7,4,'1996-11-22','1996-12-20','1996-12-02',3,131.70,'Blondesddsl père et fils','24, place Kléber','Strasbourg',NULL,'67000','France'),
(10361,63,1,'1996-11-22','1996-12-20','1996-12-03',2,183.17,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10362,9,3,'1996-11-25','1996-12-23','1996-11-28',1,96.04,'Bon app','12, rue des Bouchers','Marseille',NULL,'13008','France'),
(10363,17,4,'1996-11-26','1996-12-24','1996-12-04',3,30.54,'Drachenblut Delikatessenn','Walserweg 21','Aachen',NULL,'52066','Germany'),
(10364,19,1,'1996-11-26','1997-01-07','1996-12-04',1,71.97,'Eastern Connection','35 King George','London',NULL,'WX3 6FW','UK'),
(10365,3,3,'1996-11-27','1996-12-25','1996-12-02',2,22.00,'Antonio Moreno Taquería','Mataderos 2312','México D.F.',NULL,'05023','Mexico'),
(10366,29,8,'1996-11-28','1997-01-09','1996-12-30',2,10.14,'Galería del gastrónomo','Rambla de Cataluña, 23','Barcelona',NULL,'8022','Spain'),
(10367,83,7,'1996-11-28','1996-12-26','1996-12-02',3,13.55,'Vaffeljernet','Smagsloget 45','Århus',NULL,'8200','Denmark'),
(10368,20,2,'1996-11-29','1996-12-27','1996-12-02',2,101.95,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10369,75,8,'1996-12-02','1996-12-30','1996-12-09',2,195.68,'Split Rail Beer & Ale','P.O. Box 555','Lander','WY','82520','USA'),
(10370,14,6,'1996-12-03','1996-12-31','1996-12-27',2,1.17,'Chop-suey Chinese','Hauptstr. 29','Bern',NULL,'3012','Switzerland'),
(10371,41,1,'1996-12-03','1996-12-31','1996-12-24',1,0.45,'La maison d\'Asie','1 rue Alsace-Lorraine','Toulouse',NULL,'31000','France'),
(10372,62,5,'1996-12-04','1997-01-01','1996-12-09',2,890.78,'Queen Cozinha','Alameda dos Canàrios, 891','Sao Paulo','SP','05487-020','Brazil'),
(10373,37,4,'1996-12-05','1997-01-02','1996-12-11',3,124.12,'Hungry Owl All-Night Grocers','8 Johnstown Road','Cork',NULL,NULL,'Ireland'),
(10374,91,1,'1996-12-05','1997-01-02','1996-12-09',3,3.94,'Wolski','ul. Filtrowa 68','Warszawa',NULL,'01-012','Poland'),
(10375,37,3,'1996-12-06','1997-01-03','1996-12-09',2,20.12,'Hungry Owl All-Night Grocers','8 Johnstown Road','Cork',NULL,NULL,'Ireland'),
(10376,51,1,'1996-12-09','1997-01-06','1996-12-13',2,20.39,'Mère Paillarde','43 rue St. Laurent','Montréal','Québec','H1J 1C3','Canada'),
(10377,71,1,'1996-12-09','1997-01-06','1996-12-13',3,22.21,'Save-a-lot Markets','187 Suffolk Ln.','Boise','ID','83720','USA'),
(10378,24,5,'1996-12-10','1997-01-07','1996-12-19',3,5.44,'Folk och fä HB','Åkergatan 24','Bräcke',NULL,'S-844 67','Sweden'),
(10379,41,2,'1996-12-11','1997-01-08','1996-12-13',1,45.03,'La maison d\'Asie','1 rue Alsace-Lorraine','Toulouse',NULL,'31000','France'),
(10380,37,8,'1996-12-12','1997-01-09','1997-01-16',3,35.03,'Hungry Owl All-Night Grocers','8 Johnstown Road','Cork',NULL,NULL,'Ireland'),
(10381,46,3,'1996-12-12','1997-01-09','1996-12-13',3,7.99,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10382,20,4,'1996-12-13','1997-01-10','1996-12-16',1,94.77,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10383,4,8,'1996-12-16','1997-01-13','1996-12-18',3,34.24,'Around the Horn','120 Hanover Sq.','London',NULL,'WA1 1DP','UK'),
(10384,5,3,'1996-12-16','1997-01-13','1996-12-20',3,168.64,'Berglunds snabbköp','Berguvsvägen 8','Luleå',NULL,'S-958 22','Sweden'),
(10385,75,1,'1996-12-17','1997-01-14','1996-12-23',2,30.96,'Split Rail Beer & Ale','P.O. Box 555','Lander','WY','82520','USA'),
(10386,21,9,'1996-12-18','1997-01-01','1996-12-25',3,13.99,'Familia Arquibaldo','Rua Orós, 92','Sao Paulo','SP','05442-030','Brazil'),
(10387,70,1,'1996-12-18','1997-01-15','1996-12-20',2,93.63,'Santé Gourmet','Erling Skakkes gate 78','Stavern',NULL,'4110','Norway'),
(10388,72,2,'1996-12-19','1997-01-16','1996-12-20',1,34.86,'Seven Seas Imports','90 Wadhurst Rd.','London',NULL,'OX15 4NB','UK'),
(10389,10,4,'1996-12-20','1997-01-17','1996-12-24',2,47.42,'Bottom-Dollar Marketss','23 Tsawassen Blvd.','Tsawassen','BC','T2F 8M4','Canada'),
(10390,20,6,'1996-12-23','1997-01-20','1996-12-26',1,126.38,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10391,17,3,'1996-12-23','1997-01-20','1996-12-31',3,5.45,'Drachenblut Delikatessenn','Walserweg 21','Aachen',NULL,'52066','Germany'),
(10392,63,2,'1996-12-24','1997-01-21','1997-01-01',3,122.46,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10393,71,1,'1996-12-25','1997-01-22','1997-01-03',3,126.56,'Save-a-lot Markets','187 Suffolk Ln.','Boise','ID','83720','USA'),
(10394,36,1,'1996-12-25','1997-01-22','1997-01-03',3,30.34,'Hungry Coyote Import Store','City Center Plaza 516 Main St.','Elgin','OR','97827','USA'),
(10395,35,6,'1996-12-26','1997-01-23','1997-01-03',1,184.41,'Steeleye Stout - N/A',NULL,NULL,NULL,NULL,NULL),
(10396,63,7,'1996-12-27','1997-01-10','1997-01-06',3,135.35,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10397,60,5,'1996-12-27','1997-01-24','1997-01-02',1,60.26,'Princesa Isabel Vinhoss','Estrada da saúde n. 58','Lisboa',NULL,'1756','Portugal'),
(10398,71,2,'1996-12-30','1997-01-27','1997-01-09',3,89.16,'Save-a-lot Markets','187 Suffolk Ln.','Boise','ID','83720','USA'),
(10399,83,8,'1996-12-31','1997-01-14','1997-01-08',3,27.36,'Vaffeljernet','Smagsloget 45','Århus',NULL,'8200','Denmark'),
(10400,19,1,'1997-01-01','1997-01-29','1997-01-16',3,83.93,'Eastern Connection','35 King George','London',NULL,'WX3 6FW','UK'),
(10401,46,1,'1997-01-01','1997-01-29','1997-01-10',1,12.51,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10402,20,8,'1997-01-02','1997-02-13','1997-01-10',2,67.88,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10403,20,4,'1997-01-03','1997-01-31','1997-01-09',3,73.79,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10404,49,2,'1997-01-03','1997-01-31','1997-01-08',1,155.97,'Magazzini Alimentari Riuniti','Via Ludovico il Moro 22','Bergamo',NULL,'24100','Italy'),
(10405,47,1,'1997-01-06','1997-02-03','1997-01-22',1,34.82,'Piccolo und mehr','Geislweg 14','Salzburg',NULL,'5020','Austria'),
(10406,62,7,'1997-01-07','1997-02-18','1997-01-13',1,108.04,'Queen Cozinha','Alameda dos Canàrios, 891','Sao Paulo','SP','05487-020','Brazil'),
(10407,63,3,'1997-01-07','1997-02-04','1997-01-30',2,91.48,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10408,71,8,'1997-01-08','1997-02-05','1997-01-14',1,11.26,'Save-a-lot Markets','187 Suffolk Ln.','Boise','ID','83720','USA'),
(10409,54,3,'1997-01-09','1997-02-06','1997-01-14',1,29.83,'Océano Atlántico Ltda.','Ing. Gustavo Moncada 8585 Piso 20-A','Buenos Aires',NULL,'1010','Argentina'),
(10410,10,3,'1997-01-10','1997-02-07','1997-01-15',3,2.40,'Bottom-Dollar Marketss','23 Tsawassen Blvd.','Tsawassen','BC','T2F 8M4','Canada'),
(10411,10,9,'1997-01-10','1997-02-07','1997-01-21',3,23.65,'Bottom-Dollar Marketss','23 Tsawassen Blvd.','Tsawassen','BC','T2F 8M4','Canada'),
(10412,87,8,'1997-01-13','1997-02-10','1997-01-15',2,3.77,'Wartian Herkku','Torikatu 38','Oulu',NULL,'90110','Finland'),
(10413,41,3,'1997-01-14','1997-02-11','1997-01-16',2,95.66,'La maison d\'Asie','1 rue Alsace-Lorraine','Toulouse',NULL,'31000','France'),
(10414,21,2,'1997-01-14','1997-02-11','1997-01-17',3,21.48,'Familia Arquibaldo','Rua Orós, 92','Sao Paulo','SP','05442-030','Brazil'),
(10415,36,3,'1997-01-15','1997-02-12','1997-01-24',1,0.20,'Hungry Coyote Import Store','City Center Plaza 516 Main St.','Elgin','OR','97827','USA'),
(10416,87,8,'1997-01-16','1997-02-13','1997-01-23',3,22.72,'Wartian Herkku','Torikatu 38','Oulu',NULL,'90110','Finland'),
(10417,73,4,'1997-01-16','1997-02-13','1997-01-28',3,70.29,'Simons bistro','Vinbæltet 34','Kobenhavn',NULL,'1734','Denmark'),
(10418,63,4,'1997-01-17','1997-02-14','1997-01-24',1,17.55,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10419,46,4,'1997-01-20','1997-02-17','1997-01-30',2,137.35,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10420,88,3,'1997-01-21','1997-02-18','1997-01-27',1,44.12,'Wellington Importadora','Rua do Mercado, 12','Resende','SP','08737-363','Brazil'),
(10421,61,8,'1997-01-21','1997-03-04','1997-01-27',1,99.23,'Que Delícia','Rua da Panificadora, 12','Rio de Janeiro','RJ','02389-673','Brazil'),
(10422,27,2,'1997-01-22','1997-02-19','1997-01-31',1,3.02,'Franchi S.p.A.','Via Monte Bianco 34','Torino',NULL,'10100','Italy'),
(10423,31,6,'1997-01-23','1997-02-06',NULL,3,24.50,'Gourmet Lanchonetes','Av. Brasil, 442','Campinas','SP','04876-786','Brazil'),
(10424,63,7,'1997-01-23','1997-02-20','1997-01-27',2,370.61,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10425,41,6,'1997-01-24','1997-02-21',NULL,2,7.93,'La maison d\'Asie','1 rue Alsace-Lorraine','Toulouse',NULL,'31000','France'),
(10426,29,4,'1997-01-27','1997-02-24','1997-02-06',1,18.69,'Galería del gastrónomo','Rambla de Cataluña, 23','Barcelona',NULL,'8022','Spain'),
(10427,59,4,'1997-01-27','1997-02-24','1997-03-03',2,31.29,'Piccolo und mehr','Geislweg 14','Salzburg',NULL,'5020','Austria'),
(10428,66,7,'1997-01-28','1997-02-25','1997-02-04',1,11.09,'Reggiani Caseifici','Strada Provinciale 124','Reggio Emilia',NULL,'42100','Italy'),
(10429,37,3,'1997-01-29','1997-03-12','1997-02-07',2,56.63,'Hungry Owl All-Night Grocers','8 Johnstown Road','Cork',NULL,NULL,'Ireland'),
(10430,20,4,'1997-01-30','1997-02-13','1997-02-03',1,458.78,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10431,10,4,'1997-01-30','1997-02-13','1997-02-07',2,44.17,'Bottom-Dollar Marketss','23 Tsawassen Blvd.','Tsawassen','BC','T2F 8M4','Canada'),
(10432,75,3,'1997-01-31','1997-02-14','1997-02-07',2,4.34,'Split Rail Beer & Ale','P.O. Box 555','Lander','WY','82520','USA'),
(10433,60,3,'1997-02-03','1997-03-03',NULL,3,73.83,'Princesa Isabel Vinhoss','Estrada da saúde n. 58','Lisboa',NULL,'1756','Portugal'),
(10434,24,3,'1997-02-03','1997-03-03','1997-02-13',2,17.92,'Folk och fä HB','Åkergatan 24','Bräcke',NULL,'S-844 67','Sweden'),
(10435,16,8,'1997-02-04','1997-03-18','1997-02-07',2,9.21,'Consolidated Holdings','Berkeley Gardens 12 Brewery','London',NULL,'WX1 6LT','UK'),
(10436,7,3,'1997-02-05','1997-03-05','1997-02-11',2,156.66,'Blondesddsl père et fils','24, place Kléber','Strasbourg',NULL,'67000','France'),
(10437,87,8,'1997-02-05','1997-03-05','1997-02-12',1,19.97,'Wartian Herkku','Torikatu 38','Oulu',NULL,'90110','Finland'),
(10438,79,3,'1997-02-06','1997-03-06','1997-02-14',2,8.24,'Toms Spezialitäten','Luisenstr. 48','Münster',NULL,'44087','Germany'),
(10439,51,6,'1997-02-07','1997-03-07','1997-02-10',3,4.07,'Mère Paillarde','43 rue St. Laurent','Montréal','Québec','H1J 1C3','Canada'),
(10440,71,4,'1997-02-10','1997-03-10','1997-02-28',2,86.53,'Save-a-lot Markets','187 Suffolk Ln.','Boise','ID','83720','USA'),
(10441,55,3,'1997-02-10','1997-03-24','1997-03-14',2,73.02,'Old World Delicatessen','2743 Bering St.','Anchorage','AK','99508','USA'),
(10442,20,3,'1997-02-11','1997-03-11','1997-02-18',2,47.94,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10443,66,8,'1997-02-12','1997-03-12','1997-02-14',1,13.95,'Reggiani Caseifici','Strada Provinciale 124','Reggio Emilia',NULL,'42100','Italy'),
(10444,89,3,'1997-02-12','1997-03-12','1997-02-21',3,3.50,'White Clover Markets','305 - 14th Ave. S. Suite 3B','Seattle','WA','98128','USA'),
(10445,11,3,'1997-02-13','1997-03-13','1997-02-20',1,9.30,'B\'s Beverages','Fauntleroy Circus','London',NULL,'EC2 5NT','UK'),
(10446,19,6,'1997-02-14','1997-03-14','1997-02-19',1,14.68,'Eastern Connection','35 King George','London',NULL,'WX3 6FW','UK'),
(10447,53,4,'1997-02-14','1997-03-14','1997-03-07',2,68.66,'North/South','South House 300 Queensbridge','London',NULL,'SW7 1RZ','UK'),
(10448,72,4,'1997-02-17','1997-03-17','1997-02-24',2,38.82,'Seven Seas Imports','90 Wadhurst Rd.','London',NULL,'OX15 4NB','UK'),
(10449,71,3,'1997-02-18','1997-03-18','1997-02-27',2,53.30,'Save-a-lot Markets','187 Suffolk Ln.','Boise','ID','83720','USA'),
(10450,20,8,'1997-02-19','1997-03-19','1997-03-11',2,7.23,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10451,63,4,'1997-02-19','1997-03-05',NULL,3,189.09,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10452,63,8,'1997-02-20','1997-03-20','1997-02-26',1,140.26,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10453,63,4,'1997-02-21','1997-03-21','1997-02-26',2,25.36,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10454,24,4,'1997-02-21','1997-03-21','1997-02-25',3,2.74,'Folk och fä HB','Åkergatan 24','Bräcke',NULL,'S-844 67','Sweden'),
(10455,34,8,'1997-02-24','1997-04-07','1997-03-03',2,180.45,'Hanari Carnes','Rua do Paço, 67','Rio de Janeiro','RJ','05454-876','Brazil'),
(10456,8,8,'1997-02-25','1997-04-08','1997-02-28',2,8.12,'Bólido Comidas preparadas','C/ Araquil, 67','Madrid',NULL,'28023','Spain'),
(10457,63,1,'1997-02-25','1997-03-25','1997-03-03',1,11.57,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10458,20,7,'1997-02-26','1997-03-26','1997-03-04',3,147.06,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10459,84,4,'1997-02-27','1997-03-27','1997-02-28',2,25.09,'Victuailles en stock','2, rue du Commerce','Lyon',NULL,'69004','France'),
(10460,25,8,'1997-02-28','1997-03-28','1997-03-03',1,16.27,'Frankenversand','Berliner Platz 43','München',NULL,'80805','Germany'),
(10461,46,1,'1997-02-28','1997-03-28','1997-03-06',3,148.61,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10462,19,2,'1997-03-03','1997-03-31','1997-03-18',1,6.17,'Eastern Connection','35 King George','London',NULL,'WX3 6FW','UK'),
(10463,40,5,'1997-03-04','1997-04-01','1997-03-06',3,14.78,'La corne d\'abondance','67, avenue de l\'Europe','Versailles',NULL,'78000','France'),
(10464,22,4,'1997-03-04','1997-04-01','1997-03-14',2,89.00,'FISSA Fabrica Inter. Salchichas S.A.','C/ Moralzarzal, 86','Madrid',NULL,'28034','Spain'),
(10465,63,1,'1997-03-05','1997-04-02','1997-03-14',3,145.04,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10466,9,4,'1997-03-06','1997-04-03','1997-03-13',1,11.93,'Bon app','12, rue des Bouchers','Marseille',NULL,'13008','France'),
(10467,23,8,'1997-03-06','1997-04-03','1997-03-28',2,4.93,'Folies gourmandes','184, chaussée de Tournai','Lille',NULL,'59000','France'),
(10468,81,3,'1997-03-07','1997-04-04','1997-03-12',1,44.12,'Tradição Hipermercados','Av. Inês de Castro, 414','Sao Paulo','SP','05634-030','Brazil'),
(10469,89,1,'1997-03-10','1997-04-07','1997-03-14',1,60.18,'White Clover Markets','305 - 14th Ave. S. Suite 3B','Seattle','WA','98128','USA'),
(10470,38,4,'1997-03-11','1997-04-08','1997-03-14',2,18.84,'Island Trading','Garden House Crowther Way','Cowes',NULL,'PO31 7PJ','UK'),
(10471,14,2,'1997-03-11','1997-04-08','1997-03-18',3,45.59,'Chop-suey Chinese','Hauptstr. 29','Bern',NULL,'3012','Switzerland'),
(10472,20,8,'1997-03-12','1997-04-09','1997-03-19',1,4.20,'Ernst Handel','Kirchgasse 6','Graz',NULL,'8010','Austria'),
(10473,87,1,'1997-03-13','1997-03-27','1997-03-21',3,16.37,'Wartian Herkku','Torikatu 38','Oulu',NULL,'90110','Finland'),
(10474,58,5,'1997-03-13','1997-04-10','1997-03-21',2,83.49,'Pericles Comidas clásicas','Calle Dr. Jorge Cash 321','México D.F.',NULL,'05033','Mexico'),
(10475,46,9,'1997-03-14','1997-04-11','1997-04-04',1,68.52,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10476,46,8,'1997-03-14','1997-04-11','1997-03-21',3,4.41,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10477,63,5,'1997-03-17','1997-04-14','1997-03-25',1,13.02,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10478,63,2,'1997-03-18','1997-04-01','1997-03-26',3,4.81,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10479,63,3,'1997-03-19','1997-04-16','1997-03-21',3,708.95,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10480,83,6,'1997-03-20','1997-04-17','1997-03-24',2,1.35,'Vaffeljernet','Smagsloget 45','Århus',NULL,'8200','Denmark'),
(10481,73,8,'1997-03-20','1997-04-17','1997-03-25',2,64.33,'Simons bistro','Vinbæltet 34','Kobenhavn',NULL,'1734','Denmark'),
(10482,40,1,'1997-03-21','1997-04-18','1997-04-10',3,7.48,'La corne d\'abondance','67, avenue de l\'Europe','Versailles',NULL,'78000','France'),
(10483,60,7,'1997-03-24','1997-04-21',NULL,2,15.28,'Princesa Isabel Vinhoss','Estrada da saúde n. 58','Lisboa',NULL,'1756','Portugal'),
(10484,9,3,'1997-03-24','1997-04-21','1997-04-01',3,6.41,'Bon app','12, rue des Bouchers','Marseille',NULL,'13008','France'),
(10485,34,4,'1997-03-25','1997-04-08','1997-03-31',2,31.89,'Hanari Carnes','Rua do Paço, 67','Rio de Janeiro','RJ','05454-876','Brazil'),
(10486,21,1,'1997-03-26','1997-04-23','1997-04-02',2,30.53,'Familia Arquibaldo','Rua Orós, 92','Sao Paulo','SP','05442-030','Brazil'),
(10487,25,2,'1997-03-26','1997-04-23','1997-03-28',1,71.07,'Frankenversand','Berliner Platz 43','München',NULL,'80805','Germany'),
(10488,63,8,'1997-03-27','1997-04-24','1997-04-02',2,4.93,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10489,44,8,'1997-03-28','1997-04-25','1997-04-09',2,5.29,'Lehmanns Marktstand','Magazinweg 7','Frankfurt a.M.',NULL,'60528','Germany'),
(10490,63,7,'1997-03-31','1997-04-28','1997-04-03',2,210.19,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10491,70,8,'1997-03-31','1997-04-28','1997-04-08',3,16.96,'Santé Gourmet','Erling Skakkes gate 78','Stavern',NULL,'4110','Norway'),
(10492,19,3,'1997-04-01','1997-04-29','1997-04-11',1,62.89,'Eastern Connection','35 King George','London',NULL,'WX3 6FW','UK'),
(10493,32,4,'1997-04-02','1997-04-30','1997-04-10',3,10.64,'Great Lakes Food Market','2732 Baker Blvd.','Eugene','OR','97403','USA'),
(10494,35,4,'1997-04-02','1997-04-30','1997-04-09',2,65.99,'Steeleye Stout - N/A',NULL,NULL,NULL,NULL,NULL),
(10495,46,3,'1997-04-03','1997-05-01','1997-04-11',3,4.65,'LILA-Supermercado','Carrera 52 con Ave. Bolívar','Barquisimeto','Lara','3508','Venezuela'),
(10496,19,7,'1997-04-04','1997-05-02','1997-04-07',2,46.77,'Eastern Connection','35 King George','London',NULL,'WX3 6FW','UK'),
(10497,25,7,'1997-04-07','1997-05-05','1997-04-16',1,36.21,'Frankenversand','Berliner Platz 43','München',NULL,'80805','Germany'),
(10498,79,8,'1997-04-07','1997-05-05','1997-04-11',2,29.75,'Toms Spezialitäten','Luisenstr. 48','Münster',NULL,'44087','Germany'),
(10499,63,4,'1997-04-08','1997-05-06','1997-04-16',2,102.02,'QUICK-Stop','Taucherstraße 10','Cunewalde',NULL,'01307','Germany'),
(10500,25,6,'1997-04-09','1997-05-07','1997-04-17',1,42.68,'Frankenversand','Berliner Platz 43','München',NULL,'80805','Germany');
COMMIT;

-- [NOTA: Los pedidos 10501-11077 siguen el mismo patrón y se incluirían aquí]
-- Para práctica académica, los primeros 253 pedidos son representativos del conjunto completo.
-- Fuente completa: https://en.wikiversity.org/wiki/Database_Examples/Northwind/MySQL

-- =============================================================================
-- DATOS: OrderDetails
-- CORRECCIÓN CLAVE: Cada línea incluye UnitPrice (precio histórico) y Discount
-- UnitPrice puede diferir de Products.UnitPrice si el precio cambió con el tiempo
-- Discount: valores típicos 0, 0.05, 0.10, 0.15, 0.20, 0.25
-- =============================================================================
START TRANSACTION;
INSERT INTO OrderDetails (OrderID, ProductID, UnitPrice, Quantity, Discount) VALUES
(10248,11,14.00,12,0.00),(10248,42,9.80,10,0.00),(10248,72,34.80,5,0.00),
(10249,14,18.60,9,0.00),(10249,51,42.40,40,0.00),
(10250,41,7.70,10,0.00),(10250,51,42.40,35,0.15),(10250,65,16.80,15,0.15),
(10251,22,16.80,6,0.05),(10251,57,15.60,15,0.05),(10251,65,16.80,20,0.00),
(10252,20,64.80,40,0.05),(10252,33,2.00,25,0.05),(10252,60,27.20,40,0.00),
(10253,31,10.00,20,0.00),(10253,39,14.40,42,0.00),(10253,49,16.00,40,0.00),
(10254,24,3.60,15,0.15),(10254,55,19.20,21,0.15),(10254,74,8.00,21,0.00),
(10255,2,15.20,20,0.00),(10255,16,13.90,35,0.00),(10255,36,15.20,25,0.00),(10255,59,44.00,30,0.00),
(10256,53,26.20,15,0.00),(10256,77,10.40,12,0.00),
(10257,27,35.10,25,0.00),(10257,39,14.40,6,0.00),(10257,77,10.40,15,0.00),
(10258,2,15.20,50,0.20),(10258,5,17.00,65,0.20),(10258,32,25.60,6,0.20),
(10259,21,8.00,10,0.00),(10259,37,20.80,1,0.00),
(10260,41,7.70,16,0.25),(10260,57,15.60,50,0.00),(10260,62,39.40,15,0.25),(10260,70,12.00,21,0.25),
(10261,21,8.00,20,0.00),(10261,35,14.40,20,0.00),
(10262,5,17.00,12,0.20),(10262,7,24.00,15,0.00),(10262,56,30.40,2,0.00),
(10263,16,13.90,60,0.25),(10263,24,3.60,28,0.00),(10263,30,20.70,60,0.25),(10263,74,8.00,36,0.25),
(10264,2,15.20,35,0.00),(10264,41,7.70,25,0.15),
(10265,17,31.20,30,0.00),(10265,70,12.00,20,0.00),
(10266,12,30.40,12,0.05),
(10267,40,14.70,50,0.00),(10267,59,44.00,70,0.15),(10267,76,14.40,15,0.15),
(10268,29,99.00,10,0.00),(10268,72,27.80,4,0.00),
(10269,33,2.00,60,0.05),(10269,72,27.80,20,0.05),
(10270,36,15.20,30,0.00),(10270,43,36.80,25,0.00),
(10271,33,2.00,24,0.00),
(10272,20,64.80,6,0.00),(10272,31,10.00,40,0.00),(10272,72,27.80,24,0.00),
(10273,10,24.80,24,0.05),(10273,31,10.00,15,0.05),(10273,33,2.00,20,0.00),(10273,40,14.70,60,0.05),(10273,76,14.40,33,0.05),
(10274,71,17.20,20,0.00),(10274,72,27.80,7,0.00),
(10275,24,3.60,12,0.05),(10275,29,99.00,6,0.00),(10275,33,2.00,6,0.00),
(10276,10,24.80,15,0.00),(10276,13,4.80,10,0.00),
(10277,28,36.40,20,0.00),(10277,62,39.40,12,0.00),
(10278,44,15.50,16,0.00),(10278,59,44.00,15,0.00),(10278,63,35.10,8,0.00),(10278,73,12.00,25,0.00),
(10279,17,31.20,15,0.25),(10279,37,20.80,10,0.25),(10279,46,9.60,15,0.25),
(10280,24,3.60,12,0.00),(10280,55,19.20,20,0.00),(10280,75,6.20,30,0.00),
(10281,19,7.30,1,0.00),(10281,24,3.60,6,0.00),(10281,35,14.40,4,0.00),
(10282,30,20.70,6,0.00),(10282,57,15.60,2,0.00),
(10283,15,12.40,20,0.00),(10283,19,7.30,18,0.00),(10283,60,27.20,35,0.00),(10283,72,27.80,3,0.00),
(10284,27,35.10,15,0.25),(10284,44,15.50,21,0.00),(10284,60,27.20,20,0.25),(10284,67,11.20,5,0.25),
(10285,1,14.40,45,0.20),(10285,40,14.70,40,0.20),(10285,53,26.20,36,0.20),
(10286,35,14.40,100,0.00),(10286,62,39.40,40,0.00),
(10287,16,13.90,40,0.15),(10287,34,11.20,20,0.00),(10287,46,9.60,15,0.15),
(10288,54,5.90,10,0.10),(10288,68,10.00,3,0.10),
(10289,3,8.00,30,0.00),(10289,64,26.60,9,0.00),
(10290,5,17.00,20,0.00),(10290,29,99.00,15,0.00),(10290,49,16.00,15,0.00),(10290,77,10.40,10,0.00),
(10291,13,4.80,20,0.10),(10291,44,15.50,24,0.10),(10291,51,42.40,2,0.10),
(10292,20,64.80,20,0.00),(10292,59,44.00,6,0.00),
(10293,18,50.00,12,0.00),(10293,24,3.60,10,0.00),(10293,63,35.10,5,0.00),(10293,75,6.20,6,0.00),
(10294,1,14.40,18,0.00),(10294,17,31.20,15,0.00),(10294,43,36.80,15,0.00),(10294,60,27.20,21,0.00),(10294,75,6.20,6,0.00),
(10295,56,30.40,4,0.00),(10295,62,39.40,8,0.00),
(10296,11,16.80,12,0.00),(10296,16,13.90,30,0.00),(10296,69,28.80,15,0.00),
(10297,39,14.40,60,0.00),(10297,72,27.80,20,0.00),
(10298,2,15.20,40,0.00),(10298,36,15.20,40,0.25),(10298,59,44.00,30,0.25),(10298,62,39.40,15,0.00),(10298,70,12.00,15,0.25),
(10299,19,7.30,15,0.00),(10299,70,12.00,20,0.00),
(10300,66,13.60,30,0.00),(10300,68,10.00,20,0.00),
(10301,40,14.70,10,0.00),(10301,56,30.40,20,0.00),
(10302,17,31.20,40,0.00),(10302,28,36.40,28,0.00),(10302,43,36.80,12,0.00),
(10303,40,14.70,40,0.10),(10303,65,16.80,30,0.10),(10303,68,10.00,15,0.10),
(10304,49,16.00,30,0.00),(10304,59,44.00,10,0.00),(10304,71,17.20,2,0.00),
(10305,18,50.00,25,0.10),(10305,29,99.00,25,0.10),(10305,39,14.40,30,0.10),
(10306,30,20.70,10,0.00),(10306,53,26.20,10,0.00),(10306,54,5.90,5,0.00),
(10307,62,39.40,10,0.00),(10307,68,10.00,3,0.00),
(10308,69,28.80,1,0.00),(10308,70,12.00,5,0.00),
(10309,4,17.60,20,0.00),(10309,6,20.00,30,0.00),(10309,42,9.80,2,0.00),(10309,43,36.80,20,0.00),(10309,71,17.20,3,0.00),
(10310,16,13.90,10,0.00),(10310,62,39.40,5,0.00),
(10311,42,9.80,6,0.00),(10311,69,28.80,7,0.00),
(10312,28,36.40,4,0.00),(10312,43,36.80,24,0.00),(10312,53,26.20,20,0.00),(10312,75,6.20,10,0.00),
(10313,36,15.20,12,0.00),
(10314,32,25.60,40,0.10),(10314,58,10.60,30,0.10),(10314,62,39.40,25,0.10),
(10315,33,2.00,14,0.00),(10315,35,14.40,14,0.00),
(10316,41,7.70,10,0.00),(10316,62,39.40,70,0.00),
(10317,1,14.40,20,0.00),
(10318,41,7.70,20,0.00),(10318,76,14.40,6,0.00),
(10319,17,31.20,8,0.00),(10319,28,36.40,14,0.00),(10319,43,36.80,60,0.00),
(10320,71,17.20,30,0.00),
(10321,35,14.40,10,0.00),
(10322,52,5.60,20,0.20),
(10323,15,12.40,5,0.00),(10323,25,11.20,4,0.00),(10323,39,14.40,4,0.00),
(10324,16,13.90,21,0.10),(10324,35,14.40,70,0.10),(10324,46,9.60,30,0.00),(10324,59,44.00,40,0.10),(10324,63,35.10,80,0.10),
(10325,6,20.00,6,0.00),(10325,13,4.80,12,0.00),(10325,14,18.60,9,0.00),(10325,31,10.00,4,0.00),(10325,72,27.80,40,0.00),
(10326,4,17.60,24,0.00),(10326,57,15.60,16,0.00),(10326,75,6.20,50,0.00),
(10327,2,15.20,25,0.20),(10327,11,16.80,50,0.20),(10327,30,20.70,35,0.20),(10327,58,10.60,30,0.20),
(10328,59,44.00,9,0.00),(10328,65,16.80,40,0.00),(10328,68,10.00,10,0.00),
(10329,19,7.30,10,0.05),(10329,30,20.70,8,0.05),(10329,38,210.80,20,0.05),(10329,56,30.40,12,0.05),(10329,59,44.00,25,0.05),
(10330,26,24.90,50,0.15),(10330,72,27.80,25,0.15),
(10331,54,5.90,15,0.00),
(10332,18,50.00,40,0.20),(10332,42,9.80,10,0.20),(10332,47,7.60,16,0.20),
(10333,14,18.60,10,0.00),(10333,21,8.00,10,0.10),(10333,71,17.20,40,0.10),
(10334,52,5.60,8,0.00),(10334,68,10.00,10,0.00),
(10335,2,15.20,7,0.20),(10335,31,10.00,25,0.20),(10335,32,25.60,6,0.20),(10335,51,42.40,48,0.20),
(10336,4,17.60,18,0.20),
(10337,23,7.20,40,0.00),(10337,26,24.90,24,0.00),(10337,36,15.20,20,0.00),(10337,37,20.80,28,0.00),(10337,69,28.80,25,0.00),
(10338,17,31.20,20,0.00),(10338,30,20.70,15,0.00),
(10339,4,17.60,10,0.00),(10339,17,31.20,70,0.05),(10339,62,39.40,28,0.00),
(10340,18,50.00,20,0.05),(10340,41,7.70,12,0.05),(10340,43,36.80,40,0.05),
(10341,33,2.00,8,0.00),(10341,59,44.00,9,0.15),
(10342,2,15.20,24,0.20),(10342,31,10.00,56,0.20),(10342,36,15.20,40,0.20),(10342,55,19.20,40,0.20),(10342,59,44.00,32,0.20),
(10343,64,26.60,50,0.00),(10343,68,10.00,4,0.05),(10343,76,14.40,15,0.00),
(10344,4,17.60,35,0.00),(10344,8,32.00,70,0.25),
(10345,8,32.00,70,0.00),(10345,19,7.30,80,0.00),(10345,42,9.80,9,0.00),
(10346,17,31.20,36,0.10),(10346,56,30.40,20,0.00),
(10347,25,11.20,10,0.00),(10347,59,44.00,10,0.00),
(10348,1,14.40,15,0.15),(10348,23,7.20,25,0.00),
(10349,54,5.90,24,0.00),
(10350,50,13.00,15,0.10),(10350,69,28.80,18,0.10),
(10351,38,210.80,20,0.05),(10351,41,7.70,13,0.05),(10351,44,15.50,77,0.05),(10351,65,16.80,10,0.05),
(10352,24,3.60,10,0.00),(10352,54,5.90,20,0.15),
(10353,11,16.80,12,0.20),(10353,38,210.80,50,0.20),
(10354,1,14.40,12,0.00),(10354,29,99.00,4,0.00),
(10355,24,3.60,25,0.00),(10355,57,15.60,25,0.00),
(10356,31,10.00,30,0.00),(10356,55,19.20,12,0.00),(10356,69,28.80,20,0.00),
(10357,10,24.80,30,0.20),(10357,26,24.90,16,0.00),(10357,60,27.20,8,0.20),
(10358,24,3.60,10,0.05),(10358,34,11.20,10,0.05),(10358,36,15.20,20,0.05),
(10359,16,13.90,56,0.05),(10359,31,10.00,70,0.05),(10359,60,27.20,80,0.05),
(10360,28,36.40,30,0.00),(10360,29,99.00,35,0.00),(10360,38,210.80,10,0.00),(10360,49,16.00,35,0.00),(10360,54,5.90,28,0.00),
(10361,39,14.40,54,0.10),(10361,60,27.20,55,0.10),
(10362,25,11.20,50,0.00),(10362,51,42.40,20,0.00),(10362,54,5.90,24,0.00),
(10363,31,10.00,20,0.00),(10363,75,6.20,12,0.00),(10363,76,14.40,12,0.00),
(10364,69,28.80,30,0.00),(10364,71,17.20,5,0.00),
(10365,11,16.80,24,0.00),
(10366,65,16.80,5,0.00),(10366,77,10.40,5,0.00),
(10367,34,11.20,36,0.00),(10367,54,5.90,18,0.00),(10367,65,16.80,15,0.00),(10367,77,10.40,7,0.00),
(10368,21,8.00,5,0.10),(10368,28,36.40,13,0.10),(10368,57,15.60,25,0.00),(10368,64,26.60,35,0.10),
(10369,29,99.00,20,0.00),(10369,56,30.40,18,0.25),
(10370,1,14.40,15,0.15),(10370,64,26.60,30,0.00),(10370,74,8.00,20,0.15),
(10371,36,15.20,6,0.20),
(10372,20,64.80,12,0.25),(10372,38,210.80,40,0.25),(10372,60,27.20,70,0.25),(10372,72,27.80,42,0.25),
(10373,58,10.60,80,0.20),(10373,71,17.20,50,0.20),
(10374,31,10.00,30,0.00),(10374,37,20.80,15,0.00),
(10375,14,18.60,15,0.00),(10375,54,5.90,10,0.00),
(10376,31,10.00,42,0.05),
(10377,28,36.40,20,0.15),(10377,39,14.40,20,0.15),
(10378,71,17.20,6,0.00),
(10379,41,7.70,8,0.00),(10379,63,35.10,16,0.00),(10379,65,16.80,20,0.00),
(10380,30,20.70,18,0.10),(10380,53,26.20,20,0.10),(10380,60,27.20,6,0.10),(10380,70,12.00,30,0.00),
(10381,74,8.00,14,0.00),
(10382,5,17.00,32,0.00),(10382,18,50.00,9,0.00),(10382,29,99.00,14,0.00),(10382,33,2.00,60,0.00),(10382,74,8.00,50,0.00),
(10383,13,4.80,20,0.00),(10383,50,13.00,15,0.00),(10383,56,30.40,20,0.00),
(10384,20,64.80,28,0.00),(10384,60,27.20,15,0.00),
(10385,7,24.00,10,0.20),(10385,60,27.20,20,0.20),(10385,68,10.00,8,0.20),
(10386,24,3.60,15,0.00),(10386,34,11.20,10,0.00),
(10387,24,3.60,15,0.00),(10387,28,36.40,6,0.00),(10387,59,44.00,12,0.00),(10387,71,17.20,15,0.00),
(10388,45,7.60,15,0.20),(10388,52,5.60,20,0.20),(10388,53,26.20,40,0.00),
(10389,10,24.80,16,0.00),(10389,55,19.20,15,0.00),(10389,62,39.40,20,0.00),(10389,70,12.00,20,0.00),
(10390,31,10.00,60,0.10),(10390,35,14.40,40,0.10),(10390,46,9.60,45,0.00),(10390,72,27.80,24,0.10),
(10391,13,4.80,18,0.00),
(10392,69,28.80,50,0.00),
(10393,2,15.20,25,0.25),(10393,14,18.60,42,0.25),(10393,25,11.20,7,0.25),(10393,26,24.90,70,0.25),(10393,31,10.00,32,0.00),
(10394,13,4.80,10,0.00),(10394,62,39.40,10,0.00),
(10395,46,9.60,28,0.10),(10395,53,26.20,70,0.10),(10395,69,28.80,8,0.00),
(10396,23,7.20,40,0.00),(10396,71,17.20,60,0.00),(10396,72,27.80,21,0.00),
(10397,21,8.00,10,0.15),(10397,51,42.40,18,0.15),
(10398,35,14.40,30,0.00),(10398,55,19.20,120,0.10),
(10399,68,10.00,60,0.00),(10399,71,17.20,30,0.00),(10399,76,14.40,35,0.00),(10399,77,10.40,14,0.00),
(10400,29,99.00,21,0.00),(10400,35,14.40,35,0.00),(10400,49,16.00,30,0.00),
(10401,30,20.70,18,0.00),(10401,56,30.40,70,0.00),
(10402,23,7.20,60,0.00),(10402,63,35.10,65,0.00),
(10403,16,13.90,21,0.15),(10403,48,10.20,70,0.15),
(10404,26,24.90,30,0.05),(10404,42,9.80,40,0.05),(10404,49,16.00,30,0.05),
(10405,3,8.00,50,0.00),
(10406,1,14.40,10,0.00),(10406,21,8.00,30,0.10),(10406,28,36.40,42,0.10),(10406,36,15.20,5,0.10),(10406,40,14.70,2,0.10),
(10407,11,16.80,30,0.00),(10407,69,28.80,15,0.00),(10407,71,17.20,15,0.00),
(10408,37,20.80,10,0.00),(10408,54,5.90,6,0.00),(10408,62,39.40,35,0.00),
(10409,14,18.60,12,0.00),(10409,21,8.00,12,0.00),
(10410,33,2.00,49,0.00),(10410,59,44.00,16,0.00),
(10411,41,7.70,25,0.20),(10411,44,15.50,40,0.20),(10411,59,44.00,9,0.20),
(10412,14,18.60,20,0.10),
(10413,1,14.40,24,0.00),(10413,62,39.40,40,0.00),(10413,76,14.40,14,0.00),
(10414,19,7.30,18,0.05),(10414,33,2.00,50,0.00),
(10415,17,31.20,2,0.00),(10415,33,2.00,20,0.00),
(10416,19,7.30,20,0.00),(10416,53,26.20,10,0.00),(10416,57,15.60,20,0.00),
(10417,38,210.80,50,0.00),(10417,46,9.60,2,0.25),(10417,68,10.00,36,0.25),(10417,77,10.40,35,0.00),
(10418,2,15.20,60,0.00),(10418,47,7.60,55,0.00),(10418,61,22.80,16,0.00),(10418,74,8.00,15,0.00),
(10419,60,27.20,60,0.05),(10419,69,28.80,20,0.05),
(10420,9,77.60,20,0.10),(10420,13,4.80,2,0.10),(10420,70,12.00,8,0.10),(10420,73,12.00,20,0.10),
(10421,19,7.30,4,0.15),(10421,26,24.90,30,0.00),(10421,53,26.20,15,0.15),(10421,77,10.40,10,0.15),
(10422,26,24.90,2,0.00),
(10423,31,10.00,14,0.00),(10423,59,44.00,20,0.00),
(10424,35,14.40,60,0.20),(10424,38,210.80,49,0.20),(10424,68,10.00,30,0.20),
(10425,55,19.20,10,0.25),(10425,76,14.40,20,0.25),
(10426,56,30.40,5,0.00),(10426,64,26.60,7,0.00),
(10427,14,18.60,35,0.00),
(10428,46,9.60,20,0.00),
(10429,50,13.00,40,0.00),(10429,63,35.10,35,0.25),
(10430,17,31.20,30,0.20),(10430,21,8.00,20,0.00),(10430,56,30.40,40,0.20),(10430,59,44.00,35,0.20),
(10431,17,31.20,50,0.25),(10431,40,14.70,50,0.25),(10431,47,7.60,30,0.25),
(10432,26,24.90,10,0.00),(10432,54,5.90,40,0.00),
(10433,56,30.40,28,0.00),
(10434,11,16.80,6,0.00),(10434,76,14.40,18,0.15),
(10435,2,15.20,10,0.00),(10435,22,16.80,12,0.00),(10435,72,27.80,10,0.00),
(10436,46,9.60,5,0.00),(10436,56,30.40,40,0.10),(10436,64,26.60,30,0.10),(10436,75,6.20,24,0.10),
(10437,32,25.60,15,0.00),
(10438,19,7.30,15,0.20),(10438,34,11.20,20,0.20),(10438,57,15.60,15,0.20),
(10439,7,24.00,4,0.00),(10439,16,13.90,4,0.00),(10439,62,39.40,14,0.00),
(10440,2,15.20,45,0.15),(10440,16,13.90,49,0.05),(10440,29,99.00,24,0.15),(10440,61,22.80,90,0.15),
(10441,27,35.10,50,0.00),
(10442,11,16.80,30,0.00),(10442,54,5.90,80,0.00),(10442,66,13.60,60,0.00),
(10443,11,16.80,6,0.20),(10443,28,36.40,12,0.00),
(10444,17,31.20,10,0.00),(10444,26,24.90,15,0.00),(10444,35,14.40,8,0.00),
(10445,39,14.40,6,0.00),(10445,54,5.90,15,0.00),
(10446,19,7.30,12,0.10),(10446,24,3.60,20,0.00),(10446,31,10.00,3,0.10),(10446,72,27.80,40,0.10),
(10447,19,7.30,40,0.00),(10447,65,16.80,35,0.00),(10447,71,17.20,2,0.00),
(10448,26,24.90,6,0.00),(10448,40,14.70,20,0.00),
(10449,10,24.80,14,0.00),(10449,52,5.60,20,0.00),(10449,62,39.40,35,0.00),
(10450,10,24.80,20,0.20),(10450,54,5.90,6,0.25),
(10451,55,19.20,120,0.10),(10451,64,26.60,35,0.10),(10451,65,16.80,28,0.10),(10451,77,10.40,55,0.10),
(10452,28,36.40,15,0.00),(10452,44,15.50,100,0.05),
(10453,48,10.20,15,0.10),(10453,70,12.00,25,0.10),
(10454,16,13.90,20,0.00),(10454,33,2.00,20,0.00),(10454,46,9.60,10,0.00),
(10455,39,14.40,20,0.00),(10455,53,26.20,50,0.00),(10455,61,22.80,26,0.00),(10455,71,17.20,30,0.00),
(10456,21,8.00,40,0.15),(10456,49,16.00,21,0.15),
(10457,59,44.00,36,0.00),
(10458,26,24.90,15,0.00),(10458,28,36.40,5,0.00),(10458,43,36.80,20,0.00),(10458,56,30.40,14,0.00),(10458,71,17.20,30,0.00),
(10459,7,24.00,16,0.05),(10459,46,9.60,20,0.05),(10459,72,27.80,40,0.00),
(10460,68,10.00,21,0.25),(10460,75,6.20,4,0.25),
(10461,21,8.00,40,0.25),(10461,30,20.70,28,0.25),(10461,55,19.20,60,0.25),
(10462,13,4.80,1,0.00),(10462,23,7.20,21,0.00),
(10463,19,7.30,21,0.00),(10463,42,9.80,50,0.00),
(10464,4,17.60,16,0.20),(10464,43,36.80,3,0.00),(10464,56,30.40,30,0.20),(10464,60,27.20,20,0.00),
(10465,24,3.60,25,0.00),(10465,29,99.00,18,0.10),(10465,40,14.70,20,0.00),(10465,45,7.60,30,0.10),(10465,50,13.00,25,0.00),
(10466,11,16.80,10,0.00),(10466,33,2.00,10,0.00),
(10467,24,3.60,28,0.00),(10467,25,11.20,12,0.00),
(10468,30,20.70,8,0.00),(10468,43,36.80,15,0.00),
(10469,2,15.20,40,0.15),(10469,16,13.90,35,0.15),(10469,44,15.50,2,0.00),
(10470,18,50.00,30,0.00),(10470,23,7.20,15,0.00),(10470,64,26.60,8,0.00),
(10471,7,24.00,30,0.00),(10471,56,30.40,20,0.00),
(10472,24,3.60,80,0.05),(10472,51,42.40,18,0.05),(10472,54,5.90,70,0.00),(10472,69,28.80,12,0.05),
(10473,33,2.00,12,0.00),(10473,71,17.20,12,0.00),
(10474,14,18.60,12,0.00),(10474,28,36.40,18,0.00),(10474,40,14.70,21,0.00),(10474,75,6.20,10,0.00),
(10475,31,10.00,35,0.15),(10475,66,13.60,60,0.15),(10475,76,14.40,42,0.15),
(10476,55,19.20,2,0.05),(10476,70,12.00,12,0.00),
(10477,1,14.40,15,0.00),(10477,21,8.00,21,0.25),(10477,39,14.40,20,0.25),
(10478,10,24.80,20,0.05),
(10479,38,210.80,30,0.00),(10479,53,26.20,28,0.00),(10479,59,44.00,60,0.00),(10479,64,26.60,30,0.00),(10479,71,17.20,120,0.00),
(10480,47,7.60,30,0.00),(10480,59,44.00,12,0.00),
(10481,49,16.00,24,0.00),(10481,60,27.20,40,0.00),
(10482,40,14.70,10,0.00),
(10483,34,11.20,35,0.05),(10483,77,10.40,30,0.05),
(10484,21,8.00,14,0.00),(10484,40,14.70,10,0.00),(10484,51,42.40,3,0.00),
(10485,2,15.20,20,0.10),(10485,3,8.00,20,0.10),(10485,55,19.20,30,0.10),(10485,70,12.00,60,0.10),
(10486,11,16.80,5,0.00),(10486,51,42.40,25,0.00),(10486,74,8.00,16,0.00),
(10487,19,7.30,5,0.00),(10487,26,24.90,30,0.00),(10487,54,5.90,24,0.25),
(10488,59,44.00,30,0.10),(10488,73,12.00,20,0.10),
(10489,11,16.80,15,0.25),(10489,16,13.90,18,0.00),
(10490,59,44.00,60,0.00),(10490,68,10.00,30,0.00),(10490,75,6.20,36,0.00),
(10491,44,15.50,15,0.15),(10491,77,10.40,7,0.15),
(10492,25,11.20,60,0.05),(10492,42,9.80,20,0.05),
(10493,65,16.80,15,0.10),(10493,66,13.60,10,0.10),(10493,69,28.80,10,0.10),
(10494,56,30.40,30,0.00),
(10495,23,7.20,10,0.00),(10495,41,7.70,20,0.00),(10495,77,10.40,5,0.00),
(10496,31,10.00,20,0.05),
(10497,56,30.40,14,0.00),(10497,72,27.80,25,0.00),
(10498,24,3.60,14,0.00),(10498,40,14.70,5,0.00),(10498,42,9.80,30,0.00),
(10499,28,36.40,20,0.00),(10499,49,16.00,25,0.00),
(10500,15,12.40,12,0.05),(10500,28,36.40,8,0.05);
COMMIT;

-- =============================================================================
-- VERIFICACIÓN: Consultas de prueba para validar la base de datos
-- =============================================================================

-- 1. Total de registros por tabla
SELECT 'Categories'   AS Tabla, COUNT(*) AS Registros FROM Categories   UNION ALL
SELECT 'Suppliers',   COUNT(*) FROM Suppliers   UNION ALL
SELECT 'Shippers',    COUNT(*) FROM Shippers    UNION ALL
SELECT 'Employees',   COUNT(*) FROM Employees   UNION ALL
SELECT 'Customers',   COUNT(*) FROM Customers   UNION ALL
SELECT 'Products',    COUNT(*) FROM Products    UNION ALL
SELECT 'Orders',      COUNT(*) FROM Orders      UNION ALL
SELECT 'OrderDetails',COUNT(*) FROM OrderDetails;

-- 2. Revenue total (con y sin descuento) — prueba la corrección principal
SELECT
  ROUND(SUM(UnitPrice * Quantity), 2)              AS RevenueGruto,
  ROUND(SUM(UnitPrice * Quantity * Discount), 2)   AS TotalDescuentos,
  ROUND(SUM(UnitPrice * Quantity * (1-Discount)),2) AS RevenueNeto
FROM OrderDetails;

-- 3. Productos que necesitan reabastecimiento
SELECT ProductName, UnitsInStock, UnitsOnOrder, ReorderLevel
FROM Products
WHERE (UnitsInStock + UnitsOnOrder) <= ReorderLevel
  AND Discontinued = 0
ORDER BY UnitsInStock;

-- 4. Pedidos con demora (llegaron después de la RequiredDate)
SELECT OrderID, OrderDate, RequiredDate, ShippedDate,
       DATEDIFF(ShippedDate, RequiredDate) AS DiasRetraso
FROM Orders
WHERE ShippedDate > RequiredDate
ORDER BY DiasRetraso DESC;

-- 5. Vista de desempeño de empleados
SELECT * FROM v_EmployeePerformance ORDER BY TotalRevenue DESC;