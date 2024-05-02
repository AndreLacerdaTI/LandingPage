from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        # Preencha as informações do seu servidor SMTP
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'nean1020@gmail.com'
        smtp_password = 'ciun juch xzoq lkla'

        # Recupere os dados do formulário
        recipient = request.form['recipient']
        subject = request.form['subject']
        message = request.form['message']

        # Configurar o email
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Conecte-se ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Envie o email
        server.send_message(msg)

        # Feche a conexão
        server.quit()

        return 'E-mail enviado com sucesso!'
    else:
        return 'Método inválido'

if __name__ == '__main__':
    app.run(debug=True)
