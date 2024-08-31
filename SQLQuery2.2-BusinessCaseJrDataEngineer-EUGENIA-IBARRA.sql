SELECT SUM(Venta) AS "Sales", MONTH(Fecha_Venta) AS "Month", YEAR(Fecha_Venta) AS "Year" FROM [BusinessCaseJrDataEngineerSales-EUGENIA-IBARRA] 
	GROUP BY MONTH(Fecha_Venta), YEAR(Fecha_Venta)