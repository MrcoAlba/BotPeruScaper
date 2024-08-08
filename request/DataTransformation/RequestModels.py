from typing import Optional, List

class RequestProduct:
    def __init__(
        self                    ,
        idResultadoBusqueda: int,
        idProducto         : int,
        idCompetencia      : int,
        Descripcion        : str,
        URL                : str,
        SKU                : str                 
    ):
        self.idResultadoBusqueda = idResultadoBusqueda
        self.idProducto          = idProducto
        self.idCompetencia       = idCompetencia
        self.Descripcion         = Descripcion
        self.URL                 = URL
        self.SKU                 = SKU

class RequestClass:
    def __init__(
        self                     ,
        HuboError : bool         ,
        ErrorCode : str          ,
        ErrorMsj  : Optional[str],
        SuccessMsj: Optional[str],
        obj       : List[RequestProduct]
    ):
        self.HuboError  = HuboError
        self.ErrorCode  = ErrorCode
        self.ErrorMsj   = ErrorMsj
        self.SuccessMsj = SuccessMsj
        self.obj        = obj