## アプリの機能  
1．動画の再生  
2．動画の分割(開発中)  
3．動画のアップロード  

## 操作手順   
1.git clone https://github.com/j17012/video.git  
2.cd video  
3.pip3 install -r requirements.txt  
4.python3 manage.py migrate  
5.python3 manage.py runserver  
6.http://localhost:8000/top/  

## エラーとその解決策
操作手順3.「ModuleNotFoundWrror:No module named 'skbuild'」    
→pip3 install -U pip  
