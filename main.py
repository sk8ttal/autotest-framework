import os
import importlib
import time


def main():
    folder_path = 'TestCases/Registration'
    module_prefix = folder_path.replace('/', '.')

    modules = [f[:-3]
               for f in os.listdir(folder_path) if f.endswith('.py') and f != '__init__.py']
    cases = []

    for module_name in modules:
        module = importlib.import_module(f"{module_prefix}.{module_name}")
        module_name = module_name[0].upper() + module_name[1:]
        class_ = getattr(module, module_name)

        cases.append(class_)

    for case in cases:
        print("Запуск кейса " + case.__name__)
        case().main()
        print()
        time.sleep(1)

main()
