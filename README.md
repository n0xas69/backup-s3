Script python permettant de sauvegarder des fichiers depuis un système linux sur un backup storage scaleway utilisant le protocole S3.

plus d'info : https://www.scaleway.com/en/docs/object-storage-with-s3cmd/

## utilisation

Installer s3cmd :

``` bash
# télécharger s3cmd
pip3 install s3cmd

# déplacer le binaire si nécessaire
mv ~/.local/bin/s3cmd /usr/local/bin
```

Configurer s3cmd en créant le fichier .s3cfg à la raçine du home
``` bash
vim ~/.s3cfg
```

``` init
[default]
# Object Storage Region
host_base = https://s3.fr-par.scw.cloud
host_bucket = https://bucket.s3.fr-par.scw.cloud
bucket_location = fr-par
use_https = True

# Login credentials
access_key = 
secret_key = 

```

Configurer les variables du script "backup.py" et il est prêt à être utilisé.

