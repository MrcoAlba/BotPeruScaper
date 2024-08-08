from request.DataTransformation.RequestModels import RequestClass, RequestProduct
import json
import csv

def ExportLine(data, file_name):
    with open(file_name, 'a', encoding='UTF8') as f:
        writer = csv.writer(f,delimiter='|')
        writer.writerow(data)
        f.close()

def CastJSONtoCSV(file_path, output_filename, competenciaID):
    # Read the JSON data from the file
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    # Parse the JSON data into instances of the defined classes
    json_response  = RequestClass(
        HuboError  = json_data['HuboError'],
        ErrorCode  = json_data['ErrorCode'],
        ErrorMsj   = json_data['ErrorMsj'],
        SuccessMsj = json_data['SuccessMsj'],
        obj = [
            RequestProduct(
                idResultadoBusqueda = result_data['idResultadoBusqueda'],
                idProducto          = result_data['idProducto'],
                idCompetencia       = result_data['idCompetencia'],
                Descripcion         = result_data['Descripcion'],
                URL                 = result_data['URL'],
                SKU                 = result_data['SKU']
                ) for result_data in json_data['obj']
            ]
    )

    # Check any error on petition
    if json_response.HuboError == True or json_response.ErrorCode != "0" or json_response.ErrorMsj != None:
        return False
    # Accessing data from the first RequestProduct instance
    try:
        for object in json_response.obj:
            if (object.idCompetencia == competenciaID):
                data = []
                data.append(object.idResultadoBusqueda)
                data.append(object.idProducto)
                data.append(object.idCompetencia)
                data.append(object.Descripcion)
                data.append(object.URL)
                data.append(object.SKU)
                ExportLine(data, output_filename)
        return True
    except Exception as e:
        return False
