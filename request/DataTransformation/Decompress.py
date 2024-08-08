import gzip
import base64
import json
from datetime import datetime

def Decompress(file_path, output_filename):
    with open(file_path, "r") as file:
        compressed_data = file.read()
    try:
        # Decode from base64
        compressed_bytes = base64.b64decode(compressed_data)

        # Decompress using gzip
        decompressed_data = gzip.decompress(compressed_bytes)

        # Deserialize JSON
        json_data = decompressed_data.decode('utf-8')
        result = json.loads(json_data)

        if result:
            with open(output_filename, 'w') as output_file:
                json.dump(result, output_file, default=lambda o: o.__dict__, indent=4)

        return True

    except Exception as e:
        return False