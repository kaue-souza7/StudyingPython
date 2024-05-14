# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma ser
# classe "callable".


from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, *args, **kwargs):
        return f'Discando number... {self.phone}'
    
call1 = CallMe('11 9 97841558')
print(call1())