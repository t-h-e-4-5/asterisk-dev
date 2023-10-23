import paramiko
import getpass

# Informations de connexion SSH
hostname = '192.168.112.123'
port = 22
username = 'theo'
password = ' '

# Créer une instance de SSHClient
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Établir la connexion SSH
ssh.connect(hostname, port, username, password)

# Ouvrir un canal interactif
channel = ssh.invoke_shell()

# Exécuter la commande "sudo su"
channel.send('sudo su\n')
while not channel.recv_ready():
    pass
output = channel.recv(4096).decode('utf-8')
print(output)

# Envoyer le mot de passe
sudo_password = getpass.getpass(prompt='Mot de passe sudo : ')
channel.send(sudo_password + '\n')
while not channel.recv_ready():
    pass
output = channel.recv(4096).decode('utf-8')
print(output)

# Exécuter d'autres commandes en tant que superutilisateur
channel.send('asterisk -rvvvvv\n')
while not channel.recv_ready():
    pass
output = channel.recv(4096).decode('utf-8')
print(output)

# Fermer le canal et la connexion SSH
channel.close()
ssh.close()
