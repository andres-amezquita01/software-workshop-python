import smtplib 
from email.message import EmailMessage
import datetime

class LogMail():

   def __init__(self,receiver_email_address,nivel, message, object):
      self.receiver_email_address=receiver_email_address
      self.nivel = nivel
      self.message = message
      self.object = object
      self.sender_email_address = "su_correo@gmail.com" 
   
   def send_email(self):
      message = EmailMessage() 

      message['Subject'] = 'Log aplicación ...'
      message['From'] =  self.sender_email_address
      message['To'] = self.receiver_email_address
      email_smtp = "smtp.gmail.com" 
      email_password = "clavequegeneragmail" 

      now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

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

      server = smtplib.SMTP(email_smtp, '587') 
      server.ehlo() 
      server.starttls() 
      server.login(self.sender_email_address, email_password) 
      server.send_message(message) 
      server.quit()