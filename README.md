# Test-SharingCloud

Ce projet est un site de gestions de ressources, on peut acceder à la liste des ressources et voir le détail de chacunes d'elles.
Il y a un système d'authentification, seuls les personnes connectés peuvent se connecter au site.
Seuls les admins peuvent ajouter, modifier et supprimer des ressources.

## Premier lancement

Dès qu'il faut executer une commande contenant `manage.py`, il faut se rendre dans le répértoire _repo_/sharingCloud  (là où se situe ce fichier ) :

__Lancement des migrations :__
Windows :
```py manage.py migrate```

UNIX :
```python manage.py migrate```

__Lancement du serveur :__
Windows :
```py manage.py runserver```

UNIX :
```python manage.py runserver```

### Admins

__Création d'un compte admin :__

Windows :
```py manage.py createsuperuser```

UNIX :
```python manage.py createsuperuser```

__Transformer un user en admin :__

Windows :
```py manage.py user_to_superuser username```

UNIX :
```python manage.py user_to_superuser username```

__Transformer un admin en user:__

Windows :
```py manage.py superuser_to_user username```

UNIX :
```python manage.py superuser_to_user username```

### Améliorations possibles

* Ajouter un système de filtres par nom, type et capacité.
* Prédéfinir les types pour les associer à une ressource. Actuellement le type est un string à écrire manuellement pour chaque ressource.
* Faire en sorte que le reste des infos s'affiche à la suite du nom et du type lors du clic sur une ressource dans la page index (uniquement pour les users). Actuellement, au clic, l'user est renvoyé sur la page détail de la ressource.
* Ajouter des seeders pour les ressources.
