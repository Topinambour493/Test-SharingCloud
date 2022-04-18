# Test-SharingCloud

Ce projet est un site de gestions de ressources, on peut acceder à la liste des ressources et voir le détail de chacunes d'elles.
Il y a un système d'authentification, seuls les personnes connectés peuvent se connecter au site.
Seuls les admins peuvent ajouter, modifier et supprimer des ressources.

## Premier lancement

Dès qu'il faut executer une commande contenant `manage.py`, il faut se rendre dans le répértoire _repo_/sharingCloud  (là où se situe le fichier ) :

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
