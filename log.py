import re
import datetime
from collections import defaultdict

# Définir les seuils pour les tentatives de connexion suspectes
max_attempts = 5 # Nombre maximal de tentatives de connexion
timeframe = 30 # Intervalle de temps en minutes pour les tentatives de connexion

# Définir les heures de travail
start_time = datetime.time(8, 0, 0)
end_time = datetime.time(17, 0, 0)

# Initialiser les compteurs pour les adresses IP suspectes
ip_count = defaultdict(int)

# Ouvrir le fichier journal de serveur
with open("server_log.txt", "r") as f:
    # Parcourir chaque ligne du fichier
    for line in f:
        # Utiliser une expression régulière pour extraire l'adresse IP, le nom d'utilisateur et l'heure de la connexion
        match = re.match(r'(\d+\.\d+\.\d+\.\d+)\s+\S+\s+(\S+)\s+\[(.*?)\]', line)
        if match:
            ip = match.group(1)
            user = match.group(2)
            time_str = match.group(3)
            time = datetime.datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S %z')

            # Vérifier si l'heure est en dehors des heures normales de travail
            if time.time() < start_time or time.time() > end_time:
                ip_count[ip] += 1

            # Vérifier si le nom d'utilisateur est erroné ou inexistant
            if user == "-" or user == "guest":
                ip_count[ip] += 1

            # Vérifier si l'adresse IP a un nombre élevé de tentatives de connexion dans un intervalle de temps court
            recent_attempts = sum(1 for t in attempts[ip] if (time - t).total_seconds() < timeframe*60)
            if recent_attempts >= max_attempts:
                ip_count[ip] += 1

            # Ajouter la tentative de connexion à la liste des tentatives pour cette adresse IP
            attempts[ip].append(time)

# Générer une liste des adresses IP suspectes et du nombre de tentatives de connexion suspectes pour chacune d'entre elles
suspect_ips = [(ip, count) for ip, count in ip_count.items() if count > 0]

# Trier la liste par ordre décroissant du nombre de tentatives de connexion suspectes
suspect_ips.sort(key=lambda x: x[1], reverse=True)

# Afficher les adresses IP suspectes et le nombre de tentatives de connexion suspectes pour chacune d'entre elles
for ip, count in suspect_ips:
    print(f"Adresse IP suspecte : {ip} - Nombre de tentatives de connexion suspectes : {count}")

