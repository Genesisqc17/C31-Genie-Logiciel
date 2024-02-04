# Définir le nom de votre repository(dépôt) dans la variable suivante :
# Ne PAS mettre .git
SET gitHubRepository=C31-Genie-Logiciel
SET gitHubUsername=genesisqc17

C:
cd travail
IF NOT EXIST %gitHubRepository% git clone https://github.com/%gitHubUsername%/%gitHubRepository%
pause