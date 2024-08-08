class Product:
    def __init__(
        self,
        description        : str,
        idResultadoBusqueda: int,
        idProducto         : int,
        idCompetencia      : int,
        Precio             : float,
        PrecioOferta       : float,
        PrecioTarjeta      : float,
        FechaRegistroS     : str
    ):
        self.description         = description
        self.idResultadoBusqueda = idResultadoBusqueda
        self.idProducto          = idProducto
        self.idCompetencia       = idCompetencia
        self.Precio              = Precio
        self.PrecioOferta        = PrecioOferta
        self.PrecioTarjeta       = PrecioTarjeta
        self.FechaRegistroS      = FechaRegistroS
    
    def __str__(self):
        # Convert all properties to a string and concatenate them
        return f"Product(A={self.idResultadoBusqueda}, B={self.idProducto}, C={self.idCompetencia}, D1={self.Precio}, D2={self.PrecioOferta}, D3={self.PrecioTarjeta}, E={self.FechaRegistroS})"