# django_rest_framework_test
- 参考ページ  
https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8

- migrationファイルを作る   
python manage.py makemigrations  
- migrationファイルを元にDBに反映する    
python manage.py migrate  

- admin用のユーザー作成  
python manage.py createsuperuser  
   Username (leave blank to use 'kimihiro_n'): dev  
   Email address:  
   Password:  
   Password (again):  
   Superuser created successfully.  

- 開発サーバーを起動  
python manage.py runserver  
