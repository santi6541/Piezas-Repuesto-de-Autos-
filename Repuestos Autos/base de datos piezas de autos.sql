-- Crear la base de datos si no existe (opcional, si ya existe no es necesario)
CREATE DATABASE IF NOT EXISTS taller_repuestos;
USE taller_repuestos;

-- Tabla de Productos 
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    stock VARCHAR(255), 
    marca VARCHAR(100),
    codigo_barras VARCHAR(255) UNIQUE, 
    categoria VARCHAR(100),
    unidad_medida VARCHAR(50),
    precio_fabrica VARCHAR(255),
    precio_tienda VARCHAR(255) 
);

-- Insertar datos 
INSERT INTO productos (nombre, descripcion, stock, marca, codigo_barras, categoria, unidad_medida, precio_fabrica, precio_tienda) VALUES
('Bujía de Encendido NGK BKR6E', 'Bujía estándar para motores de gasolina', '150', 'NGK', '0087295142214', 'Encendido', 'pieza', 50.00, '100.00'),
('Filtro de Aceite Bosch 0451103375', 'Filtro de aceite para motor', '100', 'Bosch', '4047025248129', 'Filtros', 'pieza', 80.00, '150.00'),
('Aceite de Motor Castrol GTX 20W-50 (4 Litros)', 'Aceite multigrado para motores a gasolina', '50', 'Castrol', '0003700812345', 'Lubricantes', 'litro', 200.00, '300.00'),
('Filtro de Aire Mann-Filter C 27 130', 'Filtro de aire para motor', '80', 'Mann-Filter', '4011558721009', 'Filtros', 'pieza', 65.00, '120.00'),
('Batería LTH L-42-400', 'Batería de automóvil, 400 CCA', '30', 'LTH', '7501035000001', 'Baterías', 'pieza', 900.00, '1400.00'),
('Llanta Michelin Energy XM2+ 185/65 R15', 'Llanta para automóvil, alta durabilidad', '60', 'Michelin', '3528707177808', 'Llantas', 'pieza', 1100.00, '1700.00'),
('Amortiguador Delantero Monroe 71341', 'Amortiguador delantero para suspensión', '40', 'Monroe', '037606713419', 'Suspensión', 'pieza', 600.00, '950.00'),
('Banda de Tiempo Gates 5489XS', 'Banda de distribución para motor', '70', 'Gates', '072053548900', 'Motor', 'pieza', 220.00, '400.00'),
('Anticongelante Prestone Concentrado (1 Litro)', 'Refrigerante para motor, concentrado', '90', 'Prestone', '079635098765', 'Fluidos', 'litro', 60.00, '100.00'),
('Balatas Delanteras Brembo P 85 020', 'Pastillas de freno delanteras', '55', 'Brembo', '8020584000201', 'Frenos', 'juego', 320.00, '500.00'),
('Bomba de Agua Bosch 0120489278', 'Bomba de agua para sistema de enfriamiento', '35', 'Bosch', '3165143123456', 'Enfriamiento', 'pieza', 480.00, '750.00'),
('Radiador Denso DRM-4001', 'Radiador de aluminio', '25', 'Denso', '014390400100', 'Enfriamiento', 'pieza', 800.00, '1300.00'),
('Faro Delantero Izquierdo TYC 20-6789-A', 'Faro delantero izquierdo', '15', 'TYC', '762405678912', 'Iluminación', 'pieza', 650.00, '1000.00'),
('Filtro de Gasolina Mahle KL 581', 'Filtro de combustible', '65', 'Mahle', '4009026581007', 'Filtros', 'pieza', 80.00, '130.00'),
('Sensor de Oxígeno NTK 90001', 'Sensor de oxígeno, sonda lambda', '45', 'NTK', '025900900012', 'Sensores', 'pieza', 270.00, '420.00');
