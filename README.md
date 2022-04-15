# Test-SharingCloud

Pour lancer le projet pour la première fois, il faut se rendre dans le répértoire _repo_/sharingCloud puis executer la commande permettant de migrer les modeles dans la base de données :
Windows :

```
py manage.py migrate
```

UNIX :

```
python manage.py migrate
```

<br/>
Pour lancer le serveur, executez toujours dans _repo_/sharingCloud :
Windows :
```
py manage.py runserver
```
UNIX :
```
python manage.py runserver
```
<br/>
Pour ajouter, modifier et supprimer des ressources, il faut avoir un compte admin.
Pour se créer un compte admin, entrez dans le terminal, toujours au niveau de _repo_/sharingCloud :

Windows :

```
py manage.py createsuperuser
```

UNIX :

```
python manage.py createsuperuser
```

Il faut ensuite se rendre sur la page dédié aux admins, pour cela, entrez à la fin de l'url du site : "admin".
