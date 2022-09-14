import smtplib 
from email.message import EmailMessage
import datetime

class LogMail():

   def __init__(self,receiver_email_address,nivel, message, object):
      self.receiver_email_address=receiver_email_address
      self.nivel = nivel
      self.message = message
      self.object = object
      self.sender_email_address = "correoalterno5000@gmail.com"

   def get_colores(self) -> tuple[str, str]:
       fondo = 'RED'
       color = 'BLUE'
       if self.nivel == 'INFO':
           fondo = 'RED'
           color = 'BLUE'
       elif self.nivel == 'WARNING':
           fondo = 'BLCK'
           color = 'YELLOW'
       elif self.nivel == 'ERROR':
           fondo = 'BLUE'
           color = 'RED'
       elif self.nivel == 'DEBUG':
           fondo = 'BLACK'
           color = 'MAGENTA'
       return (fondo, color)

   
   def send_email(self):
      try: 
        message = EmailMessage() 

        message['Subject'] = 'Log aplicación ...'
        message['From'] =  self.sender_email_address
        message['To'] = self.receiver_email_address
        email_smtp = "smtp.gmail.com" 
        email_password = "andres.amezquita01"

        now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
        color, fondo = self.get_colores()

        wrapper  = """
            <!DOCTYPE html> 
            <head> 
            </head>    
            <body>        
            <h1>Log Aplicación</h1>        
            <p style="background-color:%s; color:%s;">%s %s %s %s</p>        
            </body> 
            </html>
        """
        file_content =  wrapper % (fondo,color,now,self.nivel,self.message,self.object)

        message.set_content(file_content, subtype='html')
    
        server = smtplib.SMTP(email_smtp, 587) 
        server.ehlo() 
        server.starttls() 
        server.login(self.sender_email_address, email_password) 
        server.send_message(message) 
        server.quit()
      except smtplib.SMTPAuthenticationError:
          raise smtplib.SMTPAuthenticationError(100, "Error en autenticación del SMTP")

