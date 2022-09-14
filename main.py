import log_class.logger_factory_impl as lfi
import smtplib 

def main() -> None:
    type_logger = str(input("""
        [c]Para salida por consola
        [f]Para salida hacia el archivo
        [e]Para salida por email
        >>>: """))
    try:
        logger = lfi.LoggerFactoryImpl().get_logger(type=type_logger)
        logger.info('Mensage generico', 200)
        logger.warning('Mensage generico', 404)
        logger.error('Mensage generico', 401)
        logger.debug('Mensage generico', 500)
    except KeyError as error:
        print(str(error))
    except smtplib.SMTPAuthenticationError as error:
        print(str(error.strerror))
    except Exception as error:
        print('Unknown error' + str(error))

if __name__ == '__main__':
    main()
