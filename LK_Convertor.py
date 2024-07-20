import os
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString

yaml = YAML()
yaml.default_flow_style = False
yaml.indent(sequence=4, offset=2)

def write_yml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def main_menu():
    print("Preconfiguración de archivo .yml")
    
    # Preguntar por el nombre del archivo .yml al inicio
    file_name = input("Ingrese el nombre del archivo (sin extensión .yml): ") + ".yml"
    
    estructura = input("Elija la estructura ('Oraxen' o 'IA'): ").strip().lower()
    
    namespace = "lk"
    configuraciones = {}
    if estructura == 'ia':
        namespace = input("Ingrese la palabra que desea agregar al namespace: ")
        configuraciones = {
            'info': {
                'namespace': namespace
            },
            'items': {}
        }

    directory_path = os.getcwd()
    archivos = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    material = input("Ingrese el material para todos los ítems: ").upper()
    custom_model_data = 1780  
    
    for i, archivo in enumerate(archivos):
        print(f"\nIteración {i + 1}")
        nombre = os.path.splitext(archivo)[0]  
        nombre_formateado = ' '.join(word.capitalize() for word in nombre.split('_'))  
        
        if estructura == 'oraxen':
            configuraciones[nombre] = {
                'displayname': DoubleQuotedScalarString(f'<white>{nombre_formateado}'),
                'material': material,
                'Pack': {
                    'generate_model': True,
                    'parent_model': DoubleQuotedScalarString("item/handheld"),
                    'custom_model_data': custom_model_data,
                    'textures': [f'item/{nombre}']
                }
            }
        elif estructura == 'ia':
            configuraciones['items'][nombre] = {
                'display_name': DoubleQuotedScalarString(nombre_formateado),
                'resource': {
                    'material': material,
                    'generate': True,
                    'model_id': custom_model_data,
                    'textures': [f'item/{nombre}']
                }
            }
        
        custom_model_data += 1  
    
    return configuraciones, file_name

def generate_yml():
    configuraciones, file_name = main_menu()

    file_path = os.path.join(os.getcwd(), file_name)

    write_yml(file_path, configuraciones)
    
    print(f"Archivo {file_path} generado con éxito.")

generate_yml()
