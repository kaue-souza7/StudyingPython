# ABSTRAÇÃO
# Heranca = é um
# LOG
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('implemente o metodo LOG')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = (f'{msg} LogFile MIXIN')
        print()
        print('Salvando no LOG: ', msg_formatada)
        with open(LOG_FILE, 'a', encoding="utf8") as arquivo:
            print(f'Salvando no log: {msg_formatada}')
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        

class LogPrintMixin(Log):
    
    
    def _log(self, msg):
        print(msg, 'LogPrint MIXIN')



if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Parte de (error):')
    lp.log_success('Parte de (success):')
    

    lf = LogFileMixin()
    lf.log_error('Parte de:')
    lf.log_success('Parte de:')

    # print(LOG_FILE)