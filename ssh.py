import paramiko

# Informations de connexion SSH
hostname = '192.168.112.123'
port = 22  # Port SSH par défaut
username = 'theo'
password = ' '

# Créer une instance de SSHClient
ssh = paramiko.SSHClient()

# Ignorer les erreurs d'authenticité de l'hôte (attention en production)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.set_missing_host_key_policy(paramiko.RejectPolicy())
#ssh.set_missing_host_key_policy(paramiko.WarningPolicy())

# Établir la connexion SSH
ssh.connect(hostname, port, username, password)

# Exécuter une commande à distance
stdin, stdout, stderr = ssh.exec_command('sudo su ' '')
stdin, stdout, stderr = ssh.exec_command('asterisk -rvvvv')

# Lire la sortie de la commande
output = stdout.read().decode('utf-8')

# Afficher la sortie
print(output)

# Fermer la connexion SSH
ssh.close()
 