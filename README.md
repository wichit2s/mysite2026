

   D:
   mkdir Github
   cd Github
   mkdir wichit2s
   cd wichit2s
   gh repo clone wichit2s/mysite2026
   cd mysite2026
   uv init
   uv add django
   uv run django-admin startproject mysite .
   uv run manage.py runserver 0.0.0.0:80

