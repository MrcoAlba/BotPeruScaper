import csv
import json
import requests
import traceback
from support.Write import append_to_csv

class Product:
    def __init__(
        self,
        idProducto         : int,
        idCompetencia      : int,
        idResultadoBusqueda: int,
        Precio             : float,
        PrecioOferta       : float,
        PrecioTarjeta      : float,
        FechaRegistroS     : str
    ):
        self.idResultadoBusqueda = idResultadoBusqueda
        self.idProducto          = idProducto
        self.idCompetencia       = idCompetencia
        self.Precio              = Precio
        self.PrecioOferta        = PrecioOferta
        self.PrecioTarjeta       = PrecioTarjeta
        self.FechaRegistroS      = FechaRegistroS
    
    def to_json(self):
        # Convert the Product instance to a JSON-formatted string
        return json.dumps(self.__dict__)

def ExportData(url, file_export, file_error):
    # Read products from CSV file
    try:
        with open(file_export, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for fila in reader:
                product_temp = fila[0].split("|")
                product = Product(
                    int(    product_temp[2]),
                    int(    product_temp[3]),
                    int(    product_temp[1]),
                    float(  product_temp[4]),
                    float(  product_temp[5]),
                    float(  product_temp[6]),
                    str(    product_temp[7])
                )
                json_data = product.to_json()

                print(json_data)
                # # Send the JSON data to the web service
                # response = requests.post(url, json=json.loads(json_data))

                # # Check the response status
                # if response.status_code == 200:
                #     print(f"Product sent successfully: {json_data}")
                # else:
                #     print(f"Failed to send product. Status code: {response.status_code}, Response content: {response.content}")
                

        return True
    
    except Exception as e:
        append_to_csv(file_error,traceback.format_exc())