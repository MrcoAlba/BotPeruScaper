from support.FileMaker                         import GetFileNames
from support.Write                             import append_to_csv
from request.DataTransformation.FileManagement import CleanFiles, DeleteFiles
from request.Petition                          import RequestData
from request.DataTransformation.Decompress     import Decompress
from request.DataTransformation.CastFile       import CastJSONtoCSV
from webScripting.BPWebScript                  import WebScriptBP
from response.DataExport                       import ExportData
import traceback

def main():
    webService1    = "http://34.193.40.144/ws/Servicios/svc_ResultadoBusqueda.svc/ResultadoBusqueda_GetAll_Elegido"
    webService2    = "http://34.193.40.144/ws/Servicios/svc_VariacionPrecio.svc/VariacionPrecio_Insertar"
    file_names     = GetFileNames()
    id_competencia = 19
    sleep_time     = 5
    
    append_to_csv(file_names[1],"El bot ha iniciado")
    
    try:
        CleanFiles([file_names[2],file_names[3],file_names[4],file_names[6]])
        if RequestData(webService1, file_names[2]):
            if Decompress(file_names[2], file_names[3]):
                if CastJSONtoCSV(file_names[3],file_names[4], id_competencia):
                    if WebScriptBP(file_names[4], sleep_time,file_names[6],file_names[0]):
                        if ExportData(webService2,file_names[6],file_names[0]):
                            print("FIN")
                    else: append_to_csv(file_names[0],"web service error")
                else: append_to_csv(file_names[0],"La respuesta del servidor no ha podido ser casteada de json a csv o hubo un error en la petición")
            else: append_to_csv(file_names[0],"La respuesta del servidor no ha podido ser descomprimida")
        else: append_to_csv(file_names[0],"La petición GET del WebService1 ha fallado")
        DeleteFiles([file_names[2],file_names[3]])

    except Exception as e:
        append_to_csv(file_names[0],traceback.format_exc())
    
    append_to_csv(file_names[1],"El bot ha finalizado")

if __name__ == "__main__":
    main()


    